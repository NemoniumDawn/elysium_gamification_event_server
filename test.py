import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.msg = None  # Store the message box as an instance variable
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pop-up Example")
        self.setGeometry(300, 300, 300, 200)

        # Show the pop-up as soon as the window is created
        QTimer.singleShot(0, self.showPopup)

    def showPopup(self):
        self.msg = QMessageBox(self)
        self.msg.setWindowTitle("Simple Pop-up")
        self.msg.setText("This is a simple pop-up message!")
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.NoButton)  # No buttons needed

        # Show the message box
        self.msg.show()

        # Set a timer to close the message box after 2 seconds
        QTimer.singleShot(2000, self.closeAndQuit)

    def closeAndQuit(self):
        if self.msg:
            self.msg.close()
        QApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
