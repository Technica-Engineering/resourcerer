from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Dict, List
from pathlib import Path
from collections import defaultdict
from resourcerer.parse_yaml import get_yaml_obj
from resourcerer.defaults import DEFAULT_CACHER, DEFAULT_SOURCE


@dataclass
class CliArgs:
    """Represents a container of CLI argument values that the
    program was called with.
    """
    file: Path
    verbosity: int


@dataclass()
class ResourcesYamlObj:
    """Represents the YAML file used to configure the tool
    at runtime.
    """
    download: List[Path]
    upload: List[Path]
    source_type: str
    root_source_dir: Path
    target_dir: Path
    caching_strategy: str = "simple"

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
            ddct["source_type"] or DEFAULT_SOURCE,
            Path(ddct["root_source_dir"] or "."),
            Path(ddct["target_dir"] or "."),
            ddct["caching_strategy"] or DEFAULT_CACHER
        )

    @classmethod
    def from_yaml(cls, yaml_file_path: Path) -> ResourcesYamlObj:
        """Loads the configuration model from a YAML file"""
        return cls.from_dict(get_yaml_obj(yaml_file_path))


@dataclass
class Config:
    cli: CliArgs
    yaml: ResourcesYamlObj
