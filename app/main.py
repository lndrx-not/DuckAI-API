import sys
import webbrowser

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl


GITHUB_URL = "https://github.com/lndrx-not"
REPOSITORY_URL = "https://github.com/lndrx-not/DuckAI-API"


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("About DuckAI-API")
        self.setFixedSize(400, 220)

        title = QLabel("DuckAI-API")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        description = QLabel(
            "Developed with Python and PySide6."
        )
        description.setWordWrap(True)

        author = QLabel("Autor: TU_NOMBRE")

        github_button = QPushButton("Open GitHub")
        github_button.clicked.connect(
            lambda: webbrowser.open(GITHUB_URL)
        )

        repository_button = QPushButton("Open repo")
        repository_button.clicked.connect(
            lambda: webbrowser.open(REPOSITORY_URL)
        )

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(github_button)
        buttons_layout.addWidget(repository_button)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(description)
        layout.addWidget(author)
        layout.addLayout(buttons_layout)
        layout.addStretch()
        layout.addWidget(close_button, alignment=Qt.AlignRight)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Duck.ai")
        self.resize(1200, 800)

        self.browser = QWebEngineView()
        self.browser.load(QUrl("https://duck.ai/"))
        self.setCentralWidget(self.browser)

        menu = self.menuBar().addMenu("Help")

        about_action = menu.addAction("About")
        about_action.triggered.connect(self.show_about)

        github_action = menu.addAction("Open GitHub")
        github_action.triggered.connect(
            lambda: webbrowser.open(GITHUB_URL)
        )

    def show_about(self):
        dialog = AboutDialog(self)
        dialog.exec()


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
