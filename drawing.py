import cv2 as cv

def draw_triangles(img, triangles):
    line = lambda u,v : cv.line(img, (u[0], u[1]), (v[0], v[1]), (255,100,100), 2)
    for u,v,w in triangles:
        line(u,v)
        line(v,w)
        line(w,u)

def draw_point(img, x,y):
    cv.circle(img, (x, y), 2, (0, 255, 0), -1)


def generate_rainbow_colors():
    import numpy as np
    n = 7
    h = np.linspace(0, 1, n, True)
    i = np.ones((n))
    x = np.vstack((h,i,i)).T
    x = (x*255).astype('uint8').reshape((n,1,3))
    return cv.cvtColor(x, cv.COLOR_HSV2BGR_FULL)

from itertools import cycle
colors = cycle(generate_rainbow_colors())

def draw_text(img, x,y, text):
    global colors
    font = cv.FONT_HERSHEY_SIMPLEX
    r,g,b = colors.__next__()[0].tolist()
    
    cv.putText(img,str(text),(x,y), font, 1,(r,g,b),1)


# for i in range(10):
#     c = (color.__next__())
#     a = c[0]
