from PyQt5 import Qt
from PyQt5 import uic
import random


class MainWindow(Qt.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('unled.ui', self)
        self.setWindowTitle('Кружочки')
        self.scene = Qt.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        b = random.randrange(0, 500)
        rect = Qt.QRectF(random.randrange(0, 800) - b, random.randrange(0, 500) - b, b, b)
        color = Qt.Qt.yellow
        self.scene.addEllipse(rect, Qt.QPen(color), Qt.QBrush(color))


if __name__ == '__main__':
    app = Qt.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec()
