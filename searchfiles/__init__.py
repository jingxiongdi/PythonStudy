# coding=utf-8
import tkinter as tk
import tkinter.messagebox #这个是消息框，对话框的关键
import tkinter.constants
import sqlite3
import os
import threading
import traceback

def update_db():
    print("更新数据库")
    tkinter.messagebox.showerror("错误提示","更新数据库功能未完待续,可以删除目录下的allFiles.db文件,然后点击搜索，即可刷新数据库")

def mouseCallBack(*args):
    indexs = listb.curselection()
    index = int(indexs[0])
    print("index",index)
    start_directory = str(myArr[index])
    print(start_directory[2:-3])
    os.startfile(start_directory[2:-3])

def obtain_all_files(filepath,cursor):
#遍历filepath下所有文件，包括子目录
  try:
      files = os.listdir(filepath)
      for fi in files:
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
          obtain_all_files(fi_d,cursor)
        else:
          path = os.path.join(filepath,fi_d)
          update_progress.set(path)
          print("目录",path)
          sqlAdd = "insert into filepath (file_path) values ('"+path+"')"
          print("sqlAdd",sqlAdd)
          cursor.execute(sqlAdd)
  except Exception as e:
      traceback.print_exc()
      print("扫描文件出异常了，点击确定继续扫描")
      tkinter.messagebox.showerror("错误提示","扫描文件出异常了看，点击确定继续扫描")




def scan_file():
    print("开始扫描文件")
 #   del myArr[:]
    connection.execute("BEGIN TRANSACTION;") # 关键点
    cursor = connection.cursor()
    obtain_all_files('G:\\',cursor)
    print("G盘扫描完成...")
    tkinter.messagebox.showinfo("温馨提示","G盘扫描完成....")
    connection.execute("COMMIT;")  #关键点
    connection.commit()
    connection.close()


def insert_db():
     t1 = threading.Thread(target=scan_file)
     t1.setDaemon(True)
     t1.start()
     tkinter.messagebox.showinfo("温馨提示","正在更新数据库，请等待...")

def search_file():
     #表示创建一个数据库,并获得连接
     print("数据库是否存在: ",isExistDB)
     if(isExistDB==False):
         tkinter.messagebox.showwarning("警告","数据库不存在，将更新数据库文件！")
         try:
             mycursor = connection.cursor()
             file_sql =  "create table filepath('file_path' text not null)"
             mycursor.execute(file_sql)
             mycursor.close()
             insert_db()
         except:
             tkinter.messagebox.showerror("错误提示","数据库发生异常...")
             return
     else:
         print("开始搜索")
         listb.delete(0,tk.constants.END)
         mycursor = connection.cursor()
         entry_text = inputText.get()
         search_sql = "select * from filepath where file_path like '%"+entry_text+"%'"
         files = mycursor.execute(search_sql)
          #tkinter.messagebox.showwarning("警告","没有找到对应的文件！")
         for f in files:
            print(f)
            myArr.append(f)
            listb.insert(tkinter.constants.END,f)
         print("搜索完成")
         mycursor.close()

myArr = []
isExistDB = os.path.exists("allFiles.db")
connection = sqlite3.connect("allFiles.db",check_same_thread = False)
root = tk.Tk() # 初始化Tk()
root.title("电脑文件搜索工具(仿everything)By景兄弟V1.0")    # 设置窗口标题
root.geometry("800x600")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=False, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
#设置输入框
inputText = tk.Entry(root,show=None,foreground = 'red',font = ('Helvetica', '15', 'bold'),insertbackground = 'green',width=65)
inputText.pack()
#设置按钮，以及放置的位置
searchBtn = tk.Button(root, text="搜索", fg="blue",bd=2,width=10,command=search_file)#command中的方法带括号是直接执行，不带括号才是点击执行
searchBtn.place(x=200, y=40, anchor='nw')
updateBtn = tk.Button(root, text="更新数据库", fg="blue",bd=2,width=10,command=update_db)
updateBtn.place(x=400, y=40, anchor='nw')

update_progress = tk.StringVar()
update_progress.set('还未开始扫描')
lb = tk.Label(root,text="还未开始", fg="blue",bd=2,width=100, textvariable=update_progress)
lb.place(x=20,y=90)

listb  = tk.Listbox(root,width=110,height=20)
listb.place(x=1, y=120, anchor='nw')
sb = tk.Scrollbar(root)    #垂直滚动条组件
sb.pack(side=tkinter.constants.RIGHT,fill=tkinter.constants.Y)  #设置垂直滚动条显示的位置
listb.config(yscrollcommand=sb.set)
listb.bind("<<ListboxSelect>>",mouseCallBack)
root.mainloop() # 进入消息循环