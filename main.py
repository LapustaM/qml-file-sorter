from utils import create_folder, get_all_filenames, get_all_extensions, move_file
import os

path = str(r"D:\Test_sort")

filenames = get_all_filenames(path)
print(filenames)
extensions = get_all_extensions(filenames)
print(extensions)

for extension in extensions:
    create_folder(path, extension)
    for filename in filenames:
        if filename.endswith(extension):
            move_file(path, os.path.join(path, extension), filename)