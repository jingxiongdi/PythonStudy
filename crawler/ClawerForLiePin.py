'''
爬取猎聘网职位信息做数据分析
'''
from bs4 import BeautifulSoup
import requests
import time
import pymongo

'''
保存数据库方法:
'''
def saveToDB(json):
    print("正在保存到数据库")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.LiePinData
    data = db.android
    data.insert_one(json)



'''
爬取主程序
'''
nextUrlBase = "https://www.liepin.com/zhaopin/?init=-1&headckid=870b81c75324cfd6&fromSearchBtn=2&sfrom=click-pc_homepage-centre_searchbox-search_new&ckid=870b81c75324cfd6&degradeFlag=0&key=android&siTag=wxsyNkzhnKj80VCkF-zOWA~fA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId=2e3b9060a66797f918418a1a6256318f&d_curPage=0&d_pageSize=40&d_headId=2e3b9060a66797f918418a1a6256318f&curPage=15"
page = 0
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url="https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key=android"
r = requests.get(url,headers)
#这里和网页的编码设置相关
r.encoding = 'utf-8'#解决乱码问题
soup = BeautifulSoup(r.text, 'html.parser')
jobList = soup.find_all('div','sojob-item-main clearfix')
print("一页数量 ：",len(jobList))
for pageNum in range(0,100):
    time.sleep(1)#休眠1秒
    print("------page-----",pageNum,page)
    if page>0:
        url=nextUrlBase+str(page)
        print("开始爬取 : "+url)
        r = requests.get(url,headers)
        r.encoding = 'utf-8'#解决乱码问题
        soup = BeautifulSoup(r.text, 'html.parser')
        jobList = soup.find_all('div','sojob-item-main clearfix')
    page = page+1
    for job in jobList:
        jobName = ""
        try:
            jobName = job.find('h3').a.text.strip()
        except:
            jobName = "没有找到公司职位"
        print("职位: ",jobName)
        companyName = ""
        try:
            companyName = job.find('p','company-name').a.text.strip()
        except:
            companyName = "没有找到公司名称"
        print("公司名称",companyName)
        salary = ""
        try:
            salary = job.find('span','text-warning').text.strip()
        except:
            salary = "没有找到薪水"
        print("薪水",salary)
        edu = ""
        try:
            edu = job.find('span','edu').text.strip()
        except:
            edu = "没有找到学历"
        print("学历",edu)
        workPos = ""
        try:
            workPos = job.find('p','condition clearfix').a.text.strip()
        except:
            workPos = "没有找到工作地点"
        print("工作地点",workPos)
        workTime = ""
        try:
            workTime = job.find('span','').text.strip()
        except:
            workTime="没有找到工作年限"
        print("工作年限",workTime)

        hrefDetail = job.find('h3').a['href']
        if "/a/" in hrefDetail:
            hrefDetail = hrefDetail[3:len(hrefDetail)]
            hrefDetail = "https://www.liepin.com/a/"+hrefDetail
            print("详情链接a: "+hrefDetail)
        else:
            print("详情链接：",hrefDetail)
        r2 = requests.get(hrefDetail,headers)
        soup = BeautifulSoup(r2.text, 'html.parser')
        duty = soup.find('div','content content-word')
        dutyText = ""
        try:
            dutyText = duty.text.strip()
        except:
            dutyText="没有找到职位描述"
        print("职位描述",dutyText)
        companyInfo = soup.find('div','info-word')
        companyInfoText="";
        try:
            companyInfoText = companyInfo.text.strip()
        except:
            companyInfoText="没有找到企业介绍"
        print("企业介绍",companyInfoText)
        json = {"职位 ":jobName,"公司名称":companyName,"薪水":salary,"学历":edu,"工作地点":workPos,"工作年限":workTime,"详情链接":hrefDetail,"职位描述":dutyText,"企业介绍":companyInfoText}
        saveToDB(json)
        time.sleep(1)
