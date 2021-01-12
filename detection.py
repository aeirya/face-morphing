from imutils import face_utils
from dlib import get_frontal_face_detector, shape_predictor
import cv2 as cv
from drawing import draw_point, draw_text

path = "shape_predictor_68_face_landmarks.dat"
detector = get_frontal_face_detector()
predictor = shape_predictor(path)

def detect_facial_landmarks(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = detector(gray, 0)
    points = []

    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        for pt in shape:
            points.append((pt[0], pt[1]))
    
    return points

def draw_facial_landmarks(img, with_text = False):
    img = img.copy()
    shape = detect_facial_landmarks(img)
    i = 0
    for (x, y) in shape:
        draw_point(img, x,y)
        if with_text:
            draw_text(img, x,y,i)
        i += 1
    return img

# img = cv.imread("w1.jpg")
# img = draw_facial_landmarks(img, with_text=True)
# cv.imwrite("detect1.jpg", img)