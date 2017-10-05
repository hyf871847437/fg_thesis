# -*- coding: utf-8 -*-
import requests
url = 'http://www.cnblogs.com/fg2312/p/7489201.html'
headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate', 'If-Modified-Since': 'Fri, 08 Sep 2017 14:02:48 GMT',
           'Host': 'www.cnblogs.com', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}

proxies = {'http': '61.135.217.7:80'}

r = requests.get(url,headers=headers,proxies=proxies,timeout=5)
print r.text