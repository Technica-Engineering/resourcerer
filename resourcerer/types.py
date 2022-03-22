from typing import Callable
from pathlib import Path

CacheResolverFunc = Callable[[str, Path], bool]
