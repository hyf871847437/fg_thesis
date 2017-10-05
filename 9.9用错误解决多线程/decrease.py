# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decrease.ui'
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
        Dialog.resize(598, 701)
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(590, -10, 20, 711))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(-7, 0, 20, 711))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 100, 261, 41))
        self.lineEdit.setStyleSheet(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 110, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(110, 50, 115, 19))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 50, 115, 19))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 110, 93, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(85, 85, 127);\n"
"color: rgb(170, 255, 255);\n"
"font: 75 10pt \"Adobe Caslon Pro Bold\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 660, 93, 31))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(85, 85, 127);\n"
"color: rgb(170, 255, 255);\n"
"font: 75 10pt \"Adobe Caslon Pro Bold\";"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.textBrowser_2 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(600, -10, 581, 721))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(560, 120, 72, 15))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(570, 0, 31, 31))
        self.commandLinkButton.setText(_fromUtf8(""))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 90, 581, 561))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 670, 201, 16))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.textBrowser_2.raise_()
        self.label_2.raise_()
        self.commandLinkButton.raise_()
        self.label_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lineEdit.setText(_translate("Dialog", "未选择文件", None))
        self.pushButton.setText(_translate("Dialog", "选择文件", None))
        self.label.setText(_translate("Dialog", "上传方式：", None))
        self.radioButton.setText(_translate("Dialog", "文件上传", None))
        self.radioButton_2.setText(_translate("Dialog", "文字粘贴", None))
        self.pushButton_2.setText(_translate("Dialog", "降重", None))
        self.pushButton_3.setText(_translate("Dialog", "降重", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e6e6e6;\">我在这里输入</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "降重完成：5000字", None))

