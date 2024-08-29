import csv  #用于把爬取的数据存储为csv格式，可以excel直接打开的
import time  #用于对请求加延时，爬取速度太快容易被反爬
from time import sleep #同上
import random  #用于对延时设置随机数，尽量模拟人的行为
import requests  #用于向网站发送请求
from lxml import etree    #lxml为第三方网页解析库，强大且速度快

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
}
response = requests.get(url, headers=headers, timeout=10)
html = response.text
parse = etree.HTML(html)  #解析网页
all_tr = parse.xpath('//*[@id="hotsearch_data"]')
print(all_tr)