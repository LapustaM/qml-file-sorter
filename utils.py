import os

def create_folder(path: str, name: str) -> None:
    folder_path = os.path.join(path, name)
    try:
        os.mkdir(folder_path)
    except FileExistsError as e:
        print(e)