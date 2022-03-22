import os
import json
from typing import Any, Dict
import requests
from logging import getLogger
from resourcerer.log import add_handlers

log = getLogger(__name__)
add_handlers(log)


def try_from_response(resp_dict: Dict[str, Any], dict_key: str, error_msg: str):
    try:
        val = resp_dict[dict_key]
        return val
    except KeyError:
        log.error(resp_dict)
        raise KeyError(error_msg)


def response_content_to_dict(resp):
    return json.loads(str(resp.content, encoding='utf-8'))


def download_file(name, url):
    # snatched from:
    # https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
    # NOTE the stream=True parameter below
    # NOTE if needed, MS Graph API supports Range header, e.g. `Range: bytes=0-1023`.
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        p = os.path.split(name)
        pre_path = os.path.join(*p[:-1])
        filename = p[-1]
        if not os.path.exists(pre_path):
            os.makedirs(pre_path)
        with open(os.path.join(pre_path, filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return name


def read_in_chunks(file_object, chunk_size=65536):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def upload_file(name, url):
    # adapted from: https://gist.github.com/nbari/7335384
    p = os.path.split(name)
    pre_path = os.path.join(*p[:-1])
    filename = p[-1]
    headers = {}
    index = 0
    content_size = os.stat(os.path.abspath(name)).st_size
    with open(os.path.join(pre_path, filename), 'rb') as f:
        for chunk in read_in_chunks(f, 327680):
            offset = index + len(chunk)
            headers['Content-Type'] = 'application/octet-stream'
            headers['Content-Length'] = str(content_size)
            headers['Content-Range'] = f'bytes {index}-{offset-1}/{content_size}'
            r = requests.put(url, data=chunk, headers=headers)
            # log.info(r.json())
            r.raise_for_status()
            log.info(f"Uploading {filename} bytes: {index}-{offset-1}, response: {r.status_code}")
            index = offset
    return name
