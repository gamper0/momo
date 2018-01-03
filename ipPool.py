from bs4 import BeautifulSoup
import requests
import time
import telnetlib

#n=1为http，n=2为https
def get_ip_pool(n,total_page_num):

    ip_port_pool = []
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

        time.sleep(6)

    # 获得[[ip,port],[ip,port]...]，测试用
    for i in range(len(ips)):
        ip_port_list = []
        ip = ips[i]
        port = ports[i]
        ip_port_list = [ip, port]
        ip_port_lists.append(ip_port_list)


    # 测试ip是否可用,并将可用的添加到ip池
    for i in range(len(ip_port_lists)):
        try:
            telnetlib.Telnet(ip_port_lists[i][0], port=ip_port_lists[i][1], timeout=5)
        except:
            print(str(i) + '  connect failed')
        else:
            print(str(i) + '  success')
            ip_port_pool.append(ip_port_lists[i][0] + ':' + ip_port_lists[i][1])

    return ip_port_pool







# ip = Ip()
# ip_port_pool = ip.get_ip_pool(2)
# print(ip_port_pool)

