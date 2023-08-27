import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class KrakenWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kraken")
        self.setGeometry(100, 100, 800, 600)  # Initial position (x, y) and size (width, height)
        self.setMinimumSize(400, 300)  # Set a minimum size for the window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KrakenWindow()
    window.show()
    sys.exit(app.exec_())