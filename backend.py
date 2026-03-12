from PySide6.QtCore import QObject, Slot, Signal, Property, QUrl
from pathlib import Path
from utils import create_folder, get_all_files, get_unique_extensions, move_file


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

        path_str = QUrl(path_url).toLocalFile()
        path = Path(path_str)

        if not path.is_dir():
            self.status = "Invalid directory"
            return

        self.status = "Sorting..."
        try:
            files = get_all_files(path)

            if not files:
                self.status = "No files found"
                return

            extensions = get_unique_extensions(files)

            for extension in extensions:
                target_folder = create_folder(path, extension)
                for file in files:
                    if file.suffix.lower() == f".{extension}":
                        move_file(file, target_folder)

            self.status = "Done!"
        except Exception as e:
            self.status = f"Error: {str(e)}"
            print(f"Sort error: {e}")