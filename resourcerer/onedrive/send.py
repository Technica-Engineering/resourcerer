import requests

from resourcerer.onedrive.model import ApiToken, SiteId
from resourcerer.types import UploadSourcePath, UploadTargetPath
from resourcerer.utils import (try_from_response, response_content_to_dict, upload_file)
from resourcerer.onedrive.auth import auth_token
from resourcerer.onedrive.env import SITE_ID, CLIENT_ID, TENANT_ID, SECRET
from logging import getLogger
from resourcerer.log import add_handlers

# "@odata.type" => "microsoft.graph.driveItemUploadableProperties",
#                         "@microsoft.graph.conflictBehavior" => "rename",
#                         "name" => $file_name

log = getLogger(__name__)
add_handlers(log)


def _send_to_onedrive(
    token: ApiToken,
    site_id: SiteId,
    item_path: UploadSourcePath,
    target_path: UploadTargetPath
):
    upload_request_headers = {
        "Authorization": f"Bearer {token}"
    }
    upload_request_body = {
        "item": {
            "@microsoft.graph.conflictBehavior": "replace",
        }
    }
    upload_session_start_url = \
        f"https://graph.microsoft.com/v1.0/sites/{site_id}" + \
        f"/drive/root:/{item_path}:/createUploadSession"
    log.info(upload_session_start_url)
    resp = requests.post(upload_session_start_url,
                         headers=upload_request_headers, json=upload_request_body)
    upload_url = try_from_response(response_content_to_dict(
        resp), "uploadUrl", "Response did not contain upload URL. Failed to start upload session")
    upload_file(target_path, upload_url)
    log.info(f"Upload succesful. File located at: {item_path}")


def send_to_onedrive(item_path: UploadSourcePath, target_path: UploadTargetPath):
    return _send_to_onedrive(
        auth_token(CLIENT_ID, TENANT_ID, SECRET), SITE_ID, item_path, target_path)
