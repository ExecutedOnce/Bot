import pyscreeze
import pyautogui
import random
import time
import numpy as np
import cv2 as cv


ff = 0
ListA = ['tin1.JPG', 'tin2.JPG']
ListB = ['tingone1.JPG', 'tingone2.JPG']
time.sleep(1)
length = len(ListA)


def shiftclick(dloc):
    pyautogui.keyDown('shift')
    xx = (random.randint(1,5)/100)
    pyautogui.moveTo(dloc, duration=xx)
    pyautogui.click()
    pyautogui.keyUp('shift')
#for i in ListA:

    #print(i)

def rock1():
    y = 0
    j = 9
    while j < 10:
        y = y + 2
        print(y)
        loc = pyautogui.locateOnScreen('iron1.JPG', grayscale=False, confidence=0.9)
        pyautogui.moveTo(loc, duration=0.1)
        pyautogui.click()
        r = None
        while r is None:
            print('waiting for ore1')
            r = pyautogui.locateOnScreen('iron1e.JPG', grayscale=False, confidence=0.85)
            
        loc = pyautogui.locateOnScreen('iron2.JPG', grayscale=False, confidence=0.99)
        pyautogui.moveTo(loc)
        pyautogui.click()
        print('clicking on second ore')

        varr = None
        while varr is None:
            print('waiting for ore2')
            varr = pyautogui.locateOnScreen('iron2e.JPG', grayscale=False, confidence=0.9)


        if y >= 6:
            dloc = pyautogui.locateOnScreen('invore.JPG', grayscale=False, confidence=0.7)
            while dloc != None:
                print('cleaning')
                shiftclick(dloc)
                dloc = pyautogui.locateOnScreen('invore.JPG', grayscale=False, confidence=0.7)
                continue

            else:
                y = 0
                continue


x = 0
while x < 1 :
    rock1()

def breakhandler():
    x = time.clock()
    print(x)


"""8888"""

#for image in ListA:
 #   try:
 #       loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.8 )
  #      print (loc)
  #      pyautogui.moveTo(loc, duration=0.5)
  #      pyautogui.click()
  #      time.sleep(5)
  #  except pyscreeze.ImageNotFoundException:
   #     print (image)



