from dataclasses import dataclass
from typing import List
from pathlib import Path
from enum import Enum, auto


class CachingStrategy(Enum):
    """Algorithm switch for the caching of downloaded
    resources.
    
    - `SIMPLE` -> if a file with the same name exists in the target
                  folder, don't re-download
    """
    SIMPLE = auto()


@dataclass
class CliArgs:
    """Represents a container of CLI argument values that the
    program was called with.
    """
    pass


@dataclass
class ResourcesYamlObj:
    """Represents the YAML file used to configure the tool
    at runtime.
    """
    download: List[Path]
    upload: List[Path]
    root_source_dir: Path
    target_dir: Path
    caching_strategy: CachingStrategy = CachingStrategy.SIMPLE
