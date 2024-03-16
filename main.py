from sys import argv
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from ui import Window

if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(argv)
    w = Window()
    w.show()
    app.exec_()
