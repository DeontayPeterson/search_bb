import cv2 as cv
import pyautogui
import numpy as np
from compvision import CompVision
from vision import Vision
import time

GREEN = (0, 255, 0)

vision = Vision()
comp_vision = CompVision()
foxhole = pyautogui.getWindowsWithTitle('War')[0]

#Current Bunker Bases

bb1_z = cv.imread('bb1_zoomed.png', cv.COLOR_RGB2BGR)
bb2_z = cv.imread('bb_t2_zoom_out.png', cv.COLOR_RGB2BGR)
bb3_z = cv.imread('bb_t3_zoom.png', cv.COLOR_RGB2BGR)

#Relic/Townhall bases
town_hall = cv.imread('townhall.png', cv.COLOR_RGB2BGR)
relic_base = cv.imread('relic_zoomed.png', cv.COLOR_RGB2BGR)

#Materials
wreckage = cv.imread('wreckage.png', cv.COLOR_RGB2BGR)
rmat = cv.imread('Rmat.png', cv.COLOR_RGB2BGR)
bonesaw = cv.imread('Bonesaw.png', cv.COLOR_RGB2BGR)
forty = cv.imread('40mm.png', cv.COLOR_RGB2BGR)
sixty_eight = cv.imread('68mm.png', cv.COLOR_RGB2BGR)
petrol = cv.imread('petrol.png', cv.COLOR_RGB2BGR)
satchel = cv.imread('satchel.png', cv.COLOR_RGB2BGR)




screenshot = comp_vision.take_screenshot()
my_points = vision.get_results(bb=bb2_z, game_screenshot=screenshot, threshold=.68)
my_points += vision.get_results(bb=bb3_z, game_screenshot=screenshot, threshold=.7)
my_points += vision.get_results(bb=bb1_z, game_screenshot=screenshot, threshold=.67)
my_points += vision.get_results(bb=town_hall, game_screenshot=screenshot, threshold=.5)
my_points += vision.get_results(bb=relic_base, game_screenshot=screenshot, threshold=.5)


points_for_py = vision.public_points
foxhole.activate()
item_selected = pyautogui.prompt(title="Select an Item", text=f"40mm\n68mm\nARCRPG\nRmat\nWreckage\nPetrol\nSatchel")
item_selected.lower()
mat_selected = 'rmat'
cor_threshold = 0

if item_selected == 'wreckage':
    mat_selected = wreckage
    cor_threshold = .7
elif item_selected == '40mm':
    mat_selected = forty
    cor_threshold = .83
elif item_selected == '68mm':
    mat_selected = sixty_eight
    cor_threshold = .8
elif item_selected == 'arcrpg':
    mat_selected = bonesaw
    cor_threshold = .8
elif item_selected == "rmat":
    mat_selected = rmat
    cor_threshold = .8
elif item_selected == 'petrol':
    mat_selected = petrol
    cor_threshold = .85
elif item_selected == 'satchel':
    mat_selected = satchel
    cor_threshold = .8



for point in points_for_py:
    x = point[0]
    y = point[1]
    pyautogui.moveTo(x, y)
    time.sleep(1.5)

    base_contents = pyautogui.screenshot()
    base_contents = np.array(base_contents)
    base_contents = cv.cvtColor(base_contents, cv.COLOR_RGB2BGR)


            ######Check for material ####### Wreckage = (.7) Rmat = (.8) Bonesaw = (.8)
    condition = vision.check_for_material(base_contents, mat_selected, threshold=cor_threshold)
    if condition:
        w = bb2_z.shape[1]
        h = bb2_z.shape[0]
        top_left = (x,y)
        bottom_right = (x + w, y + h)
        cv.rectangle(screenshot, top_left, bottom_right, color=GREEN, lineType=cv.LINE_4, thickness=2 )

print(len(screenshot))
cv.imshow('Marked', screenshot)

cv.waitKey()
cv.destroyAllWindows()
