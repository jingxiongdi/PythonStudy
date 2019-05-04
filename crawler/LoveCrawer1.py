#coding=gbk
'''
爬取情话网站  http://www.duanmeiwen.com/yulu/aiqing/8174.html
'''
from bs4 import BeautifulSoup
import requests

url="http://www.duanmeiwen.com/yulu/aiqing/8174.html"
r = requests.get(url)
#这里和网页的编码设置相关
r.encoding = 'gbk'#解决乱码问题
soup = BeautifulSoup(r.text, 'html.parser')
listAA = soup.find_all("p")
print("num ",len(listAA))
txtName = "love1.txt"
f = open(txtName, 'a+')
loveContent = ""
for i in range(0,len(listAA)-1):
    print(listAA[i].text)
    loveContent +=listAA[i].text
loveContent = loveContent.replace('\ufffd','')#替换掉不属于GBK编码的字符
f.write(loveContent)
f.close()
print("爬取情话成功==========================")


