import os

import pyautogui
import keyboard
keyboard.wait('ctrl')
print(keyboard.read_key())
first=pyautogui.position()

keyboard.wait('alt')
print('alt')
second=pyautogui.position()

print(first.x,first.y,second.x, second.y)
width=abs(second.x-first.x)
height=abs(second.y-first.y)
print('calc')
pyautogui.screenshot(region=(first.x,first.y, width, height),
                        imageFilename='tu.png')

im=pyautogui.locateOnScreen('tu.png', confidence=0.5)
print(im)
pyautogui.screenshot(region=(im.left,im.top, im.width, im.height),
                        imageFilename='tu1.png')
os.startfile('tu1.png')
# try:
#     pyautogui.click('tu.png')
# except:
#     print('don`t found screen')