# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTextCodec
from PyQt4.QtGui import QMainWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QMainWindow,QtGui.QWidget):
    def __init__(self,parent=None):

        QMainWindow.__init__(self,parent)
       # self.initUI()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(518, 331)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 20, 101, 41))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 220, 101, 41))
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 220, 101, 41))
        self.pushButton_5.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 240, 21, 16))
        self.pushButton_6.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 240, 21, 16))
        self.pushButton_7.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(75, -12, 371, 291))
        self.label.setStyleSheet(_fromUtf8("border-image: url(1.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "论文生成", None))
        self.pushButton_4.setText(_translate("MainWindow", "论文降重", None))
        self.pushButton_5.setText(_translate("MainWindow", "论文查重", None))
        self.pushButton_6.setText(_translate("MainWindow", "X", None))
        self.pushButton_7.setText(_translate("MainWindow", "i", None))

if __name__ == "__main__":
    import sys

    reload(sys)
    sys.setdefaultencoding('utf8')

    app = QtGui.QApplication(sys.argv)
    myapp = Ui_MainWindow()
    # myapp.setWindowOpacity(0.1)
    myapp.show()
    app.exec_()

import qrc_rc
