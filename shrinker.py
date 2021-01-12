from seam_carving import find_seam, draw_seam
import cv2 as cv
import numpy as np
from my_tools import resize

def split(img, seam):
    seam_stack = np.vstack([seam,] * img.shape[1]).T
    y_indices = np.indices(img.shape[:2])[1]
    left_mask = y_indices < seam_stack
    right_mask = y_indices > seam_stack
    return left_mask, right_mask

def remove_seam(img, seam):
    lm, rm = split(img, seam)
    ip = img.copy()
    im_right = img[rm]
    rm[:,:-1] = rm[:,1:]
    rm[:,-1] = False
    ip[rm] = im_right
    ip = ip[:,:-1]
    return ip

# def limited_seam_carving()

img = cv.imread("wewe.jpg")
img = resize(img, 0.2)

mask = None

for i in range(400):
    # h,w = img.shape[:2]
    # mask = np.zeros((h,w)).astype('int')
    # mask[:, :w//2 ] = 1
    # mask[:, w//2 + w//10: w - w//5] = 1

    seam = find_seam(img, mask)
    cv.imwrite("seam.jpg",draw_seam(img, seam))
    img = remove_seam(img, seam)
    # cv.imwrite("seam.jpg", img)
    if i % 5 == 0 :
        pass


a = np.zeros((4608,4228,3))
cv.imwrite("one.jpg", a)
