import os
from pathlib import Path


def is_cached(target_file_name: str, target_file_directory: Path):
    """Checks whether a file exists in a given directory
    (whether it's cached).

    Args:
        `target_file_name` (:obj:`str`): filename to search for
        `target_file_directory` (:obj:`str`): path to the directory
            where to search for a given file

    Returns:
        :obj:`bool`, `True` if the file has been found,
        `False` otherwise
    """
    if not target_file_directory.exists():
        return False
    for f in target_file_directory.iterdir():
        if f.name == target_file_name:
            return True
    else:
        return False
