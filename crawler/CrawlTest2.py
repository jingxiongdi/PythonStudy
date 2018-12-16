# coding=utf-8
from bs4 import BeautifulSoup
import requests

import xlwt
import xlrd

#爬取平安夜短信祝福语
excelTabel= xlwt.Workbook()#创建excel对象
sheet1=excelTabel.add_sheet('平安夜祝福语')
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
#excelTabel.save("祝福语.xls")


#爬取元旦祝福部分
sheet1=excelTabel.add_sheet('元旦祝福语')
nrows = 0
url=""
for num in range(1,8):
    if num==1:
        url = "http://www.hengexing.com/z/80863.html"
    else:
        url="http://www.hengexing.com/z/80863_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")


#爬取圣诞节部分代码：
sheet1=excelTabel.add_sheet('圣诞祝福语')
nrows = 0
url=""
for num in range(1,11):
    if num==1:
        url = "http://www.hengexing.com/z/80852.html"
    else:
        url="http://www.hengexing.com/z/80852_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")


#爬取春节部分代码:
sheet1=excelTabel.add_sheet('春节祝福语')
nrows = 0
url=""
for num in range(1,31):
    if num==1:
        url = "http://www.hengexing.com/z/80814.html"
    else:
        url="http://www.hengexing.com/z/80814_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")


#爬取元宵节祝福语
sheet1=excelTabel.add_sheet('元宵节祝福语')
nrows = 0
url=""
for num in range(1,14):
    if num==1:
        url = "http://www.hengexing.com/z/80864.html"
    else:
        url="http://www.hengexing.com/z/80864_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")


#爬取除夕节祝福语
sheet1=excelTabel.add_sheet('除夕节祝福语')
nrows = 0
url=""
for num in range(1,6):
    if num==1:
        url = "http://www.hengexing.com/z/80811.html"
    else:
        url="http://www.hengexing.com/z/80811_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")

#爬取父亲节祝福语
sheet1=excelTabel.add_sheet('父亲节祝福语')
nrows = 0
url=""
for num in range(1,10):
    if num==1:
        url = "http://www.hengexing.com/z/80821.html"
    else:
        url="http://www.hengexing.com/z/80821_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")


#爬取母亲节祝福语
sheet1=excelTabel.add_sheet('母亲节祝福语')
nrows = 0
url=""
for num in range(1,9):
    if num==1:
        url = "http://www.hengexing.com/z/80843.html"
    else:
        url="http://www.hengexing.com/z/80843_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")



#爬取七夕节祝福语
sheet1=excelTabel.add_sheet('七夕祝福语')
nrows = 0
url=""
for num in range(1,22):
    if num==1:
        url = "http://www.hengexing.com/z/80845.html"
    else:
        url="http://www.hengexing.com/z/80845_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")


#爬取结婚祝福语
sheet1=excelTabel.add_sheet('结婚祝福语')
nrows = 0
url=""
for num in range(1,8):
    if num==1:
        url = "http://www.hengexing.com/z/80833.html"
    else:
        url="http://www.hengexing.com/z/80833_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")



#爬取端午祝福语
sheet1=excelTabel.add_sheet('端午祝福语')
nrows = 0
url=""
for num in range(1,13):
    if num==1:
        url = "http://www.hengexing.com/z/80819.html"
    else:
        url="http://www.hengexing.com/z/80819_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")


#爬取开业祝福语
sheet1=excelTabel.add_sheet('开业祝福语')
nrows = 0
url=""
for num in range(1,9):
    if num==1:
        url = "http://www.hengexing.com/z/80868.html"
    else:
        url="http://www.hengexing.com/z/80868_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")


#爬取乔迁祝福语
sheet1=excelTabel.add_sheet('乔迁祝福语')
nrows = 0
url=""
for num in range(1,3):
    if num==1:
        url = "http://www.hengexing.com/z/80869.html"
    else:
        url="http://www.hengexing.com/z/80869_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")


#爬取喜得贵子祝福语
sheet1=excelTabel.add_sheet('喜得贵子祝福语')
nrows = 0
url=""
for num in range(1,5):
    if num==1:
        url = "http://www.hengexing.com/z/80871.html"
    else:
        url="http://www.hengexing.com/z/80871_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语.xls")


#爬取满月祝福语
sheet1=excelTabel.add_sheet('满月祝福语')
nrows = 0
url=""
for num in range(1,3):
    if num==1:
        url = "http://www.hengexing.com/z/80879.html"
    else:
        url="http://www.hengexing.com/z/80879_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
#excelTabel.save("祝福语大全.xls")


#爬取中秋祝福语
sheet1=excelTabel.add_sheet('中秋祝福语')
nrows = 0
url=""
for num in range(1,18):
    if num==1:
        url = "http://www.hengexing.com/z/80866.html"
    else:
        url="http://www.hengexing.com/z/80866_%d.html" %num
    r = requests.get(url)
    #这里和网页的编码设置相关
    r.encoding = 'gb2312'#解决乱码问题
    soup = BeautifulSoup(r.text, 'html.parser')
    listAA = soup.find_all("p")

    for text in listAA:
        print(text.getText())
        sheet1.write(nrows,0,text.getText())
        nrows+=1
excelTabel.save("祝福语大全.xls")