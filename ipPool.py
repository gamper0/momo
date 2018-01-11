from bs4 import BeautifulSoup
import requests
import time
import multiprocessing
import telnetlib

#返回[[ip,port],[ip,port]...]，测试用
def ip_ports(n,total_page_num):
    ips = []
    ports = []
    # [[ip,port],[ip,port]...]测试用
    ip_port_lists = []
    ip_page_num = 0

    while ip_page_num < total_page_num:
        ip_page_num += 1
        # stype=2是https ip，stype=1是http ip   'http://www.nianshao.me/?stype=1&page=2'
        ip_url = 'http://www.nianshao.me/?stype=' + str(n) + '&page=' + str(ip_page_num)
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        r = requests.post(ip_url, headers=headers)
        print(r)

        soup = BeautifulSoup(r.text, "html.parser")

        #ip list
        ip_items = soup.select('td[style="WIDTH:110PX"]')
        # print('ip_items:{}'.format(ip_items))
        for ip_item in ip_items:
            ips.append(ip_item.get_text())
        print('ips:{}'.format(ips))

        # port list
        port_items = soup.select('td[style="WIDTH:40PX"]')
        # print('port_items:{}'.format(port_items))
        for port_item in port_items:
            ports.append(port_item.get_text())
        print('port:{}'.format(ports))

        time.sleep(3)

    # 获得[[ip,port],[ip,port]...]，测试用
    for i in range(len(ips)):
        ip = ips[i]
        port = ports[i]
        ip_port_list = [ip, port]
        ip_port_lists.append(ip_port_list)

    return ip_port_lists

#测试ip能不能用（单个）
def test_ip_pool(ip_port_list):
    try:
        telnetlib.Telnet(ip_port_list[0],port= ip_port_list[1],timeout= 4)
    except:
        print('connect failed')
    else:
        print('succes')
        ip_port = ip_port_list[0]+ ':' + ip_port_list[1]
        return  ip_port

#多进程运行test_ip_pool
def get_ip_pool(n,total_page_num):
    ip_port_lists = ip_ports(n,total_page_num)

    pool = multiprocessing.Pool()
    result = pool.map(test_ip_pool, ip_port_lists)
    pool.close()
    pool.join()

    ip_pool = [i for i in result if i is not None]
    return ip_pool

