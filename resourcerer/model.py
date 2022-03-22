from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Dict, List
from pathlib import Path
from enum import Enum, auto
from collections import defaultdict
from resourcerer.parse_yaml import get_yaml_obj


class UnknownCachingStrategy(Exception):
    """Raised when an unknown caching strategy is used"""
    pass


class CachingStrategy(Enum):
    """Algorithm switch for the caching of downloaded
    resources.

    - `SIMPLE` -> if a file with the same name exists in the target
                  folder, don't re-download
    """
    SIMPLE = auto()

    @classmethod
    def from_str(cls, str_ipt: str) -> CachingStrategy:
        lookup_map = dict(
            simple=cls.SIMPLE
        )
        try:
            return CachingStrategy(lookup_map[str_ipt.lower()])
        except KeyError:
            raise UnknownCachingStrategy(f"Used {str_ipt}, available {list(lookup_map.keys())}")


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
        """Loads the configuration model from a dictionary"""
        ddct = defaultdict(lambda: None)
        # turn all keys to lowercase
        lowercase_key_dct = {k.lower(): v for k, v in dct.items()}
        # shove it into defaultdict:
        ddct.update(lowercase_key_dct)
        return ResourcesYamlObj(
            [Path(i) for i in ddct["download"] or []],
            [Path(i) for i in ddct["upload"] or []],
            Path(ddct["root_source_dir"] or "."),
            Path(ddct["target_dir"] or "."),
            CachingStrategy(ddct["caching_strategy"] or CachingStrategy.SIMPLE.value)
        )

    @classmethod
    def from_yaml(cls, yaml_file_path: Path) -> ResourcesYamlObj:
        """Loads the configuration model from a YAML file"""
        return cls.from_dict(get_yaml_obj(yaml_file_path))
