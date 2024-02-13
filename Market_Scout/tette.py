import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout


class YouTubeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('YouTube Video')
        self.setGeometry(250, 150, 1280, 720)

        self.youtube_view = QWebEngineView()
        self.youtube_view.load(QUrl('https://www.youtube.com/embed/FE2In6NKRN4'))

        layout = QVBoxLayout()
        layout.addWidget(self.youtube_view)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YouTubeWindow()
    window.show()
    sys.exit(app.exec())