# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'look_up_thesis.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from write_thesis import write_thesis
from translate import en_zh,zh_en
from PyQt4.QtCore import pyqtSignature,QStringList,Qt,pyqtSignal,QThread,QTextCodec
from PyQt4.QtGui import QMessageBox
from lxml import html
import time,docx,requests,os,re

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


class Ui_Form_Look_Up(QtGui.QWidget):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(542, 706)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 241, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 261, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_1 = QtGui.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(370, 40, 93, 28))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 190, 93, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textBrowser_3 = QtGui.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 340, 521, 81))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 670, 93, 28))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.textBrowser_5 = QtGui.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(10, 580, 521, 81))
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 310, 93, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 550, 93, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.textBrowser_2 = QtGui.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 220, 521, 81))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_1 = QtGui.QTextBrowser(Form)
        self.textBrowser_1.setGeometry(QtCore.QRect(10, 100, 521, 81))
        self.textBrowser_1.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 430, 93, 28))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.textBrowser_4 = QtGui.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 460, 521, 81))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.textBrowser_6 = QtGui.QTextBrowser(Form)
        self.textBrowser_6.setGeometry(QtCore.QRect(550, -1, 561, 721))
        self.textBrowser_6.setLineWidth(0)
        self.textBrowser_6.setMidLineWidth(0)
        self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(530, 0, 20, 721))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(-5, 0, 20, 701))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))


        self.pushButton_1.clicked.connect(self.reveal_thesis)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #search按钮
    def reveal_thesis(self):
        keyword = self.lineEdit.text()
        if keyword != '':
            self.setFixedSize(542, 706)
            def get_page(keyword):
                url = 'http://www.wenkuxiazai.com/search/%s.html' % keyword
                headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate',
                           'Host': 'www.wenkuxiazai.com',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive',
                           'Referer': 'http://www.wenkuxiazai.com/search/%s.html' % keyword,
                           'Cache-Control': 'max-age=0',
                           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
                r = requests.get(url, headers=headers)
                r.encoding = 'gb2312'
                r.raise_for_status()

                tree = html.fromstring(r.text)
                base = tree.xpath('//div[@class="lista"]')[0]
                lis = []
                for each in base[:5]:
                    title = each.xpath('p[1]/a/@title')
                    if title:
                        href = 'http://www.wenkuxiazai.com' + each.xpath('p[1]/a/@href')[0]
                        summary1 = ''.join(each.xpath('p[2]//text()'))
                        # summary2 = (each.xpath('p[2]'))[0].xpath('string(.)')  #两种方法

                        yield title[0], href, summary1

            lis = list(get_page(keyword))
            index = 1
            for content in lis:
                # self.textBrowser.setText(content)
                order_text = 'self.textBrowser_%s.setText(content[2])' % index
                eval(order_text)
                print '1'
                index += 1
            self.pushButton_2.clicked.connect(lambda: self.write_thesis(lis[0][1], lis[0][0]))
            self.pushButton_3.clicked.connect(lambda: self.write_thesis(lis[1][1], lis[1][0]))
            self.pushButton_6.clicked.connect(lambda: self.write_thesis(lis[2][1], lis[2][0]))
            self.pushButton_4.clicked.connect(lambda: self.write_thesis(lis[3][1], lis[3][0]))
            self.pushButton_5.clicked.connect(lambda: self.write_thesis(lis[4][1], lis[4][0]))
            print 'over'

            # 获取论文显示页面



    #获取主页面。返回标题。连接，摘要
    def get_page(self, keyword):
        url = 'http://www.wenkuxiazai.com/search/%s.html' % keyword
        headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate',
                   'Host': 'www.wenkuxiazai.com',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive',
                   'Referer': 'http://www.wenkuxiazai.com/search/%s.html' % keyword, 'Cache-Control': 'max-age=0',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
        r = requests.get(url, headers=headers)
        r.encoding = 'gb2312'
        r.raise_for_status()

        tree = html.fromstring(r.text)
        base = tree.xpath('//div[@class="lista"]')[0]
        lis = []
        for each in base:
            title = each.xpath('p[1]/a/@title')
            if title:
                href = 'http://www.wenkuxiazai.com' + each.xpath('p[1]/a/@href')[0]
                summary1 = ''.join(each.xpath('p[2]//text()'))
                # summary2 = (each.xpath('p[2]'))[0].xpath('string(.)')  #两种方法

                yield title[0], href, summary1


        # 获取具体论文内容1
    #获取具体文章内容
    def get_thesis(self, href):
        global my_thesis
        my_thesis = []
        headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate',
                   'Host': 'www.wenkuxiazai.com',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}

        def recall(url):
            print url
            r = requests.get(url, headers=headers)
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
    #写下内容
    def write_thesis(self, url, title):
        self.setFixedSize(1112, 706)
        self.get_thesis(url)
        text = ''.join(my_thesis)
        print len(text)
        text = re.sub(r'((reward([\s\S]*?)gg336x280\(\)\;[\s])|(gg336x280\(\)\;)|reward\(\)\;|(Automatch\(\)\;)|(automatch\(\)\;))', '',text)


        my_data=text
        self.textBrowser_6.setText(my_data)
        print 'all done'

        #print os.getcwd() + '\\' + title + '.docx'
        #write_thesis(os.getcwd() + '\\' + title + '.docx', title, my_data)  #写下docx格式论文




    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        #self.label.setText(_translate("Form", "输入", None))
        self.pushButton_1.setText(_translate("Form", "搜索", None))
        self.pushButton_2.setText(_translate("Form", "查看论文", None))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_5.setText(_translate("Form", "查看论文", None))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_3.setText(_translate("Form", "查看论文", None))
        self.pushButton_4.setText(_translate("Form", "查看论文", None))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_6.setText(_translate("Form", "查看论文", None))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

