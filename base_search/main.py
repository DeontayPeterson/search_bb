
import cv2 as cv
from matplotlib import test
import numpy as np
import pyautogui
import time
import bases
from windowcapture import Screencap
from find_item import ItemFinder

lower = np.array([50,50,50])
upper = np.array([70, 255, 255])

fist_TL = (115, 62)
fist_BR = (155, 100)
legend_TL = (58, 552)
legend_BR = (90, 764)

screenshot = Screencap.take_screenshot()
screenshot = np.array(screenshot)
screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

screenshot[fist_TL[1]:fist_BR[1], fist_TL[0]:fist_BR[0]] = np.zeros((1,))
screenshot[legend_TL[1]:legend_BR[1], legend_TL[0]:legend_BR[0]] = np.zeros((1,))
hsv = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)

mask = cv.inRange(hsv, lower, upper)

res = cv.bitwise_and(screenshot, screenshot, mask=mask)


cv.imshow('res', res)


cv.waitKey(0)