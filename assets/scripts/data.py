import requests  #用于向网站发送请求
from lxml import etree    #lxml为第三方网页解析库，强大且速度快

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
}
response = requests.get(url, headers=headers, timeout=10)

html = response.text

parse = etree.HTML(html)  #解析网页
# 获取所有 li 元素
items = parse.xpath('//*[@id="hotsearch-content-wrapper"]/li')

# 初始化结果列表
data = []

# 遍历每个 li，提取标题和链接
for item in items:
    title = item.xpath('.//a//span[@class="title-content-title"]/text()')[0]  # 获取标题
    link = item.xpath('.//a/@href')[0]  # 获取链接

    # 将标题和链接存入字典并添加到结果列表中
    data.append({"title": title, "link": link})

# 打印结果
print(data)