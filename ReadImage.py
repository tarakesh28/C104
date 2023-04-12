import cv2
import numpy

img = cv2.imread("butterfly.jpg")

grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow("Grayscale", grayImg)
#print(img)

#
cv2.waitKey(3000)