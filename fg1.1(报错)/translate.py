# -*- coding: utf-8 -*-
import requests

def cut(lis):
    my_str = ''
    for paragraph in lis:
        if len(my_str) < 1000:
            my_str = my_str + paragraph + '\n'
        else:
            my_str = my_str + paragraph + '\n'
            a = my_str
            my_str = ''
            yield a
    yield my_str



def zh_en(text):   #####中文翻译为英文
    lis = text.split('\n')
    my_translate = ''
    count = 0
    for content in cut(lis):
        try:
            url = 'http://fy.iciba.com/ajax.php?a=fy'
            data = {'f': 'zh',
                    't': 'en',
                    'w': content
                    }
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
            r = requests.post(url, data=data, headers=headers)
            null = false =''
            dic = eval(r.text)
            try:
                my_translate += dic['content']['out'] + '\n'
            except:
                my_translate += dic['content']['word_mean'][0] + '\n'
            count += 1
       #     process = '{:.2f}%'.format(count * 50 / len(lis))  # 清除按钮
        except Exception, e:
            print e
    return my_translate.replace('<br\/>', '\n')


def en_zh(text):  #####英文翻译为中文

    lis = text.split('\n')
    my_translate = ''
    count = 0
    for content in cut(lis):
        try:
            url = 'http://fy.iciba.com/ajax.php?a=fy'
            data = {'f': 'en',
                    't': 'zh',
                    'w': content
                    }
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
            r = requests.post(url, data=data, headers=headers)
            r.encoding = 'utf8'
            null = false = ''
            dic = eval(r.text)
            try:
                my_translate += dic['content']['out'] + '\n'*2
            except:
                my_translate += dic['content']['word_mean'][0].split(';')[0].split('.')[-1] + '\n'*2
            count += 1
        #    process = '{:.2f}%'.format(count * 50 / len(lis) + 50)  # 清除按钮
        except Exception, e:
            print e
    return my_translate.replace('<br\/>', '\n'*2)
