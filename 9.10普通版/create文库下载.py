# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from lxml import html
from PyQt4.QtCore import pyqtSignature,QStringList,Qt,pyqtSignal,QThread,QTextCodec
import time,docx,requests,os,re

ip = '106.14.223.169:8118'
proxies = {'http': ip}

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

    def __init__(self, func, args):
        super(Mythread, self).__init__()
        self.func = func
        self.args = args

    def run(self):

        text = self.func(self.args)
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
        self.line_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()

        self.pushButton.clicked.connect(self.reveal_thesis)

        self.thread1 = ''
        self.thread2 = ''
        self.thread3 = ''
        self.thread4 = ''
        self.thread5 = ''
        self.thread6 = ''




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    # search按钮
    def reveal_thesis(self):
        keyword = self.lineEdit.text()
        if keyword != '':

            def get_page(keyword):
                url = 'http://www.wenkuxiazai.com/search/%s.html' % keyword
                headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate',
                           'Host': 'www.wenkuxiazai.com',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive',
                           'Referer': 'http://www.wenkuxiazai.com/search/%s.html' % keyword,
                           'Cache-Control': 'max-age=0',
                           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
                #代理IP

                r = requests.get(url, headers=headers,proxies=proxies,timeout=5)
                r.encoding = 'gb2312'
                r.raise_for_status()

                tree = html.fromstring(r.text)
                base = tree.xpath('//div[@class="lista"]')[0]
                lis = []
                for each in base[:6]:
                    title = each.xpath('p[1]/a/@title')
                    if title:
                        href = 'http://www.wenkuxiazai.com' + each.xpath('p[1]/a/@href')[0]
                        summary1 = ''.join(each.xpath('p[2]//text()'))
                        # summary2 = (each.xpath('p[2]'))[0].xpath('string(.)')  #两种方法

                        yield title[0], href, summary1

            lis = list(get_page(keyword))
            index = 2
            for content in lis:
                # self.textBrowser.setText(content)
                order_text = 'self.pushButton_%s.setText(content[0])' % index
                eval(order_text)
                print '1'
                index += 1
            print lis
            self.pushButton_2.clicked.connect(lambda: self.write_thesis(lis[0][1], lis[0][0]))
            self.pushButton_3.clicked.connect(lambda: self.write_thesis(lis[1][1], lis[1][0]))
            self.pushButton_6.clicked.connect(lambda: self.write_thesis(lis[2][1], lis[2][0]))
            self.pushButton_4.clicked.connect(lambda: self.write_thesis(lis[3][1], lis[3][0]))
            self.pushButton_5.clicked.connect(lambda: self.write_thesis(lis[4][1], lis[4][0]))
            print 'over'

    def reveal_textbrowser_result(self,text):
        self.textBrowser.setText(text)
        print 'all done'


    # 获取论文显示页面

    # 写下内容
    def write_thesis(self, url, title):
        self.setFixedSize(1394, 633)
        # 获取具体文章内容
        def get_thesis(href):
            global my_thesis
            my_thesis = []
            headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate',
                       'Host': 'www.wenkuxiazai.com',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}

            def recall(url):
                print url
                r = requests.get(url, headers=headers,proxies=proxies,timeout=5)
                r.encoding = 'gb2312'
                tree = html.fromstring(r.text)
                base = tree.xpath('//div[@id="contents"]')[0]
                my_thesis.append(base.xpath('string(.)'))

                if tree.xpath('//a[@class="next"]/@href'):
                    href = 'http://www.wenkuxiazai.com' + tree.xpath('//a[@class="next"]/@href')[0]
                    return href
                else:
                    return ''

            while True:
                try:
                    href = recall(href)
                except:
                    break

                    # 显示具体论文内容2

        def write_thread(url):
            get_thesis(url)
            text = ''.join(my_thesis)
            print len(text)
            text = re.sub(
                r'((reward([\s\S]*?)gg336x280\(\)\;[\s])|(gg336x280\(\)\;)|reward\(\)\;|(Automatch\(\)\;)|(automatch\(\)\;))',
                '', text)

            my_data = text
            return my_data

            # print os.getcwd() + '\\' + title + '.docx'
            # write_thesis(os.getcwd() + '\\' + title + '.docx', title, my_data)  #写下docx格式论文

        #要改
        my_data = write_thread(url)
        self.textBrowser.append(my_data)

        # if self.thread1 =='':
        #     self.thread1 = Mythread(write_thread, url)  # 多线程连接函数
        #     self.thread1.send_text.connect(self.reveal_textbrowser_result)  # 传递信号
        #     self.thread1.start()  # 开始线程
        #     self.thread1 = ''  #出现多线程错误，重置self.thread ,不知道行不行



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

