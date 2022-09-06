import cv2 as cv
import pyautogui
import numpy as np


class CompVision:
    def __init__(self):
        pass

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        #Color from RGB -> BGR

        return screenshot
