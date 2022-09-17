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
wincap = WindowCapture('RuneLite - blameslant')
animalfolder = 'shrimp'
if animalfolder == 'shrimp':
    startfish = 'fisher/netfishshrimp.JPG'
    invfull = 'fisher/invshrimp.JPG'
    fishingtrue = 'fisher/fishingtrue.JPG'
    fishingfalse = 'fisher/fishingfalse.JPG'
    invshrimp = 'fisher/invshrimp.JPG'
if animalfolder == 'chickens':
    startfish = 'attackchickens/Attack.JPG'
    path2 = 'attackchickens/combatnotify,JPG'
    path3 = 'attackchickens/combatover.JPG'
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def randomizer():
    antibanpixels = (random.randint(100,600)/100)
    return antibanpixels

def antirandom():
    matchent

def shiftclick(xx, yy):
    pyautogui.keyDown('shift')
    xxt = (random.randint(1,10)/100)
    pyautogui.moveTo(xx, yy, duration=xxt)
    pyautogui.click(xx, yy)
    pyautogui.keyUp('shift')

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
            needle_w = 0.5 * needle_img.shape[1]
            needle_h = 0.5 * needle_img.shape[0]
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
            time.sleep(0)
            return locs, xx, yy

def matchentplus(needle_file, threshval, starty, endy, startx, endx):
    loop_time = 0
    start_time = time.time()
    screenshot = wincap.get_screenshot()
    while loop_time < 3:
        loop_time = (time.time() - start_time)
        if loop_time < 2:
            haystack_img = screenshot[starty:endy, startx:endx]
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
            #print('nomatch',needle_file, threshval, starty, endy, startx, endx, 'threshold=', min_val, max_val)
            time.sleep(0.4)
            if min_val <= threshval:
                locs = min_loc
                print(needle_file, 'threshval', threshval, 'min_val', min_val)
                return locs, xx, yy
        if loop_time > 2:
                locs = 0
                xx = 0
                yy = 0
                time.sleep(0)
                return locs, xx, yy
        """ cv.imshow('test', haystack_img)
            cv.waitKey()"""


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



#loop_time = time()
while(True):
    if keyboard.is_pressed('q'):
        pyautogui.keyUp('shift')
        break
 #    startfish invfull  fishingtrue  fishingfalse
    # if last inv slot full
    #locs, xx, yy = matchent(invshrimp, 0.9)
    locs, xx, yy = matchentplus(invshrimp, 0.3, starty=480, endy=545, startx=708, endx=760)
    runtime = 0
    while locs != 0:
        runtime+=1
        print(runtime)
        locs, xx, yy = matchent(invshrimp, 0.3)
        while locs != 0:
            shiftclick(xx, yy)
            locs, xx, yy = matchent(invshrimp, 0.3)
            print(locs)

     #   locs, xx, yy = matchentplus(invshrimp, 0.4, starty=280, endy=545, startx=569, endx=760)
    #find shrimp to fish

    #if last inv slot full

    print('final', locs, xx, yy)






   # if locs != 0:


   # if locs != (0, 0):
