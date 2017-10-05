# -*-coding:utf-8-*-
from PyQt4.QtGui import *
from PyQt4.Qt import *
from PyQt4.QtCore import *


class AboutUsDialog(QDialog):
    def __init__(self, parent=None):
        super(AboutUsDialog, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    aboutus = AboutUsDialog()
    aboutus.show()
    sys.exit(app.exec_())