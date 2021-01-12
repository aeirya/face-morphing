import os
import cv2 as cv
import numpy as np

# reading points from file
def read(path):
    text = ""
    with open(path, 'r') as reader:
        text = reader.read()
    return text

def read_points(path):
    if not os.path.exists(path):
        return []
    
    text = read(path)
    lines = text.split("\n")[:-1]
    tuples = [line.split(",") for line in lines]
    return [(int(x), int(y)) for (x,y) in tuples]

def write_points(path, points):
    with open(path, 'a') as writer:
        writer.writelines(
            [f"{p[0]},{p[1]}\n" for p in points]
        )

# saving frame
def save_frame(img, i):
    h,w = img.shape[:2]
    h = h - h % 2
    w = w - w % 2
    cv.imwrite(
        "frames/frame{:02d}.jpg".format(i),
        img[:h, :w]
        )

# image tools
def resize(img, scale):
    h,w = img.shape[:2]
    h,w = int(scale * h), int(scale * w)
    return cv.resize(img, (w,h))

def float32_array(l):
    return np.array(l).astype('float32')

def make_same_size(img0, img1):
    # print(img0.shape)
    # print(img1.shape)
    x,y = img0.shape[:2]
    u,v = img1.shape[:2]
    avg = lambda x,y : (x + y) // 2 
    dest_shape = (avg(y,v), avg(x,u))
    img0 = cv.resize(img0, dest_shape)
    img1 = cv.resize(img1, dest_shape)
    # print(dest_shape)
    return (
        img0, img1
    )