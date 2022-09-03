import pyautogui
import time

time.sleep(1)
# print(pyautogui.locateOnScreen('num_9.png'))
# coords = pyautogui.locateAllOnScreen('num_9.png')
# for element in coords:
#     print(element)
# pyautogui.moveTo('num_9.png')

# x = 676
# y = 462
# RGB = 254
# tolerance = 0
# image = pyautogui.screenshot('items/screenshot.png')
# color = image.getpixel((676, 462)) 
# potato = pyautogui.pixelMatchesColor(x, y, (RGB, RGB, RGB), tolerance) # x, y, R G B, tolerance
# print(potato)
# print(color)

# pyautogui.locateAllOnScreen('Items/num_9.png')
# pyautogui.moveTo('Items/num_9.png')

pyautogui.locateAllOnScreen('Items/iconItems_toolboxWornOut.png')
pyautogui.moveTo('Items/iconItems_toolboxWornOut.png')