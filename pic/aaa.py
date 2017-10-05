# -*- coding: utf-8 -*-
import requests,threading
from bs4 import BeautifulSoup
from threading import Thread

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}
#result_ip = open('verify_ip.txt', 'w')


#定义获取IP函数
def get_ip():
   #写入txt
    write_ip = open('get_ip.txt', 'w')
    for page in range(1, 10):
        url = 'http://www.xicidaili.com/nn/%s' % page
        r = requests.get(url, headers=headers,timeout=5)

        # 用beautifulsoup库解析网页
        soup = BeautifulSoup(r.content, 'lxml')
        trs = soup.find('table', id='ip_list').find_all('tr')

        for tr in trs[1:]:
            tds = tr.find_all('td')
            ip = tds[1].text.strip()
            port = tds[2].text.strip()

            write_ip.write('%s\n'%(ip+':'+port))
    write_ip.close()
    print('done')



get_ips = open('get_ip.txt','r')
lock = threading.Lock() #使用线程锁

#利用多线程，在新浪IP接口上，验证IP
def verify_ip():

    url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js'  # 新浪IP接口
    try:
        # 先要获取锁:
        lock.acquire()
        ip = get_ips.readline().strip()
        #解开锁
        lock.release()

        proxies = {'http': ip}

        r = requests.get(url, headers=headers, proxies=proxies,timeout=3)
       #如果requests成功，表示验证成功，打印出IP
        print ip
    except:
        pass


thread_all = []
for i in range(100):

    t = Thread(target=verify_ip)
    thread_all.append(t)
    t.start()

for t in thread_all:
    t.join()

get_ip.close()