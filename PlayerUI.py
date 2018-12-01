# 2.tkinter���
# ����GUI�������̣�
# �ٵ���tkinterģ��
# �ڴ����ؼ�
# ��ָ���ؼ�������������õ���������
# �ܸ��߽����������geometry manager���пؼ�����
import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory

def mouseCallBack(*args):
    indexs = listb.curselection()
    index = int(indexs[0])
    #str_value = str(index)#����ת�ַ���
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

    #Ϊ��һ��Listbox���ð��¼�
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
    label = Label(root, text='�������ֵ��԰�\n ', fg='red', bg='white')
    label.pack(expand=YES, fill=BOTH)
root = Tk()
path = StringVar()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='��', command=selectFile)
filemenu.add_command(label='����')
filemenu.add_separator()
filemenu.add_command(label='�˳�', command=root.quit)
menubar.add_cascade(label='�ļ�', menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='��������', command=about)
menubar.add_cascade(label='����', menu=helpmenu)
listb  = Listbox(root,width=500,height=300)
root.config(menu=menubar)
root.geometry('800x500')
root.mainloop()+
