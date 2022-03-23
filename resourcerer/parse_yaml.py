from pathlib import Path
import yaml


def get_yaml_obj(path: Path):
    """Loads a YAML file as a dictionary."""
    with open(path, "r") as f:
        resources_obj = yaml.full_load(f)
    return resources_obj
