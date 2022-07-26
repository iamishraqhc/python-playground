import cv2
import numpy as np

img = cv2.imread('me.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

scale_percent = 20
width = int(cartoon.shape[1] * scale_percent / 100)
height = int(cartoon.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(cartoon, dim, interpolation=cv2.INTER_AREA)
resized2 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("Image", resized2)
cv2.imshow("Cartoon", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
