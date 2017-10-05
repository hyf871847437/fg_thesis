# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from lxml import html
from PyQt4.QtCore import pyqtSignal
from translate import zh_en,en_zh
import requests


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


class Mythread(QtCore.QThread):  #创建多线程
    send_text = pyqtSignal(str)
    send_list = pyqtSignal(list)

    def __init__(self, func, *args):
        super(Mythread, self).__init__()
        self.moveToThread(self)   #稳定多了
        self.func = func
        self.args = args

    def run(self):
        text = self.func(self.args)
       # print type(text)
        if type(text) == list:
            self.send_list.emit(text)
        else:
            self.send_text.emit(text)


class Ui_Dialog4(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
       # Dialog.resize(1392, 633)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 30, 261, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 40, 93, 28))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{background-color:rgb(0, 170, 0);border:none;color:#ffffff;font-size:20px;}"
                                      "QPushButton:hover{background-color:#333333; }"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 30, 31, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(590, 60, 101, 20))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
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
        self.pushButton_2.setStyleSheet(_fromUtf8(("QPushButton{background-color:#16A085;border:none;color:rgb(74, 74, 0);font-size:20px;}"
                                      "QPushButton:hover{background-color:rgb(0, 255, 255);}")))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(5, 180, 691, 81))
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:rgb(74, 74, 0);font-size:20px;}"
                                      "QPushButton:hover{background-color:rgb(0, 255, 255);}"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(5, 270, 691, 81))
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:rgb(74, 74, 0);font-size:20px;}"
                                      "QPushButton:hover{background-color:rgb(0, 255, 255);}"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(5, 360, 691, 81))
        self.pushButton_5.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:rgb(74, 74, 0);font-size:20px;}"
                                      "QPushButton:hover{background-color:rgb(0, 255, 255);}"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(5, 450, 691, 81))
        self.pushButton_6.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:rgb(74, 74, 0);font-size:20px;}"
                                      "QPushButton:hover{background-color:rgb(0, 255, 255);}"))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(5, 540, 691, 81))
        self.pushButton_7.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:rgb(74, 74, 0);font-size:20px;}"
                                      "QPushButton:hover{background-color:rgb(0, 255, 255);}"))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(1290, 590, 93, 28))
        self.pushButton_8.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}"
                                      "QPushButton:hover{background-color:#333333;}"))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.textBrowser.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.line_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()

        self.pushButton.clicked.connect(self.get_href)
        self.pushButton_8.clicked.connect(self.decrease)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def reveal_search(self,lis):
        index = 2
        try:
            for content in lis[:6]:
                order_text = 'self.pushButton_%s.setText(content[0]+content[1])' % index
                eval(order_text)
                index += 1
            if lis != []:
                self.pushButton_2.clicked.connect(lambda: self.get_article(lis[0][0], lis[0][2].strip()))
                self.pushButton_3.clicked.connect(lambda: self.get_article(lis[1][0], lis[1][2].strip()))
                self.pushButton_4.clicked.connect(lambda: self.get_article(lis[2][0], lis[2][2].strip()))
                self.pushButton_5.clicked.connect(lambda: self.get_article(lis[3][0], lis[3][2].strip()))
                self.pushButton_6.clicked.connect(lambda: self.get_article(lis[4][0], lis[4][2].strip()))
                self.pushButton_7.clicked.connect(lambda: self.get_article(lis[5][0], lis[5][2].strip()))
            else:
                self.label_2.setText(u'！无效关键字')
        except Exception,e:
            print e
            self.label_2.setText(str(e))
       # print 'over'

    # 从超星发现系统获取文章连接, search按钮
    def get_href(self):
        self.label_2.setText('')
        keyword = self.lineEdit.text()
        if keyword != '':
            def get_page(keyword):
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
                url = 'http://ss.chaoxing.com/ncs?sw=%s&strchannel=72&x=0_97' % keyword
                r = requests.get(url, headers=headers,timeout=6)
                r.raise_for_status()
                tree = html.fromstring(r.text)
                base = tree.xpath('//tr[@class="zcon"]')

                for each in base:
                    summary = each.xpath('td[2]/h2/a')[0]
                    title = summary.xpath('string(.)')
                    href = each.xpath('td[2]/h2/a/@href')
                    author = each.xpath('td[2]/p/text()')
                    yield title+'\n', author[0], href[0]

            def return_lis(*args):
                try:
                    lis = list(get_page(keyword))
                    return lis
                except Exception, e:
                    print e
                    self.label_2.setText(str(e))

            self.thread2 = Mythread(return_lis)
            self.thread2.send_list.connect(self.reveal_search)  # 传递信号
            self.thread2.start()


    # 从链接中获取文章
    def get_article(self,title,url):
        self.label_2.setText(u'正在生成...')
        self.textBrowser.setText('')
        self.setFixedSize(1394, 633)
        self.title = title
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
        def write_thread(url):
            try:
                r = requests.get(url, headers=headers, timeout=6)
                tree = html.fromstring(r.text)
                base = tree.xpath('//div[@class="FtextCon"]/p')
                content = ''
                for each in base:
                    content = content + '\n' * 2 + each.xpath('string(.)')
                if content == '':
                    self.textBrowser.setText(u'%sNot Found,意思就是这篇文章没找到。。。翻页吧，少年' % self.title)
                else:
                    self.textBrowser.setText(content)
                self.label_2.setText(u'论文:%s' % (len(content)))
            except Exception, e:
                print e
                self.label_2.setText(str(e))
        write_thread(url)






    def reveal_result(self,my_data):
        self.textBrowser.setText(my_data)
        self.label_2.setText(u'降重完成:%s字' % len(my_data))
        self.pushButton_8.setDisabled(False)

    def decrease(self):
        self.label_2.setText(u'正在降重...')
        self.pushButton_8.setDisabled(True)
        def decrease_article(text):
            try:
                if type(text) == tuple:
                    text = text[0]
                my_data = zh_en(text)
                my_data = unicode(en_zh(my_data), 'unicode_escape')
              #  print type(my_data)
                return my_data

            except Exception, e:
                print e
                self.label_2.setText(str(e))

        self.thread1 = Mythread(decrease_article, u'%s' % self.textBrowser.toPlainText())  # 多线程连接函数
        self.thread1.send_text.connect(self.reveal_result)  # 传递信号
        self.thread1.start()  # 开始线程



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

