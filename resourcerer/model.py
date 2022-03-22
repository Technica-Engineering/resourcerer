from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Dict, List
from pathlib import Path
from enum import Enum, auto
from collections import defaultdict


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


@dataclass()
class ResourcesYamlObj:
    """Represents the YAML file used to configure the tool
    at runtime.
    """
    download: List[Path]
    upload: List[Path]
    root_source_dir: Path
    target_dir: Path
    caching_strategy: CachingStrategy = CachingStrategy.SIMPLE

    def __dict__(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dct: Dict[str, Any]) -> ResourcesYamlObj:
        ddct = defaultdict(default_factory=None)
        # turn all keys to lowercase
        lowercase_key_dct = {k.lower(): v for k, v in dct.items()}
        # shove it into defaultdict:
        ddct.update(lowercase_key_dct)
        return ResourcesYamlObj(
            ddct["download"] or [],
            ddct["upload"] or [],
            ddct["root_source_dir"] or Path("."),
            ddct["target_dir"] or Path("."),
            ddct["caching_strategy"] or CachingStrategy.SIMPLE
        )
