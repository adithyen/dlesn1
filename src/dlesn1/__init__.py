"""
dlesn1: Deep Learning Lab 1 Experiments and Notebooks.
"""

from pathlib import Path
import shutil
from typing import List

__version__ = "0.1.0"

DATA_DIR = Path(__file__).resolve().parent / "data"


def list_files() -> List[str]:
    """Return a list of all experiment notebooks in the package."""
    if not DATA_DIR.exists():
        return []
    return sorted([f.name for f in DATA_DIR.iterdir() if f.is_file()])


def list_notebooks() -> List[str]:
    """Return a list of all Jupyter notebooks in the package."""
    return [f for f in list_files() if f.endswith(".ipynb")]


def get_path(filename: str) -> Path:
    """Get the absolute Path of a file inside the package."""
    target = DATA_DIR / filename
    if not target.exists():
        raise FileNotFoundError(
            f"File '{filename}' not found in dlesn1 data. Available files:\n"
            + "\n".join(f" - {f}" for f in list_files())
        )
    return target


def extract(dest: str = ".", overwrite: bool = False) -> List[Path]:
    """
    Extract all notebooks into the target directory.
    
    :param dest: Destination directory (default is current directory '.')
    :param overwrite: Whether to overwrite existing files (default False)
    :return: List of copied file paths
    """
    dest_path = Path(dest).resolve()
    dest_path.mkdir(parents=True, exist_ok=True)
    copied = []

    for file_path in DATA_DIR.iterdir():
        if file_path.is_file():
            target = dest_path / file_path.name
            if target.exists() and not overwrite:
                continue
            shutil.copy2(file_path, target)
            copied.append(target)

    return copied


def download(dest: str = ".", overwrite: bool = False) -> List[Path]:
    """Alias for extract()."""
    return extract(dest=dest, overwrite=overwrite)


__all__ = [
    "__version__",
    "DATA_DIR",
    "list_files",
    "list_notebooks",
    "get_path",
    "extract",
    "download",
]
