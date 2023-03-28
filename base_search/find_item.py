import cv2 as cv
import pyautogui
import numpy as np
METHOD = cv.TM_CCOEFF_NORMED


class ItemFinder:
    def __init__(self):
        self.public_points = []
        self.bunker_w = 0
        self.bunker_h = 0
    
    def get_results(self, game_screenshot, bb, threshold=0.5):
        result = cv.matchTemplate(game_screenshot, bb, METHOD)
        bbw = bb.shape[1]
        bbh = bb.shape[0]

        self.bunker_w = bbw
        self.bunker_h = bbw

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        rectangles = []
        for location in locations:
            rect = [int(location[0]), int(location[1]), bbw, bbh]
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        points = []

        if len(rectangles):
            line_color = (0, 0, 255)
            line_type = cv.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv.MARKER_CROSS

            for (x, y, w, h) in rectangles:
                center_x = x + int(w/2)
                center_y = y + int(h/2)

                points.append((center_x, center_y))
                self.public_points.append((center_x, center_y))

                top_left = (x, y)
                bottom_right = (x+h, y+w)


                cv.rectangle(game_screenshot, top_left, bottom_right, color=line_color, lineType=line_type,
                             thickness=2)
        return points


    def check_for_material(self, haystack, needle, threshold=0.5):
        found_material = False

        result = cv.matchTemplate(haystack, needle, METHOD)

        sq_w = self.bunker_w
        sq_h = self.bunker_h

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        rectangles = []

        for location in locations:
            rect = [int(location[0]), int(location[1]), sq_w, sq_h]
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        if len(rectangles) > 0:
            found_material = True
            # pyautogui.alert(text=f"Material found! Base will be marked in green", title=f"{needle} is in the base")
            return found_material
        else:
            return found_material

