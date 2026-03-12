import os
from PySide6.QtCore import QObject, Slot, Signal, Property, QUrl
from utils import create_folder, get_all_filenames, get_all_extensions, move_file


class Backend(QObject):
    def __init__(self):
        super().__init__()
        self._status = "Ready"

    statusChanged = Signal()

    @Property(str, notify=statusChanged)
    def status(self):
        return self._status

    @status.setter
    def status(self, val):
        if self._status != val:
            self._status = val
            self.statusChanged.emit()

    @Slot(str)
    def sortFiles(self, path_url):
        if not path_url:
            self.status = "Please select a folder"
            return

        path = QUrl(path_url).toLocalFile()

        if not os.path.isdir(path):
            self.status = "Invalid directory"
            return

        self.status = "Sorting..."
        try:
            # get_all_filenames from utils returns os.listdir results (names only)
            all_items = get_all_filenames(path)

            # Filter to ensure we only process files, not subdirectories
            filenames = [f for f in all_items if os.path.isfile(os.path.join(path, f))]

            if not filenames:
                self.status = "No files found"
                return

            extensions = get_all_extensions(filenames)

            for extension in extensions:
                create_folder(path, extension)
                for filename in filenames:
                    if filename.endswith(f".{extension}"):
                        move_file(path, os.path.join(path, extension), filename)

            self.status = "Done!"
        except Exception as e:
            self.status = f"Error: {str(e)}"
            print(f"Sort error: {e}")