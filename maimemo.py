import ipPool
import requests
import random
import datetime

user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0',
               'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36']

# 1月2日  'https://www.maimemo.com/share/page/?uid=1997795&pid=1098'
num = 1098 + (datetime.date(year=datetime.datetime.now().year,month=datetime.datetime.now().month,day=datetime.datetime.now().day) - datetime.date(2018,1,2)).days
maimemo_url = 'https://www.maimemo.com/share/page/?uid=1997795&pid=' + str(num)


headers = {
    'Host':'www.maimemo.com',
    'Content-Type':'text/css',
    'User-Agent':random.choice(user_agents)
}

ip_pool = ipPool.get_ip_pool(2,10)
print(ip_pool)

success = 0
for i in range(len(ip_pool)):
    https =  'https://' + ip_pool[i]
    http = 'http://' + ip_pool[i]
    proxies = {
        "https": https,
        "http": http
    }
    print(proxies)

    try:
        r = requests.post(maimemo_url, proxies= proxies, headers= headers,timeout = 10)
    except:
        print(i)
        print('error')
    else:
        success += 1
        print(i)
        print(r)
print(success)


