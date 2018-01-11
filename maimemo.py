import ipPool
import requests
import random
import datetime
import multiprocessing



def start(ip):
    # 1月2日  'https://www.maimemo.com/share/page/?uid=1997795&pid=1098'
    now = datetime.datetime.now()
    num = 1098 + (datetime.date(year=now.year, month=now.month, day=now.day) - datetime.date(2018, 1, 2)).days
    maimemo_url = 'https://www.maimemo.com/share/page/?uid=1997795&pid=' + str(num)

    user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0',
                   'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36']
    headers = {
        'Host':'www.maimemo.com',
        'Content-Type':'text/css',
        'User-Agent':random.choice(user_agents)
    }
    proxies = {
        "https": 'https://' + ip,
        "http": 'http://' + ip
    }

    try:
        r = requests.post(maimemo_url, proxies=proxies, headers=headers, timeout=10)
    except:
        print('error')
    else:
        print(r)
        return r




if __name__ == '__main__':
    #为了让pyinstaller转成exe可运行
    multiprocessing.freeze_support()
    #获得代理ip池
    ip_pool = ipPool.get_ip_pool(2,15)
    #多进程运行
    pool = multiprocessing.Pool()
    result = pool.map(start,ip_pool)
    pool.close()
    pool.join()

    success = [i for i in result if i is not None]
    print(len(success))

    print('done')





