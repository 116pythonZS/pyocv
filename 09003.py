# -*- coding:utf-8 -*-

import cv2
import numpy as np 

img1 = cv2.imread('clock.png')
img2 = cv2.imread('football.jpg')
print('img1.shape = ', img1.shape)
print('img2.shape = ', img2.shape)

dst = cv2.addWeighted(img1, 0.3, img2, 0.,0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()