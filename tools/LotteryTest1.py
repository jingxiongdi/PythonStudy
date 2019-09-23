# coding=utf-8
import tkinter as tk
import sqlite3
from tkinter.messagebox import *
import os
import traceback
import itertools
import random
import time


from tkinter import scrolledtext

global scr

def buyOneSecond():
    # t1 = threading.Thread(target=threadToUpdate)
    # t1.setDaemon(True)
    # t1.start()
    numStr = oneSecond.get()
    print("buyOneSecond:"+numStr)
    numList = numStr.split()
    print(numList)
    if len(numList) != 7:
        showerror("错误","输入数量不对，请核对")
        return
    try:
        buyNum = []
        for s in numList:
            buyNum.append(int(s))
        lastNum = buyNum[len(buyNum)-1]
        buyNum.remove(lastNum)
        if len(set(buyNum))!=6:
            showerror("错误","输入数字重复，请核对")
            return
        buyNum = sorted(buyNum)
        global buyOne
        buyOne = []
        buyOne.append(buyNum)
        buyOne.append(lastNum)
        print(buyNum)
        print(buyOne)
    except:
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        showerror("错误","输入不合法字符，请核对!")
    return

def addLuckMoney(money):
    updateMoney = int(moneyNumber.get())+money
    moneyNumber.set(updateMoney)
    myMoney.set(lName.get()+"的金币 "+str(moneyNumber.get()))
    connection = sqlite3.connect("lotteryTest.db",check_same_thread = False)
    mycursor = connection.cursor()
    connection.execute("BEGIN TRANSACTION;") # 关键点
    sql = "update userInfo set money='"+str(moneyNumber.get())+"' where user='"+lName.get().strip()+"'"
    print(sql)
    mycursor.execute(sql)
    connection.execute("COMMIT;")  #关键点
    connection.commit()
    mycursor.close()

# def startLottery1():
#     i=0
#     while i<100:
#         i+=1
#         time.sleep(0.1)
#         startLottery()
#     return

def startLottery():
    print(buyOne)
    scr.insert(tk.END,str(buyOne))
    updateMoney = int(moneyNumber.get())-2
    moneyNumber.set(updateMoney)
    myMoney.set(lName.get()+"的金币 "+str(moneyNumber.get()))

    connection = sqlite3.connect("lotteryTest.db",check_same_thread = False)
    mycursor = connection.cursor()
    connection.execute("BEGIN TRANSACTION;") # 关键点
    sql = "update userInfo set money='"+str(moneyNumber.get())+"' where user='"+lName.get().strip()+"'"
    print(sql)
    mycursor.execute(sql)
    connection.execute("COMMIT;")  #关键点
    connection.commit()
    mycursor.close()

    frontNum = []
    i=0
    while i<33:
        i+=1
        frontNum.append(i)
    backNum = []
    i=0
    while i<16:
        i+=1
        backNum.append(i)
    print(frontNum)
    print(backNum)
    lotteryNum = []#最终开奖号码

    lotteryFrontListAll = list(itertools.combinations(frontNum,6))
    randomFront = random.randint(0,len(lotteryFrontListAll)-1)
    lotteryFront = lotteryFrontListAll[randomFront]
    print(lotteryFront)

    lotteryNum.append(lotteryFront)

    lotteryBackListAll = list(itertools.combinations(backNum,1))
    randomBack = random.randint(0,len(lotteryBackListAll)-1)
    lotteryBack = lotteryBackListAll[randomBack]
    print(lotteryBack)

    lotteryNum.append(lotteryBack)

    print(lotteryNum)
    scr.insert(tk.END,str(lotteryNum)+"\n")
    if len(buyOne)==0:
        return
    lotteryFrontSum=0
    for s in lotteryFront:
        if s in buyOne[0]:
            lotteryFrontSum+=1
    lotteryBackSum = 0
    if lotteryBack==buyOne[1]:
        lotteryBackSum = 1
    print(buyOne[0])
    print(lotteryFront)
    print(buyOne[1])
    print(lotteryBack)

    print("lotteryFrontSum "+str(lotteryFrontSum))
    print("lotteryBackSum "+str(lotteryBackSum))
    if (lotteryFrontSum==0 or lotteryFrontSum==1 or lotteryFrontSum==2) and lotteryBackSum==1:
        print("六等奖")
        showinfo("提示","恭喜中六等奖5金币")
        addLuckMoney(5)
    elif(lotteryFrontSum==3 and lotteryBackSum==1) or (lotteryFrontSum==4 and lotteryBackSum==0):
        print("五等奖")
        showinfo("提示","恭喜中五等奖10金币")
        addLuckMoney(10)
    elif(lotteryFrontSum==4 and lotteryBackSum==1)or(lotteryFrontSum==5 and lotteryBackSum==0):
        print("四等奖")
        showinfo("提示","恭喜中四等奖200金币")
        addLuckMoney(200)
    elif(lotteryFrontSum==5 and lotteryBackSum==1):
        print("三等奖")
        showinfo("提示","恭喜中三等奖3000金币")
        addLuckMoney(3000)
    elif(lotteryFrontSum==6 and lotteryBackSum==0):
        print("二等奖")
        showinfo("提示","恭喜中二等奖50万金币")
        addLuckMoney(500000)
    elif(lotteryFrontSum==6 and lotteryBackSum==1):
        print("一等奖")
        showinfo("提示","恭喜中一等奖1000万金币")
        addLuckMoney(10000000)
    else:
        print("未中奖")
        showinfo("提示","未中奖")
    return

class RegisterPage(object):
    def __init__(self, master=None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d' % (300, 250)) #设置窗口大小
        self.page = tk.Frame(self.root) #创建Frame
        self.page.pack()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.surePassword = tk.StringVar()
        tk.Label(self.page).grid(row=0, stick=tk.W)
        tk.Label(self.page, text = '账户: ').grid(row=1, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=tk.E)
        tk.Label(self.page, text = '密码: ').grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=tk.E)
        tk.Label(self.page, text = '确认密码: ').grid(row=3, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.surePassword, show='*').grid(row=3, column=1, stick=tk.E)
        tk.Button(self.page, text='注册', command=self.registerAccount).grid(row=4, column=1, stick=tk.W)

    def registerAccount(self):
        #print("注册账号 "+self.username.get()+" 密码:"+self.password.get())
        if self.password.get()!=self.surePassword.get():
            showerror("错误","两次密码输入不一致")
        elif self.username.get() == "" or self.password.get() == "" or self.surePassword.get() == "":
            showerror("错误","账号密码输入不能为空")
        elif len(self.password.get())<6:
            showerror("错误","密码不能小于6个字符")
        else:
            print("开始注册流程")
            try:
                connection = sqlite3.connect("lotteryTest.db",check_same_thread = False)
                mycursor = connection.cursor()
                print("111")
                connection.execute("BEGIN TRANSACTION;") # 关键点
                print("222")
                insert_sql ="insert into userInfo (user,pwd,money) values ('"+self.username.get()+"','"+self.password.get()+"','1000')"
                print(insert_sql)
                mycursor.execute(insert_sql)
                connection.execute("COMMIT;")  #关键点
                connection.commit()
                mycursor.close()
                showinfo("提示","恭喜注册成功，获得1000金币")
                self.page.destroy()
                LoginPage(root)
            except:
                showerror("错误","该账号已存在")
    pass


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d' % (300, 180)) #设置窗口大小
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.createPage()

    def createPage(self):
        self.page = tk.Frame(self.root) #创建Frame
        self.page.pack()
        tk.Label(self.page).grid(row=0, stick=tk.W)
        tk.Label(self.page, text = '账户: ').grid(row=1, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=tk.E)
        tk.Label(self.page, text = '密码: ').grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=tk.E)
        tk.Button(self.page, text='登陆', command=self.loginCheck).grid(row=3,stick=tk.W, pady=10)
        tk.Button(self.page, text='注册', command=self.toRegisterPage).grid(row=3, column=1,stick=tk.E)

    def toRegisterPage(self):
        self.page.destroy()
        RegisterPage(root)

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        if self.username.get() == "" or self.password.get() == "":
            showerror("错误","账号密码输入不能为空")
            return
        mycursor = connection.cursor()
        sql = "select user,pwd from userInfo where user='"+name+"'"
        print(sql)
        result = mycursor.execute(sql)
        userList = result.fetchall()
        if len(userList)==0:
            showerror("错误","用户名不存在")
            return
        if userList[0].__contains__(name) and userList[0].__contains__(secret):
            print("登陆成功")
            self.page.destroy()
            lName.set(name)
            lPwd.set(secret)
            MainPage(root)
        else:
            showerror(title='错误', message='账号或密码错误！')
        mycursor.close()
        pass

class MainPage(object):
    def __init__(self, master=None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d' % (700, 600)) #设置窗口大小

        mycursor = connection.cursor()
        sql = "select money from userInfo where user='"+lName.get()+"'"
        print(sql)
        result = mycursor.execute(sql)
        moneyNumber.set(result.fetchall()[0][0])#得到的list[0]是一个元祖，应该取list[0][0]就是元祖的第一个值了。
        print(moneyNumber.get())
        myMoney.set(lName.get()+"的金币 "+str(moneyNumber.get()))
        showMyMoney = tk.Label(root,textvariable=myMoney,bd=2,width=15,fg="blue",font = 'Helvetica -12')
        showMyMoney.place(x=0,y=5,anchor='nw')

        oneSecondInput =  tk.Entry(root,textvariable=oneSecond,show=None,foreground = 'blue',font = ('Helvetica', '13'),insertbackground = 'green',width=20)
        oneSecondInput.place(x=130, y=5, anchor='nw')

        updateBtn = tk.Button(root, text="自选一注购买",bd=2,width=11,font = 'Helvetica -13',command=buyOneSecond)
        updateBtn.place(x=320, y=5, anchor='nw')

        startBtn = tk.Button(root, text="开奖",bd=2,width=11,font = 'Helvetica -13',command=startLottery)
        startBtn.place(x=520, y=5, anchor='nw')
        global scr
        scr = scrolledtext.ScrolledText(root, width=50, height=20,font=("隶书",18))  #滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
        scr.place(x=50, y=50) #滚动文本框在页面的位置
        mycursor.close()
    pass

def createTable():
    try:
        connection = sqlite3.connect("lotteryTest.db",check_same_thread = False)
        mycursor = connection.cursor()
        connection.execute("BEGIN TRANSACTION;") # 关键点
        userTable =  "create table userInfo('user' text PRIMARY KEY not null,'pwd' text not null,'money' text not null)"
        mycursor.execute(userTable)
        #transactionTable = "create table transInfo('user' text PRIMARY KEY not null,'second' text not null)"
        #mycursor.execute(transactionTable)
        connection.execute("COMMIT;")  #关键点
        connection.commit()
        mycursor.close()

    except:
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        showerror("错误提示","数据库发生异常...")
        return
    pass

root = tk.Tk() # 初始化Tk()
root.title("模拟福彩购彩交易系统")    # 设置窗口标题
isExistDB = os.path.exists("lotteryTest.db")
connection = sqlite3.connect("lotteryTest.db",check_same_thread = False)
if isExistDB==False:
    createTable()
buyOne = []
moneyNumber = tk.StringVar()
lName = tk.StringVar()
lPwd = tk.StringVar()
oneSecond = tk.StringVar()
myMoney = tk.StringVar()
LoginPage(root)
root.mainloop() # 进入消息循环