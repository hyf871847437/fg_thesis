# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
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
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 220, 101, 41))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 220, 101, 41))
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 240, 21, 16))
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 240, 21, 16))
        self.pushButton_5.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(75, -12, 371, 291))
        self.label.setStyleSheet(_fromUtf8("border-image: url(:/pic/1.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 70, 301, 141))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"Franklin Gothic Medium\";\n"
""))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_2.raise_()
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
        self.pushButton_2.setText(_translate("MainWindow", "论文降重", None))
        self.pushButton_3.setText(_translate("MainWindow", "论文查重", None))
        self.pushButton_4.setText(_translate("MainWindow", "X", None))
        self.pushButton_5.setText(_translate("MainWindow", "i", None))

import qrc_rc
