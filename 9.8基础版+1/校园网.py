import requests
def login():
    url = 'http://222.198.127.170/eportal/success.jsp?userIndex=66323236376132373330346133353834316134623266336262646365663565365f31302e36382e38372e35315f687966383731383437343337&keepaliveInterval=0'

    data = {'keepaliveInterval': '0',
            'userIndex': '66323236376132373330346133353834316134623266336262646365663565365f31302e36382e38372e35315f687966383731383437343337'
            }
    headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate',
               'Host': '222.198.127.170', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive',
               'Cookie': 'EPORTAL_COOKIE_USERNAME=hyf871847437; EPORTAL_COOKIE_PASSWORD=hyf0.0; EPORTAL_COOKIE_SERVER=%E9%BB%98%E8%AE%A4; EPORTAL_COOKIE_SERVER_NAME=%E9%BB%98%E8%AE%A4; EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_COOKIE_DOMAIN=false; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_AUTO_LAND=; JSESSIONID=A187043712583BFA54FC679271A8AF64',
               'Referer': 'http://222.198.127.170/eportal/index.jsp?wlanuserip=00509cd0a7c845612bd7d037a1539c14&wlanacname=d3fd3003b8a92e5a0d9c924efc713c22&ssid=&nasip=f2267a27304a35841a4b2f3bbdcef5e6&snmpagentip=&mac=3b3191d90aa2a6cf80e6c65cf1ce3546&t=wireless-v2&url=909cf2a364dbf8f1e455f8fe270d17a0d1f581c8c5d0effda0ff26aea941f4f2&apmac=&nasid=d3fd3003b8a92e5a0d9c924efc713c22&vid=e84027679edac0b6&port=d230193a77509583&nasportid=136985ff42ef1c4528a45c84a073ddb88116087e26906b6db276baa65fee971a5335918f48bcf75a',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}

    r = requests.get(url, headers=headers, data=data)
    r.encoding = 'gbk'
    print r.text

url1 = u'http://222.198.127.170/eportal/InterFace.do?method=login'
headers = {'Content-Length': '672', 'Accept-Encoding': 'gzip, deflate', '(Request-Line)': 'POST /eportal/InterFace.do?method=login HTTP/1.1', 'Accept-Languagez': 'h-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0', 'Host': '222.198.127.170', 'Referer': u'http://222.198.127.170/eportal/index.jsp?wlanuserip=00509cd0a7c845612bd7d037a1539c14&wlanacname=d3fd3003b8a92e5a0d9c924efc713c22&ssid=&nasip=f2267a27304a35841a4b2f3bbdcef5e6&snmpagentip=&mac=3b3191d90aa2a6cf80e6c65cf1ce3546&t=wireless-v2&url=909cf2a364dbf8f1e455f8fe270d17a0d1f581c8c5d0effda0ff26aea941f4f2&apmac=&nasid=d3fd3003b8a92e5a0d9c924efc713c22&vid=e84027679edac0b6&port=d230193a77509583&nasportid=136985ff42ef1c4528a45c84a073ddb88116087e26906b6db276baa65fee971a5335918f48bcf75a', 'Cookie': 'EPORTAL_COOKIE_USERNAME=hyf871847437; EPORTAL_COOKIE_PASSWORD=hyf0.0; EPORTAL_COOKIE_SERVER=%E9%BB%98%E8%AE%A4; EPORTAL_COOKIE_SERVER_NAME=%E9%BB%98%E8%AE%A4; EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_COOKIE_DOMAIN=false; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_AUTO_LAND=; JSESSIONID=A187043712583BFA54FC679271A8AF64', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
data = {'queryString': u'wlanuserip%3D00509cd0a7c845612bd7d037a1539c14%26wlanacname%3Dd3fd3003b8a92e5a0d9c924efc713c22%26ssid%3D%26nasip%3Df2267a27304a35841a4b2f3bbdcef5e6%26snmpagentip%3D%26mac%3D3b3191d90aa2a6cf80e6c65cf1ce3546%26t%3Dwireless-v2%26url%3D909cf2a364dbf8f1e455f8fe270d17a0d1f581c8c5d0effda0ff26aea941f4f2%26apmac%3D%26nasid%3Dd3fd3003b8a92e5a0d9c924efc713c22%26vid%3De84027679edac0b6%26port%3Dd230193a77509583%26nasportid%3D136985ff42ef1c4528a45c84a073ddb88116087e26906b6db276baa65fee971a5335918f48bcf75a', 'password': 'hyf0.0', 'userId': 'hyf871847437', 'service': '%E9%BB%98%E8%AE%A4'}
params = {'method':'login'}

r =requests.post(url=url1,headers=headers,data=data,params=params)
print r.text
#login()











