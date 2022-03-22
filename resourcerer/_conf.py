from collections import defaultdict
from typing import Dict
from resourcerer.cachers.simple import _simple_strategy_is_cached
from resourcerer.exceptions import UnknownCachingStrategy
from resourcerer.types import CacheResolverFunc

# add extra cachers here:
_registered_cachers: Dict[str, CacheResolverFunc] = {
    "simple": _simple_strategy_is_cached
}


def _handle_unknown_cacher():
    raise UnknownCachingStrategy("The called caching strategy is unknown, check `_conf.py`")


CACHERS = defaultdict(_handle_unknown_cacher)
CACHERS.update(_registered_cachers)
