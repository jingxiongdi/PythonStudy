# coding=utf-8
import tkinter as tk
import tkinter.messagebox #这个是消息框，对话框的关键
import tkinter.constants
import os
import threading

global deviceStatus
global showStatusInfo
global bm1
global statusPic
showStatusInfo = False

secondLine = 40
thirdLine = 80

def runCmd(str):
    p = os.popen(str)
    return p.read()

def screenShot():
    os.system("adb shell screencap -p /sdcard/screen.jpg")
    os.system("adb pull /sdcard/screen.jpg")
    return

def updatePic():
    screenShot()
    os.system("del screen.gif")
    os.system("ffmpeg -i screen.jpg -s 240x425 screen.gif")
    global bm1
    bm1 = tk.PhotoImage(file='screen.gif')
    global statusPic
    statusPic.configure(imag=bm1)
    return

def getDeviceStatus():
    status = runCmd("adb devices").strip()
    print(status)
    if status=="List of devices attached":
        status="当前无设备连接"
    else:
        status = status.replace("List of devices attached","").strip()
        t1 = threading.Thread(target=updatePic)
        t1.setDaemon(True)
        t1.start()
    deviceStatus.set(status)
    global showStatusInfo
    if showStatusInfo==True:
        tkinter.messagebox.showinfo("提示","设备状态已更新")
    showStatusInfo = True
    return status

def screenOn():
    os.system("adb shell input keyevent 224")
    return

def screenOff():
    os.system("adb shell input keyevent 223")
    return

def unlockScreen():
    os.system("adb shell input swipe 500 600 500 50")
    return

def downSlide():
    os.system("adb shell input swipe 500 50 500 600")
    return

def showMac():
    p = runCmd("adb shell cat /sys/class/net/wlan0/address")
    tk.messagebox.showinfo("提示","Android设备MAC地址为"+p)
    return

def getDensity():
    p = runCmd("adb shell wm density")
    tk.messagebox.showinfo("提示","屏幕密度为"+p)
    return

def getScreenSize():
    p = runCmd("adb shell wm size")
    tk.messagebox.showinfo("提示","android设备屏幕分辩率"+p)
    return

def getWifi():
    p = runCmd("adb shell cat /data/misc/wifi/*.conf")
    list = p.split("network=")
    i=1

    ########################测试代码#################################
    # s=0
    # while s<150:
    #     s+=1
    #     list.append(p.split("network=")[1])
    ########################测试代码#################################

    result = ""
    while i<len(list):
        ssid = list[i].split("ssid=")[1].split("psk=")[0].strip()
        psk = list[i].split("psk=")[1].split("key_mgmt=")[0].strip()
        result =result+ "wifi名称："+ssid+" wifi密码："+psk+"  --- "
        print(result)
        i+=1
    tk.messagebox.showinfo("所有wifi名称和密码",result)
    return

def getCurrentActivity():
    p = runCmd("adb shell dumpsys window | findstr mCurrentFocus")
    tk.messagebox.showinfo("当前activity",p)
    return

def getAllPkg():
    p = runCmd("adb shell pm list package")
   # tk.messagebox.showinfo("所有应用",p)
    list = p.split("\n\n")
    print(list)
    for s in list:
        packageStr = s.split(":")
        if len(packageStr)>1:
            s = s.split(":")[1]
            listb.insert(tkinter.constants.END,s)
    return p

def getAllFile():
    p = runCmd("adb shell ls /mnt/sdcard/")
    list = p.split("\n\n")
    print(list)
    for s in list:
        listFile.insert(tkinter.constants.END,s)
    return

root = tk.Tk() # 初始化Tk()
root.title("ADB界面工具V1.0")    # 设置窗口标题
root.geometry("1100x650")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=False, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
deviceStatus = tk.StringVar()

getDeviceStatus()
#显示当前设备状态的文本框
statusText = tk.Label(root, textvariable=deviceStatus, fg="blue",bd=2,width=50,font = 'Helvetica -16')
statusText.place(x=150, y=10, anchor='nw')

#更新当前设备状态的按钮
updateBtn = tk.Button(root, text="更新状态",bd=2,width=10,font = 'Helvetica -16',command=getDeviceStatus)
updateBtn.place(x=500, y=5, anchor='nw')

screenOnBtn = tk.Button(root, text="亮屏",bd=2,width=5,font = 'Helvetica -16',command=screenOn)
screenOnBtn.place(x=0, y=secondLine, anchor='nw')

screenOffBtn = tk.Button(root, text="灭屏",bd=2,width=5,font = 'Helvetica -16',command=screenOff)
screenOffBtn.place(x=70, y=secondLine, anchor='nw')

unlockScreenBtn = tk.Button(root, text="上滑/解锁",bd=2,width=10,font = 'Helvetica -16',command=unlockScreen)
unlockScreenBtn.place(x=140, y=secondLine, anchor='nw')

unlockScreenBtn = tk.Button(root, text="下滑",bd=2,width=5,font = 'Helvetica -16',command=downSlide)
unlockScreenBtn.place(x=260, y=secondLine, anchor='nw')

screenShotBtn = tk.Button(root, text="截屏保存",bd=2,width=10,font = 'Helvetica -16',command=screenShot)
screenShotBtn.place(x=330, y=secondLine, anchor='nw')

showMacBtn = tk.Button(root, text="查看mac地址",bd=2,width=10,font = 'Helvetica -16',command=showMac)
showMacBtn.place(x=450, y=secondLine, anchor='nw')

showMacBtn = tk.Button(root, text="查看分辨率",bd=2,width=10,font = 'Helvetica -16',command=getScreenSize)
showMacBtn.place(x=570, y=secondLine, anchor='nw')

getDensityBtn = tk.Button(root, text="查看屏幕密度",bd=2,width=10,font = 'Helvetica -16',command=getDensity)
getDensityBtn.place(x=700, y=secondLine, anchor='nw')

getDensityBtn = tk.Button(root, text="查看连接过的wifi和密码(root)",bd=2,width=25,font = 'Helvetica -16',command=getWifi)
getDensityBtn.place(x=0, y=thirdLine, anchor='nw')

getCurrentActivityBtn = tk.Button(root, text="当前activity",bd=2,width=10,font = 'Helvetica -16',command=getCurrentActivity)
getCurrentActivityBtn.place(x=260, y=thirdLine, anchor='nw')



listb  = tk.Listbox(root,width=50,height=12)
listb.place(x=1, y=120, anchor='nw')

listFile  = tk.Listbox(root,width=50,height=12)
listFile.place(x=460, y=120, anchor='nw')

getAllFile()

#listb.bind("<<ListboxSelect>>",mouseCallBack)
global bm1
bm1 = tk.PhotoImage(file='screen.gif')
global statusPic
statusPic = tk.Label(root, image=bm1,width=250)
statusPic.place(x=830, y=10, anchor='nw')

getAllPkg()

root.mainloop() # 进入消息循环