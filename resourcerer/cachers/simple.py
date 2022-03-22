from pathlib import Path


def _simple_strategy_is_cached(
    target_file_name: str,
    target_file_directory: Path,
) -> bool:
    if not target_file_directory.exists():
        return False
    for f in target_file_directory.iterdir():
        if f.name == target_file_name:
            return True
    else:
        return False
