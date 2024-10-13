import sys

from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (
    QApplication,
    QDesktopWidget,
    QDialog,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def center_window(window):
    screen = QDesktopWidget().screenNumber(QDesktopWidget().cursor().pos())
    center_point = QDesktopWidget().screenGeometry(screen).center()
    frame_geometry = window.frameGeometry()
    frame_geometry.moveCenter(center_point)
    window.move(frame_geometry.topLeft())


class VideoPopup(QDialog):
    def __init__(self, video_path):
        super().__init__()
        self.setWindowTitle("Video Popup")
        self.resize(500, 175)  # Use resize instead of setGeometry

        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setStyleSheet("background-color: black;")

        # Create a main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Create a container widget
        container = QWidget()
        container.setAttribute(Qt.WA_TranslucentBackground)
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)

        # Create and add the video widget to the container
        self.video_widget = QVideoWidget()
        container_layout.addWidget(self.video_widget)

        # Add the container to the main layout
        main_layout.addWidget(container)

        # Set up the media player
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

        video_url = QUrl.fromLocalFile(video_path)
        self.media_player.setMedia(QMediaContent(video_url))

        self.media_player.mediaStatusChanged.connect(self.handle_media_status)

    def showEvent(self, event):
        center_window(self)  # Center the window before showing
        self.media_player.play()

    def handle_media_status(self, status):
        if status == QMediaPlayer.EndOfMedia:
            QTimer.singleShot(
                500, self.close
            )  # Close the dialog 500ms after video ends


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: black;")

        self.initUI()
        center_window(self)  # Center the main window

    def initUI(self):
        self.setWindowTitle("Video Popup Example")
        self.resize(300, 200)  # Use resize instead of setGeometry
        QTimer.singleShot(0, self.showVideoPopup)

    def showVideoPopup(self):
        video_path = r"C:\Users\aleks\Downloads\elysium_gamification_dev\elysium_gamification_event_server\vid.mp4"
        popup = VideoPopup(video_path)
        popup.exec_()
        self.closeAndQuit()

    def closeAndQuit(self):
        QApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
