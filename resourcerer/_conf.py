from collections import defaultdict
from typing import Dict
from resourcerer.cachers.simple import _simple_strategy_is_cached
from resourcerer.exceptions import UnknownCachingStrategy, UknownSource
from resourcerer.types import CacheResolverFunc, SourceInterfaces
from resourcerer.onedrive.get import download_from_onedrive
from resourcerer.onedrive.send import send_to_onedrive

# add extra cachers here:
_registered_cachers: Dict[str, CacheResolverFunc] = {
    "simple": _simple_strategy_is_cached,
}

# add extra sources here:
_registered_sources: Dict[str, SourceInterfaces] = {
    "onedrive": (download_from_onedrive, send_to_onedrive),
    "generic": ()
}


def _handle_unknown_cacher():
    raise UnknownCachingStrategy("The called caching strategy is unknown, check `_conf.py`")


def _handle_unknown_source():
    raise UknownSource("The source requested has no driver, check `_conf.py`")


CACHERS = defaultdict(_handle_unknown_cacher)
CACHERS.update(_registered_cachers)

SOURCES = defaultdict(_handle_unknown_source)
SOURCES.update(_registered_sources)
