from my_tools import write_points
from point_selector import select_points
from detection import detect_facial_landmarks as det_fac_lmarks
import numpy as np

def image_corner_points(img):
    y, x = img.shape[0:2]

    points = []

    for i in range(0, x , x//2-1):
        for j in range(0, y, y//2-1):
            points.append((i,j))

    points.remove((x//2-1, y //2-1))

    return points

def generate_points(img, detect_facial_landmarks = True, add_corners = True, path = None,read_file = False, add_custom = False, draw_marks = False):
    points = []

    add_points = lambda pts : [points.append(p) for p in pts]

    if detect_facial_landmarks:
        facial_landmarks = det_fac_lmarks(img)
        add_points(facial_landmarks)

    if add_corners:
        corner_points = image_corner_points(img)
        add_points(corner_points)

    if read_file:
        from my_tools import read_points
        file_points = read_points(path)
        add_points(file_points)

    if draw_marks:
        from drawing import draw_point
        for p in points:
            draw_point(img, *p)

    if add_custom:
        selected = select_points(img)
        write_points(path, selected)
        add_points(selected)

    return np.array(points, np.int)