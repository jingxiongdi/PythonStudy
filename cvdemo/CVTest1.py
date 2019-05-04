"""
:param
    无
:return
    无
功能：调用笔记本摄像头获取视频图片
"""""
import numpy as np
import cv2
import time
#调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
cap=cv2.VideoCapture(0)
sucess,img=cap.read()
time.sleep(5)
global i
i=0
while True:
    #从摄像头读取图片
    time.sleep(3)
    sucess,img=cap.read()
    timestr = time.strftime("%Y%m%d%H%M%S",time.localtime())
    filename = 'D:/tupian/1/'+timestr+".jpg"
    print(filename)
    cv2.imwrite(filename,img)
    cv2.destroyAllWindows()
    i = i+1
    print("已拍:%d",i)
    if i>60:
        break
#关闭摄像头
print("end....")
cap.release()