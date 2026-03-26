import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QTimer, QUrl, Qt
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

from desktop import DesktopWindow

class BootWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remember OS 启动")
        self.showFullScreen()
        self.setCursor(Qt.CursorShape.BlankCursor)

        self.video_widget = QVideoWidget()
        self.setCentralWidget(self.video_widget)

        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(self.video_widget)

        self.media_player.setSource(QUrl.fromLocalFile("startup_animation.mp4"))
        self.media_player.setMuted(True)
        self.media_player.play()

        self.timer = QTimer()
        self.timer.timeout.connect(self.go_to_desktop)
        self.timer.start(10000)

    def go_to_desktop(self):
        self.media_player.stop()
        self.close()
        self.desktop = DesktopWindow()
        self.desktop.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BootWindow()
    window.show()
    sys.exit(app.exec())