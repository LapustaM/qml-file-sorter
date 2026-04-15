# QML File Sorter 📂

A fast, lightweight desktop application built with Python and PySide6 (Qt) that automatically organizes messy folders by sorting files into subdirectories based on their extensions.

## Features
* **Intuitive GUI:** Modern and responsive user interface built with QML and Material Design.
* **Smart Sorting:** Automatically scans the selected directory and groups files (e.g., all `.pdf` files go to a `pdf` folder).
* **Asynchronous-ready Backend:** Clean separation of concerns between the Python backend logic and the QML frontend.

## Tech Stack
* **Language:** Python 3.14
* **GUI Framework:** PySide6 (Qt for Python), QML
* **File Operations:** Python built-in `pathlib` and `shutil`

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/LapustaM/qml-file-sorter.git
cd qml-file-sorter
```
2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```
4. Run the application:

```bash
python gui.py
```
<img width="594" height="423" alt="preview" src="https://github.com/user-attachments/assets/b3eee34c-d1e6-445c-92b5-102dbaebde70" />
