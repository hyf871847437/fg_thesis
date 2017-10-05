# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lunwen.ui'
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

class Ui_Form_Main(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(589, 92)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 30, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 261, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 30, 93, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(240, 30, 31, 31))
        self.commandLinkButton.setText(_fromUtf8(""))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 30, 93, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "fg论文", None))
        self.pushButton.setText(_translate("Form", "论文生成", None))
        self.pushButton_2.setText(_translate("Form", "论文降重", None))
        self.pushButton_3.setText(_translate("Form", "论文查重", None))

