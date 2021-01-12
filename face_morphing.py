from detection import draw_facial_landmarks
from point_generation import generate_points
from triangulation import co_triangulate
from warping import warp_triangles
from my_tools import save_frame, float32_array, resize, make_same_size
from animation import clip

import numpy as np
import cv2 as cv

def gen_morph_frames(img_from, img_to, points_from, points_to, n):
    tri_f, tri_to = co_triangulate(points_from, points_to)
    tri_f, tri_to = float32_array(tri_f), float32_array(tri_to)
    delta = tri_to - tri_f

    alphas = np.linspace(0, 1, num=n, endpoint=True)
    frame = 0
    for alpha in alphas:
        adelta = delta * alpha
        im1 = warp_triangles(img_from, tri_f, tri_f + adelta)
        im2 = warp_triangles(img_to, tri_to, tri_to - delta + adelta)
        im = (1 - alpha) * im1 + alpha * im2
        save_frame(im, frame)
        frame+=1

def make_morph_clip(img_from, img_to, points_from, points_to, fps, duration):
    n = int(fps * duration)
    gen_morph_frames(img_from, img_to, points_from, points_to, n)
    clip(fps, img_from.shape)

def gen_points(
    img_from,
    img_to,
    detect_facial_landmarks = True,
    add_custom = False,
    read_file = True,
    read_path0 = "from.txt", 
    read_path1 = "to.txt"):

    # points with opencv coordinates
    points_from = generate_points(
        img_from,
        path=read_path0, 
        read_file=read_file, 
        add_custom=add_custom,
        detect_facial_landmarks=detect_facial_landmarks, 
        draw_marks=False)
    points_to = generate_points(
        img_to,
        path=read_path1, 
        read_file=read_file, 
        add_custom=add_custom,
        detect_facial_landmarks= detect_facial_landmarks, 
        draw_marks=False)

    return points_from, points_to

def morph(
    img_from, img_to, 
    duration = 3, 
    fps = 24, 
    ):
    
    img_from, img_to = make_same_size(img_from, img_to)
    points_from, points_to = gen_points(img_from, img_to)
    make_morph_clip(img_from, img_to, points_from, points_to, fps, duration)
    

def main(from_path = "from.jpg", to_pth = "to.jpg"):
    img_from = cv.imread(from_path)
    img_to = cv.imread(to_pth)
    # if single person image set scale = 0.75
    img_from = resize(img_from, scale = 0.75)
    # img_from = resize(img_from, 0.6)

    morph(img_from, img_to)

main()