from typing import Callable, Optional, Tuple
from pathlib import Path

CacheResolverFunc = Callable[[str, Path], bool]
SourcePath = Path
TargetPath = Optional[Path]
UploadSourcePath = Path
UploadTargetPath = Path
CheckCacheFirst = bool
CachingStrategy = str
SenderFunc = Callable[[SourcePath, TargetPath, CheckCacheFirst, CachingStrategy], None]
DownloaderFunc = Callable[[UploadSourcePath, UploadTargetPath], None]
SourceInterfaces = Tuple[DownloaderFunc, SenderFunc]
