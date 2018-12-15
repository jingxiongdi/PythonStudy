# coding=utf-8
import requests
import urllib.request
from bs4 import BeautifulSoup

#官方文档 requests beautifulsoup
#http://beautifulsoup.readthedocs.io/zh_CN/latest/
#http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

#爬取整个网页源码urllib
#url = "http://www.baidu.com"
#page_info = urllib.request.urlopen(url).read()
#page_info = page_info.decode('utf-8')
#print(page_info)

#requests
url= "http://www.runoob.com/python3/"
r = requests.get("http://www.runoob.com/python3/python3-tutorial.html")
r.encoding = 'gbk2312'#解决乱码问题
#r = requests.post('http://httpbin.org/post', data = {'key':'value'})

#传参
#payload = {'key1': 'value1', 'key2': 'value2'}
#r = requests.get("http://httpbin.org/get", params=payload)
#print(r.text)#读取服务器响应

#使用BeautifulSoup解析这段代码,能够得到一个 BeautifulSoup 的对象,
# 并能按照标准的缩进格式的结构输出:
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())
#print(soup.title)

#从文档中获取所有的文字内容
#print(soup.get_text())
#

#爬取python菜鸟教程标题部分
# listTile = soup.find_all(target="_top");
# allTitle = "";
# for text in listTile:
#     allTitle = allTitle+text.text+"\n"
# with open("baidu.txt","w",encoding='utf-8') as f:
#     f.write(allTitle)

# listTile = soup.find_all(target="_top")
# for text in listTile:
#      print(url+text.get('href'))



#抓取python3简介
# discription = soup.find_all("meta")
# for text in discription:
#     if text.get('name')=="description":
#         print(text.get('content'))

