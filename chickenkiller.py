#restricted = screenshot[0:439, 0:538]
import numpy as np
import cv2 as cv
import os
import time
from windowcapture import WindowCapture
import keyboard
import pyautogui
import random
import decimal
import PIL
wincap = WindowCapture('RuneLite - charname')
animalfolder = 'cows'
if animalfolder == 'cows':
    path1 = 'attackcows/attack.JPG'
    path2 = 'attackcows/combatnotify.JPG'
    path3 = 'attackcows/combatover.JPG'
if animalfolder == 'chickens':
    path1 = 'attackchickens/Attack.JPG'
    path2 = 'attackchickens/combatnotify,JPG'
    path3 = 'attackchickens/combatover.JPG'
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))
break1 = (random.randint(1,5)*60)
break2 = (random.randint(1,5)*60)
break3 = (random.randint(1,5)*60)


def breakhandler():
    #runtime has surprassed
    return 1
def shiftclick(locs):
    pyautogui.keyDown('shift')
    xx = (random.randint(1,5)/100)
    pyautogui.moveTo(locs, duration=xx)
    pyautogui.click()
    pyautogui.keyUp('shift')
def randomizer():
    antibanpixels = (random.randint(100,600)/100)
    return antibanpixels
def antirandom():
    matchent

def pixmatchent(pix1, pix2, pix3):
    coords = []
    w1=1
    w2=769
    h1=1
    h2=624
    while coords == []:
        img = PIL.ImageGrab.grab(bbox=(w1, h1, w2, h2))
        pixels = img.load()
        width, height = img.size
        print(width)
        for x in range(w1, width):
            for y in range(h1, height):
                if pixels[x, y] == (pix1, pix2, pix3):
                    coords.append((x, y))
                    return coords




def matchent(needle_file, threshval):
    loop_time = 0
    start_time = time.time()
    while loop_time < 3:
        loop_time = (time.time() - start_time)
        if loop_time < 2:
            haystack_img = wincap.get_screenshot()

            needle_img = cv.imread(needle_file, cv.IMREAD_UNCHANGED)
            res = cv.matchTemplate(haystack_img, needle_img, cv.TM_SQDIFF_NORMED)
            needle_w = 0.5*needle_img.shape[1]
            needle_h = 0.5*needle_img.shape[0]
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            rex = (min_loc[0])
            rey = (min_loc[1])
            x = rex + 6
            y = rey + 30
            xx = x + needle_w
            yy = y + needle_h

            if min_val <= threshval:
                locs = min_loc
                print(needle_file, 'threshval', threshval, 'min_val', min_val)
                return locs, xx, yy
        if loop_time > 2:
                locs = 0
                xx = 0
                yy = 0
                pyautogui.moveTo(800, 300, duration=0.1)
                time.sleep(0)
                return locs, xx, yy



def attackconfirm(xx, yy):
    print(xx,yy, 'found ui at')
    pyautogui.moveTo(xx, yy, duration=1)
    time.sleep(0.4)
    pyautogui.click(xx, yy)
    time.sleep(15)

def rclickent(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.09)
    pyautogui.rightClick(x, y)
    time.sleep(0.2)
def clickent(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y)


break_current_time = 0
start_break_time = time.time()
while(True):
    break_current_time = (start_break_time - time.time())
    if break_current_time >= 99999999999999:
        break
    if keyboard.is_pressed('q'):
        break
    coords = pixmatchent(0, 255, 255)
    print(coords[0])
    x, y = coords[0]
    rclickent(x, y)

    locs, xx, yy = matchent(path1, 0.33)

    print('final', locs, xx, yy)

    if locs != 0:
        clickent(xx, yy)
        time.sleep(4)
        #start y and end y sart x end x

        #[starty, endy, startx, endx]
        locs, xx, yy = matchent(path2, 0.1)
        if locs != 0:
            locs = 0
            while locs == 0:
                locs, xx, yy = matchent(path3, 0.1)





   # if locs != 0:


   # if locs != (0, 0):
