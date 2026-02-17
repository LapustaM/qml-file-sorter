import os
from contextlib import chdir

def create_folder(path: str, name: str) -> None:
    folder_path = os.path.join(path, name)
    try:
        os.mkdir(folder_path)
    except FileExistsError as e:
        print(e)

def get_all_filenames(path: str) -> list:
    try:
        with chdir(path):
            file_list = os.listdir(path)
            return file_list
    except FileNotFoundError as e:
        print(e)
        return []

def get_all_extensions(filenames: list) -> list:
        extensions = []
        for filename in filenames:
            extension = filename.split('.')[-1]
            if extension not in extensions:
                extensions.append(extension)
        return extensions