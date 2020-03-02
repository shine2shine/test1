import random
import time
import pyautogui
import cv2

# im1 = pyautogui.screenshot(region=(400,0,300,70))
# time.sleep(60)
# im2 = pyautogui.screenshot(region=(400,0,300,70))
# im1.show()
# im2.show()

def calc(start,end,initValue):
    t = 0
    
    for i in range(end-start):
        t = t + initValue * 1.15 ** i
    return t




print(calc(170,200,464.24))
print(calc(50, 75, 6.01))


