#!/usr/bin/python

import pyautogui
import subprocess
import time
import keyboard
import random
import win32api, win32con
from pyautogui import *

#Open edge. Edge always opens in maximised mode. This is done through properties
#This will also boot up the website
subprocess.Popen('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
time.sleep(3)
keyboard.press_and_release('ctrl+l')
time.sleep(0.5)
keyboard.write("https://humanbenchmark.com/tests/aim")
keyboard.press_and_release("enter")
time.sleep(3)
keyboard.press_and_release('ctrl+l')
time.sleep(0.5)
keyboard.press_and_release('ctrl+a')
keyboard.write("Press Slash to stop the bot")


#Click Function (Clicks in on x and y position)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Failsafe
while keyboard.is_pressed('/') == False:
    pic = pyautogui.screenshot(region=(100,240,1300,560))

    #(149, 195, 232)

    width, height = pic.size

    for x in range (0, 1300, 30):
        for y in range (0, 560, 30):

            r,g,b = pic.getpixel((x,y))

            if b == 232:
                click(x+100,y+240)
                break
       
    










    
