from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from ui import MainWindow


def main():
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()
