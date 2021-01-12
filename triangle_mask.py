import numpy as np
import cv2 as cv

### not used anymore
def fill_triangle(img, triangle):
    pts = triangle.reshape((-1, 1, 2))
    return cv.fillPoly(img, [pts], color=(1,1,1))

def triangle_mask(img, triangle):
    z = np.zeros_like(img)
    return fill_triangle(z, triangle)
###

def triangle_crop(img, tri):
    mask = np.zeros_like(img, dtype=np.float32)
    cv.fillConvexPoly(mask, np.int32(tri), (1.0, 1.0, 1.0), 16, 0)
    return (mask).astype('uint8') * img

