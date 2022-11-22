import random
import sys

from PyQt5 import QtCore

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from qtpy import uic, QtGui


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.is_drawing = False
        self.coords = (0, 0)
        self.radius = 0
        self.color = (0, 0, 0)

    def draw_circle(self):
        self.is_drawing = True
        self.coords = (random.randint(20, 300), random.randint(20, 300))
        self.radius = random.randint(2, 60)
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.update()

    def paintEvent(self, event):
        if self.is_drawing:
            painter = QPainter()
            painter.begin(self)
            pen = QtGui.QPen(QColor(*self.color))
            pen.setWidth(5)
            painter.setPen(pen)

            painter.drawEllipse(self.coords[0], self.coords[1], self.radius, self.radius)
            painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    ex.show()
    sys.exit(app.exec())
