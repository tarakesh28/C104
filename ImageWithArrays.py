import cv2
import numpy as np

black = np.zeros([600,600])
#f_row = black[1:2]
#print(f_row)
black[200:400,200:400] = 255
cv2.imshow("Image2", black)
print(black)

cv2.waitKey(0)
#f_col = black[:,1:2]
#print(f_col)
