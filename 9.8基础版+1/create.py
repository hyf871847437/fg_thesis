# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1392, 633)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 30, 261, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 40, 93, 28))
        self.pushButton.setStyleSheet(_fromUtf8("\n"
"QPushButton{background-color:#16A085;border:none;color: rgb(74, 74, 0);font-size:20px;}\"\n"
"QPushButton:hover{background-color:#16A085;}"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 30, 241, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(700, 0, 691, 621))
        self.textBrowser.setStyleSheet(_fromUtf8("background-color:#16A085;border:none;color:#ffffff;font-size:20px;\n"
""))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 80, 691, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(5, 90, 691, 81))
        self.pushButton_2.setStyleSheet(_fromUtf8("\n"
"QPushButton{background-color:rgb(0, 255, 255);border:none;color: rgb(74, 74, 0);font-size:20px;}\"\n"
"QPushButton:hover{background-color:#16A085;}"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(5, 180, 691, 81))
        self.pushButton_3.setStyleSheet(_fromUtf8("\n"
"QPushButton{background-color:rgb(0, 255, 255);border:none;color: rgb(74, 74, 0);font-size:20px;}\"\n"
"QPushButton:hover{background-color:#16A085;}"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(5, 270, 691, 81))
        self.pushButton_4.setStyleSheet(_fromUtf8("\n"
"QPushButton{background-color:rgb(0, 255, 255);border:none;color: rgb(74, 74, 0);font-size:20px;}\"\n"
"QPushButton:hover{background-color:#16A085;}"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(5, 360, 691, 81))
        self.pushButton_5.setStyleSheet(_fromUtf8("\n"
"QPushButton{background-color:rgb(0, 255, 255);border:none;color: rgb(74, 74, 0);font-size:20px;}\"\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(5, 450, 691, 81))
        self.pushButton_6.setStyleSheet(_fromUtf8("\n"
"QPushButton{background-color:rgb(0, 255, 255);border:none;color: rgb(74, 74, 0);font-size:20px;}\"\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(5, 540, 691, 81))
        self.pushButton_7.setStyleSheet(_fromUtf8("\n"
"QPushButton{background-color:rgb(0, 255, 255);border:none;color: rgb(74, 74, 0);font-size:20px;}\"\n"
"QPushButton:hover{background-color:#333333;}"))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(1290, 590, 93, 28))
        self.pushButton_8.setStyleSheet(_fromUtf8("background-color: rgb(170, 255, 255);\n"
"QPushButton{background-color:#16A085;border:none;color: rgb(74, 74, 0);font-size:20px;}\"\n"
"QPushButton:hover{background-color:#16A085;}"))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(590, 60, 101, 20))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.line_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "查询", None))
        self.label.setText(_translate("Dialog", "Fg", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_8.setText(_translate("Dialog", "降重", None))
        self.label_2.setText(_translate("Dialog", "论文：3000字", None))

