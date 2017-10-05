# -*- coding: utf-8 -*-
import requests,time,re
from lxml import html
from translate import zh_en,en_zh

class Write_thesis():
    keyword = '生死学论文'

    #获取论文显示页面
    def get_page(self,keyword):
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



    #获取具体论文内容1
    def get_thesis(self,href):
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

    #显示具体论文内容2
    def write_thesis(self,url):
        self.get_thesis(url)
        text = ''.join(my_thesis)
        print len(text)
        text = re.sub(r'((reward([\s\S]*?)gg336x280\(\)\;[\s])|(gg336x280\(\)\;)|reward\(\)\;)', '', text)

        #print text
        print u'第一步',len(text)
        my_data = zh_en(text)
        print u'第二步',len(text)
        my_data = en_zh(my_data)

        my_data = unicode(my_data, 'unicode_escape')
        print len(my_data),my_data

    #写下论文
    def write(self):
        pass


url = 'http://www.wenkuxiazai.com/doc/0c07aa49ed630b1c58eeb554-1.html'
url = 'http://www.wenkuxiazai.com/doc/53a0fabba417866fb94a8e59.html'
W =Write_thesis()
W.write_thesis(url)
