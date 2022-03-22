from pathlib import Path
from resourcerer._conf import CACHERS


def is_cached(
    target_file_name: str,
    target_file_directory: Path,
    cacher_name: str
) -> bool:
    """Checks whether a file exists in a given directory
    (whether it's cached).

    Args:
        target_file_name (:obj:`str`): filename to search for
        target_file_directory (:obj:`str`): path to the directory
            where to search for a given file

    Returns:
        :obj:`bool`, `True` if the file has been found,
        `False` otherwise
    """

    return CACHERS[cacher_name](target_file_name, target_file_directory)
