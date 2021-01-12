from scipy.spatial import Delaunay
import cv2 as cv
import numpy as np

def co_triangulate(points0, points1):
    tri = Delaunay(points0)
    sim = tri.simplices.astype(np.int)
    return points0[sim], points1[sim]

# not used anymore
def trangulate(img, points):
    height, width = img.shape[:2]
    rect_bound = [0,0, width, height]
    sub = cv.Subdiv2D(rect_bound)
    for pt in points:
        sub.insert(pt)
    triangles = sub.getTriangleList()
    h,w = triangles.shape
    return triangles.reshape((h, w//2, 2)).astype('int32')


# archived
##

# points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
# tri = Delaunay(points)

# import matplotlib.pyplot as plt
# plt.triplot(points[:,0], points[:,1], tri.simplices)
# plt.plot(points[:,0], points[:,1], 'o')


# for j, p in enumerate(points):
#     plt.text(p[0]-0.03, p[1]+0.03, j, ha='right') # label the points
# for j, s in enumerate(tri.simplices):
#     p = points[s].mean(axis=0)
#     plt.text(p[0], p[1], '#%d' % j, ha='center') # label triangles
# plt.xlim(-0.5, 1.5); plt.ylim(-0.5, 1.5)
# plt.show()
