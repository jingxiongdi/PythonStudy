# 2.tkinter编程
# 创建GUI程序流程：
# ①导入tkinter模块
# ②创建控件
# ③指定控件的组件，并放置到主窗口中
# ④告诉界面管理器（geometry manager）有控件产生
import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory

def mouseCallBack(*args):
    indexs = listb.curselection()
    index = int(indexs[0])
    #str_value = str(index)#数字转字符串
    print(" mouse click "+path_+"/"+listSongs[index])
    curPath = path_+"/"+listSongs[index]
    try:
        pygame.mixer.music.stop()
    except:
        print("stop play error")

    pygame.mixer.init()
    track = pygame.mixer.music.load(curPath)
    pygame.mixer.music.play()


def getMp3List(folder):
    global list
    global listSongs
    list = os.listdir(folder)
    listSongs = []
    counter = 0

    #为第一个Listbox设置绑定事件
    listb.bind("<<ListboxSelect>>",mouseCallBack)
    while counter < len(list):
        if os.path.splitext(list[counter])[1]==".mp3":
            print(list[counter])
            listSongs.append(list[counter])
            listb.insert(END,list[counter])
        counter +=1
    listb.pack()

def selectFile():
    global  path_
    path_ = askdirectory()
    path.set(path_)
#    print("path "+path)
    print("path_ "+path_)
    getMp3List(path_)
def about():
    label = Label(root, text='花景音乐电脑版\n ', fg='red', bg='white')
    label.pack(expand=YES, fill=BOTH)
root = Tk()
path = StringVar()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='打开', command=selectFile)
filemenu.add_command(label='保存')
filemenu.add_separator()
filemenu.add_command(label='退出', command=root.quit)
menubar.add_cascade(label='文件', menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='关于作者', command=about)
menubar.add_cascade(label='关于', menu=helpmenu)
listb  = Listbox(root,width=500,height=300)
root.config(menu=menubar)
root.geometry('800x500')
root.mainloop()+
