import pyautogui
import time
import cv2
import os

time.sleep(1)
# mylist = ["iconItems_toolboxWornOut",
#           "iconItems_toolboxAlexs",
#           "iconItems_toolboxCommodious",
#           "iconItems_toolboxEngineers"]
mylist = []
path = "C:/DeadByDaylight_Project/DBD/Items"
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.png' in f:
            # print(f)
            mylist.append(f)
path = "Items/"
list = [path + x for x in mylist]
print(list)

# Locate images on screen and move mouse to them
# for i in range(len(list)):
#     x, y = pyautogui.locateCenterOnScreen(list[i], confidence=0.9)
#     print(x,y)
#     pyautogui.moveTo(x,y)
#     time.sleep(0.5)