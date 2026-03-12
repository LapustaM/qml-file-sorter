import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts
import Qt.labs.platform


ApplicationWindow {
    id: root
    visible: true
    width: 600
    height: 400
    title: "File Sorter"

    Material.theme: Material.Dark
    Material.accent: Material.Red

    property string folderPath: ""

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 24

        Text {
            text: "Simple file sorter"
            font.pixelSize: 32
            font.bold: true
            color: "white"
            Layout.alignment: Qt.AlignCenter
        }

        Text {
            text: "Organize your files by their extensions"
            font.pixelSize: 20
            color: "white"
            Layout.alignment: Qt.AlignCenter
            Layout.bottomMargin: 20
        }

        RowLayout {
            Layout.alignment: Qt.AlignCenter
            spacing: 10

            TextField {
                id: pathField
                placeholderText: "Select folder"
                readOnly: true
                Layout.preferredWidth: 300
            }

            Button {
                text: "Browse"
                onClicked: folderDialog.open()
            }
        }

        Button {
            text: "Sort files"
            Layout.alignment: Qt.AlignCenter
            Layout.preferredWidth: 200
            Material.background: Material.accent

            enabled: root.folderPath !== ""

            onClicked: {
                backend.sortFiles(root.folderPath)
            }
        }

        Label {
            id: statusLabel
            text: backend.status
            color: "#4CAF50"
            font.bold: true
            font.pixelSize: 16
            Layout.alignment: Qt.AlignHCenter
        }

        FolderDialog {
            id: folderDialog
            title: "Please choose a folder"
            onAccepted: {
                root.folderPath = folderDialog.folder
                pathField.text = folderDialog.folder.toString().replace("file:///", "")
            }
        }
    }
}
