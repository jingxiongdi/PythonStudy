# coding=utf-8
from bs4 import BeautifulSoup
import requests

import xlwt

#爬取一些短信祝福语
excelTabel= xlwt.Workbook()#创建excel对象
sheet1=excelTabel.add_sheet('平安夜短信祝福语')
nrows = 0
url=""
for num in range(1,6):
    if num==1:
        url = "http://www.hengexing.com/z/80844.html"
    else:
        url="http://www.hengexing.com/z/80844_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
excelTabel.save("平安夜祝福语.xls")


