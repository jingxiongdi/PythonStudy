#coding=gbk
'''
��ȡ�黰��վ  http://www.duanmeiwen.com/yulu/aiqing/8174.html
'''
from bs4 import BeautifulSoup
import requests

url="http://www.duanmeiwen.com/yulu/aiqing/8174.html"
r = requests.get(url)
#�������ҳ�ı����������
r.encoding = 'gbk'#�����������
soup = BeautifulSoup(r.text, 'html.parser')
listAA = soup.find_all("p")
print("num ",len(listAA))
txtName = "love1.txt"
f = open(txtName, 'a+')
loveContent = ""
for i in range(0,len(listAA)-1):
    print(listAA[i].text)
    loveContent +=listAA[i].text
loveContent = loveContent.replace('\ufffd','')#�滻��������GBK������ַ�
f.write(loveContent)
f.close()
print("��ȡ�黰�ɹ�==========================")


