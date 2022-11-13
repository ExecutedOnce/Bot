import pyautogui
import keyboard
import time

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

def shiftclick(xx, yy):
    pyautogui.keyDown('shift')
    xxt = (random.randint(1,5)/100)
    pyautogui.moveTo(locs, duration=xxt)
    pyautogui.click(xx, yy)
    pyautogui.keyUp('shift')

def matchent(needle_file, threshval):
    loop_time = 0
    start_time = time.time()
    while loop_time < 3:
        loop_time = (time.time() - start_time)
        if loop_time < 2:
            haystack_img = wincap.get_screenshot()
            needle_img = cv.imread(needle_file, cv.IMREAD_UNCHANGED)
            res = cv.matchTemplate(haystack_img, needle_img, cv.TM_SQDIFF_NORMED) #results
            needle_w = 0.5 * needle_img.shape[1]
            needle_h = 0.5 * needle_img.shape[0]
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res) #gets  lowest, highest match. Lowest and highest (x,y) coords.
            rex = (min_loc[0])
            rey = (min_loc[1])
            x = rex + 6
            y = rey + 30
            xx = x + needle_w
            yy = y + needle_h
            if min_val <= threshval: #Checks to make sure match isnt false
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
    while loop_time < 3:
        loop_time = (time.time() - start_time)
        if loop_time < 2:
            cropme = wincap.get_screenshot()
            haystack_img = cropme[starty:endy, startx:endx]
            needle_img = cv.imread(needle_file, cv.IMREAD_UNCHANGED)
            res = cv.matchTemplate(haystack_img, needle_img, cv.TM_SQDIFF_NORMED)
            needle_w = 0.5*needle_img.shape[1]
            needle_h = 0.5*needle_img.shape[0]
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            rex = (min_loc[0]) #gets width coord match
            rey = (min_loc[1]) #gets height coord match
            x = rex + 6 #width coord + 6
            y = rey + 30 #height coord + 30
            xx = x + needle_w #above + half of needle width (center) 0.5*needle_img.shape[1]
            yy = y + needle_h  #above + half of needle height (center) 0.5*needle_img.shape[0]
            print('nomatch',needle_file, threshval, starty, endy, startx, endx, 'threshold=', min_val, max_val, min_loc)
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
        break
    #startfish invfull  fishingtrue  fishingfalse
    # if last inv slot full
    locs, xx, yy = matchentplus('fisher/invshrimp.JPG', 0.2, starty=508, endy=545, startx=708, endx=760)
    while locs != 0:
        print(locs)
        shiftclick(xx, yy)
        locs, xx, yy = matchentplus('fisher/invshrimp.JPG', 0.2, starty=280, endy=545, startx=569, endx=760)
    #find shrimp to fish
    #if last inv slot full
    print('final', locs, xx, yy)






   # if locs != 0:


   # if locs != (0, 0):


















































while True:

    posXY = pyautogui.position()
    if keyboard.is_pressed('q'):
        posXY = pyautogui.position()
        print(posXY, pyautogui.pixel(posXY[0], posXY[1]))
        time.sleep(0.5)

    if posXY[0] == 0:
        break
    else: continue






