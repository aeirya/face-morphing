from drawing import draw_text, draw_point
import numpy as np
import cv2 as cv

i = 0

def select_points(img):
    pts = []

    def click_event(event, x, y, flags, params): 
        global i
        if event == cv.EVENT_LBUTTONDOWN: 
            point = (x,y)
            pts.append(point)
            draw_point(img, *point)
            draw_text(img, *point, i)
            i += 1
            print(point)
            cv.imshow('image', img) 

    cv.imshow("image", img)
    cv.setMouseCallback('image', click_event)
    cv.waitKey(0)
    cv.destroyAllWindows()
    global i
    i = 0

    pts= np.array(pts)
    return pts