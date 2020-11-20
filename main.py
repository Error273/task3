import sys

from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def draw_circle(self):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255))))
        size = randint(0, 400)
        qp.drawEllipse(randint(0, 400), randint(0, 400), size, size)
        qp.end()

    def paintEvent(self, event):
        if self.do_paint:
            self.draw_circle()

    def paint(self):
        self.do_paint = True
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())