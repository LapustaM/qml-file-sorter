import pathlib
from utils import create_folder

path = str(pathlib.Path().resolve())
create_folder(path, 'images')