# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decrease.ui'
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
import time,docx,requests,os,threading


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


# 从文档中读取论文
def read_docx(filename):
    doc = docx.Document(filename)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)

class Mythread(QtCore.QThread):  #创建多线程
    send_text = pyqtSignal(str)

    def __init__(self, func, args):
        super(Mythread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        text = self.func(self.args)
        self.send_text.emit(text)

class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(602, 164)
        Dialog.move(520,200)
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
        #self.lineEdit.setStyleSheet(_fromUtf8("color: rgb(216, 216, 216);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 110, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(570, 0, 31, 31))
        self.commandLinkButton.setText(_fromUtf8(""))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(110, 50, 115, 19))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 50, 115, 19))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 110, 93, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}"
                                      "QPushButton:hover{background-color:#333333;}"))  #####
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setGeometry(QtCore.QRect(10, 90, 581, 561))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 660, 93, 31))
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}"
                                      "QPushButton:hover{background-color:#333333;}"))  #####
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.textBrowser_2 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(600, -5, 581, 711))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser.raise_()
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 670, 201, 16))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.radioButton.setChecked(True)
        self.textBrowser.setVisible(False)
        self.append_flag=1

        self.my_str = ''
        self.my_rate = []

    #传递信号
    def reveal_result(self,result):
        self.textBrowser_2.setText(result)
        self.label_3.setText(u'查重完成')

    #第一个查重函数，生成结果，发送信号
    def rate_thesis(self):
        def cut3(lis):
            my_str = ''
            for i in range(len(lis)):
                if len(my_str) < 2000:
                    my_str = my_str + lis[i] + '\n'
                else:
                    my_str = my_str + lis[i] + '\n'
                    a = my_str
                    my_str = ''
                    yield a
            yield my_str

        def look_up(my_file_path):

            if my_file_path[-4:] == '.txt':  # 读取TXT文档
                with open(unicode(my_file_path)) as f:
                    my_data = f.read().decode('gbk')

            elif my_file_path[-4:] == '.doc' or 'docx':  # 使用函数读取doc文档
                my_data = read_docx(unicode(my_file_path).replace('/', '\\'))
            else:
                QMessageBox.Information(self, 'wrong', u'不支持的文件格式')
                return u'查重失败，不支持的文件格式'
            #开始查重
            lis = my_data.split('\n')
            thread_all =[]
            # 未加cookie
            headers = {'Content-Length': '20381', 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                       'Accept-Encoding': 'gzip, deflate', 'Host': '120.77.147.232',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive',
                       'Referer': 'http://120.77.147.232/paper2.html',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.',
                       'Content-Type': 'application/x-www-form-urlencoded'}
            url = 'http://120.77.147.232/Search'

            def start_url():
                r = requests.post(url, data=data)
                tree = html.fromstring(r.text)
                bases = tree.xpath('/html/body/div[2]/ol[1]/li')
                if bases:
                    for each in bases:
                        txt = each.xpath('div/h2/a[1]/text()')
                        rate = each.xpath('div/h2/strong/text()')
                        if float(rate[0][:-1]) > 1.9:
                            self.my_rate.append(rate[0][:-1])
                        self.my_str += unicode(txt[0]) + '-----' + unicode(rate[0]) + '\n' * 2

            for text in cut3(lis):
                data = {'txa': text, 'title': 'aaa'}
                t = threading.Thread(target=start_url)
                thread_all.append(t)
                t.start()

            for t in thread_all:
                t.join()

            def add_rate(m, n):
                return float(m) + float(n)

            def add_number(lis):
                number = 0
                for i in lis:
                    if float(i) > 10:
                        number += float(i) / 10
                return number

            a = '%.2f' % (float(reduce(add_rate,self.my_rate)) / len(self.my_rate) + add_number(self.my_rate)) + '%'
            return self.my_str + u'查重率:' + a
            #self.textBrowser_2.setText(self.my_str + u'查重率:' + a)
        #look_up(self.lineEdit.text())

        self.my_rate = []
        self.my_str = ''
        if os.path.isfile(self.lineEdit.text()):
            self.thread1 = Mythread(look_up, u'%s' % self.lineEdit.text())  # 多线程连接函数
            self.thread1.send_text.connect(self.reveal_result)  # 传递信号
            self.thread1.start()  # 开始线程
            ok = QMessageBox.information(self, u'查重', u'喝杯茶\n休息一下...', u'ok')
        else:
            ok = QMessageBox.information(self, u'告知', u'请选择正确的文档文件', u'ok')
            self.label_3.setText('')



    # 第二个查重函数，生成结果，发送信号
    def rate_thesis_2(self):

        def cut3(lis):
            my_str = ''
            for i in range(len(lis)):
                if len(my_str) < 2000:
                    my_str = my_str + lis[i] + '\n'
                else:
                    my_str = my_str + lis[i] + '\n'
                    a = my_str
                    my_str = ''
                    yield a
            yield my_str

        def look_up(my_data):

            # 开始查重
            lis = my_data.split('\n')
            thread_all = []
            # 未加cookie
            headers = {'Content-Length': '20381', 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                       'Accept-Encoding': 'gzip, deflate', 'Host': '120.77.147.232',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive',
                       'Referer': 'http://120.77.147.232/paper2.html',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.',
                       'Content-Type': 'application/x-www-form-urlencoded'}
            url = 'http://120.77.147.232/Search'

            def start_url():
                r = requests.post(url, data=data)
                tree = html.fromstring(r.text)
                bases = tree.xpath('/html/body/div[2]/ol[1]/li')
                if bases:
                    for each in bases:
                        txt = each.xpath('div/h2/a[1]/text()')
                        rate = each.xpath('div/h2/strong/text()')
                        if float(rate[0][:-1]) > 1.9:
                            self.my_rate.append(rate[0][:-1])
                        self.my_str += unicode(txt[0]) + '-----' + unicode(rate[0]) + '\n' * 2

            for text in cut3(lis):
                data = {'txa': text, 'title': 'aaa'}
                t = threading.Thread(target=start_url)
                thread_all.append(t)
                t.start()

            for t in thread_all:
                t.join()

            def add_rate(m, n):
                return float(m) + float(n)

            def add_number(lis):
                number = 0
                for i in lis:
                    if float(i) > 10:
                        number += float(i) / 10
                return number

            a = '%.2f' % (float(reduce(add_rate, self.my_rate)) / len(self.my_rate) + add_number(self.my_rate)) + '%'
            return self.my_str + u'查重率:' + a

        self.my_rate = []
        self.my_str = ''
        if self.textBrowser.toPlainText() != '':
            self.thread1 = Mythread(look_up, u'%s' % self.textBrowser.toPlainText())  # 多线程连接函数
            self.thread1.send_text.connect(self.reveal_result)  # 传递信号
            self.thread1.start()  # 开始线程
            ok = QMessageBox.information(self, u'查重', u'喝杯茶\n休息一下...', u'ok')
        else:
            ok = QMessageBox.information(self, u'告知', u'请输入文字', u'ok')
            self.label_3.setText('')


    #扩展按钮
    @pyqtSignature('')
    def on_commandLinkButton_clicked(self):
        if self.append_flag ==1:
            self.setFixedSize(1182,701)
            self.append_flag = 0
        else:
            self.setFixedSize(602, 701)
            self.append_flag = 1

    #选择文件
    @pyqtSignature('')
    def on_radioButton_clicked(self):
        self.pushButton_3.setVisible(False)
        self.textBrowser.setVisible(False)
        self.pushButton.setVisible(True)
        self.lineEdit.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.setFixedSize(602, 164)
    #文字粘贴
    @pyqtSignature('')
    def on_radioButton_2_clicked(self):
        self.pushButton_3.setVisible(True)
        self.textBrowser.setVisible(True)
        self.pushButton.setVisible(False)
        self.lineEdit.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.setFixedSize(602, 701)

    #选择文件按钮
    @pyqtSignature('')
    def on_pushButton_clicked(self):
        my_file_path = QtGui.QFileDialog.getOpenFileName(self, u'打开文件', '/', "Files(*.docx);;Files(*.doc);;Files(*.txt)")
        self.lineEdit.setText(unicode(my_file_path))

    # 第一个搜索
    @pyqtSignature('')
    def on_pushButton_2_clicked(self):
        self.label_3.setText(u'正在努力，请稍等...')
        self.setFixedSize(1182,701)
        self.rate_thesis()

    # 第二个搜索
    @pyqtSignature('')
    def on_pushButton_3_clicked(self):
        self.label_3.setText(u'正在努力，请稍等...')
        self.setFixedSize(1182, 701)
        self.rate_thesis_2()



    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lineEdit.setText(_translate("Dialog", "未选择文件", None))
        self.pushButton.setText(_translate("Dialog", "选择文件", None))
        self.label.setText(_translate("Dialog", "上传方式：", None))
        self.radioButton.setText(_translate("Dialog", "文件上传", None))
        self.radioButton_2.setText(_translate("Dialog", "文字粘贴", None))
        self.pushButton_2.setText(_translate("Dialog", "查重", None))
        self.pushButton_3.setText(_translate("Dialog", "查重", None))
        self.label_3.setText(_translate("Dialog", "", None))



