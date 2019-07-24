import pyautogui
import _thread
import time


def startMove(delay):
    print("start =====")
    time.sleep(delay)
    curW,curH = pyautogui.position()
    print(curW,'*',curH)
    if (curW<(screenWidth-10)) and (curH<(screenHeight-10)):
        pyautogui.moveTo(curW+5,curH+5)
    else:
        pyautogui.moveTo(10,10)
    pass

screenWidth, screenHeight = pyautogui.size()
print(screenWidth,'*',screenHeight)
curW,curH = pyautogui.position()
print(curW,'*',curH)
while True:
    startMove(2)