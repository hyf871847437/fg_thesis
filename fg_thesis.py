# -*- coding: utf-8 -*-
from PyQt4.QtGui import QMainWindow,QDialog
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import pyqtSignature,Qt,pyqtSignal,QThread,QTextCodec,QEvent
from main_page import Ui_MainWindow
from create22 import Ui_Dialog4
from decrease2 import Ui_Dialog
from thesis_rate import Ui_Dialog3
import docx

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8")) #设置编码格式的，其实我也不知何地


# 从文档中读取论文
def read_docx(filename):
    doc = docx.Document(filename)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)

class Mythread(QtCore.QThread):  #创建多线程
    send_text = pyqtSignal(str)

    def __init__(self, func, *args):
        super(Mythread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        text = self.func(self.args)
        self.send_text.emit(text)

class Form1(QDialog,Ui_Dialog4):                #论文生成
    def __init__(self,parent=None):
        send_text = pyqtSignal(str)

        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.setFixedSize(699, 665)
        self.th = QThread()

class Form2(QDialog,Ui_Dialog):            #降重界面
    def __init__(self,parent=None):
        send_text = pyqtSignal(str)
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.setFixedSize(602, 164)

class Form3(QDialog,Ui_Dialog3):            #查重界面
    def __init__(self,parent=None):
        send_text = pyqtSignal(str)
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.setFixedSize(602, 164)



class MainWindow(QMainWindow,Ui_MainWindow):            #主要的界面

    def __init__(self,parent=None):

        QMainWindow.__init__(self,parent)
        self.initUI()
        self.setupUi(self)
        self.my_rate = []
        self.setFixedSize(518, 331)


    #论文生成
    @pyqtSignature('')
    def on_pushButton_clicked(self):
        my_info = Form1()
        my_info.exec_()

    #论文降重
    @pyqtSignature('')
    def on_pushButton_2_clicked(self):  # 打开txt,word文件
        my_info = Form2()
        my_info.exec_()

    #论文查重
    @pyqtSignature('')
    def on_pushButton_3_clicked(self):
        my_info = Form3()
        my_info.exec_()

    #关闭
    @pyqtSignature('')
    def on_pushButton_4_clicked(self):
        self.close()

    #关于fg
    @pyqtSignature('')
    def on_pushButton_5_clicked(self):
        if self.label_2.text() == '':
            self.label_2.setText(u'作者QQ：871847437\nemail：15736649521@163.com\n如有建议，非常欢迎。。。')
        else:
            self.label_2.setText('')

    # 设置界面可移动 ,原理我也不知道为什么
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QtGui.QApplication.postEvent(self, QEvent(174))
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    #隐藏窗口
    def initUI(self):
        #self.setAttribute(QtCore.Qt.WA_NoSystemBackground, False)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)




if __name__ == "__main__":

    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')

    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    #myapp.setWindowOpacity(0.1)
    myapp.show()
    app.exec_()
