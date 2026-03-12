import shutil
from pathlib import Path
from typing import List, Set

def create_folder(path: Path, name: str) -> Path:
    folder_path = path / name
    folder_path.mkdir(exist_ok=True)
    return folder_path

def get_all_files(path: Path) -> List[Path]:
    try:
        return [p for p in path.iterdir() if p.is_file()]
    except FileNotFoundError as e:
        print(e)
        return []

def get_unique_extensions(files: List[Path]) -> Set[str]:
    extensions = set()
    for file in files:
        ext = file.suffix.lower()
        if ext:
            extensions.add(ext[1:])
    return extensions

def move_file(file_path: Path, dest_folder: Path) -> None:
    shutil.move(file_path, dest_folder / file_path.name)