from drawing import draw_point, draw_triangles
from triangle_mask import triangle_crop
import numpy as np
import cv2 as cv

def move_coord(vec, x,y):
    vec = vec.copy()
    vec[:,0] -= x
    vec[:,1] -= y
    return vec

def warp_triangles(img, tri_f, tri_to, show_triangles = False, write_canvas = False):
    canvas = np.zeros_like(img)
    # warp from u to v
    for u,v in zip(tri_f, tri_to):
        y, x, dy, dx = cv.boundingRect(u)
        crop = img[x:x+dx, y:y+dy]
        u = move_coord(u, y,x)

        yp, xp, dyp, dxp = cv.boundingRect(v)
        v = move_coord(v, yp,xp)

        mat = cv.getAffineTransform(u, v)
        warp = cv.warpAffine(crop, mat, (dyp,dxp), flags=cv.INTER_LINEAR, borderMode=cv.BORDER_REFLECT_101)
        warp = triangle_crop(warp, v)

        out = canvas[xp:xp+dxp, yp:yp+dyp]
        out += warp * (out == 0)

        if write_canvas:
            cv.imwrite("canvas.jpg", canvas)

    if show_triangles:
        draw_triangles(canvas, tri_to)

    return canvas


## older slower code

def do_warp(img, tri_f, tri_to):
    canvas = np.zeros_like(img)
    # warp from u to v
    for u,v in zip(tri_f, tri_to):
        mat = cv.getAffineTransform(u, v)
        dx, dy = img.shape[:2]
        warp = cv.warpAffine(img, mat, (dy,dx), flags=cv.INTER_LINEAR, borderMode=cv.BORDER_REFLECT_101)
        warp = triangle_crop(warp, v)
        canvas += warp * (canvas == 0)
        cv.imwrite("canvas.jpg", canvas)

    return canvas