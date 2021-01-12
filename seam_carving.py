from os import makedev
import numpy as np
import cv2 as cv

def sobel(img, k = -1, is_gray = True):
    sobelx = cv.Sobel(img,cv.CV_64F,1,0,k)
    sobely = cv.Sobel(img,cv.CV_64F,0,1,k)
    g3 = np.sqrt(sobelx**2 + sobely**2)
    if not is_gray:
        g3 = (g3 ** 2).sum(axis = 2)
    return g3

def find_energy(img, mask):
    s =  sobel(img, is_gray = len(img.shape)!=3).astype('int16')
    if not mask is None:
        s =  s* (1-mask) + mask* s.max()
    return s

def find_min(list):
    index = np.argmin(list)
    value = list.min()
    return value, index

def find_energy_map(energy):
    energy_map = np.zeros_like(energy).astype('uint16')
    energy_map[-1, :] = energy[-1, :]
    next_elements = np.zeros_like(energy)

    for x in range(energy.shape[0]-2, -1, -1):
        for y in range(0, energy.shape[1]):
            left, right = max(0, y-1), min(energy.shape[1]- 1, y + 1)
            ne_energy, next_element = find_min(energy_map[x + 1, left:right+1])
            
            if left == 0 and y == 0:
                next_element += 1

            next_elements[x,y] = next_element - 1
            energy_map[x,y] = ne_energy + energy[x,y]

    return energy_map, next_elements

def find_seam_at(next_elements, e):
    seam = np.zeros((next_elements.shape[0]), np.int)
    seam[0] = e
    for i in range(1,len(seam)):
        seam[i] = seam[i-1] + next_elements[i, seam[i-1]]
    return seam

def find_seam_vertical(img, mask):
    energy = find_energy(img, mask)
    energy_map, next_elements = find_energy_map(energy)
    best = energy_map[0].argmin()
    seam = find_seam_at(next_elements, best)
    return seam

def find_seam(img, mask = None):
    return find_seam_vertical(img, mask)

def draw_seam(img, seam):
    draw = img.copy()
    for i in range(img.shape[0]):  
        draw[i, seam[i]] = [0,0,0]
    return draw





# def test():
#     from my_tools import smaller
#     img = cv.imread("texture2.jpg")
#     img = smaller(img, 1)
#     seam = find_seam_vertical(img)
#     draw = draw_seam(img, seam)
#     cv.imwrite("seam.jpg", draw)

# def test2():
    # img = cv.imread("s.png")
    # left = cv.cvtColor(img, cv.COLOR_BGR2LAB)[:,:,1:]
    # seam = find_seam(left)
    # draw = draw_seam(img, seam)
    # cv.imwrite("seam.jpg", draw)

