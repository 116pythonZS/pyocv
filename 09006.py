# -*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('xiami.jpg', 0)

# 双边滤波
img2 = cv2.bilateralFilter(img, 9, 75, 75)
# 高斯模糊
img3 = cv2.GaussianBlur(img, (5, 5), 0)

plt.subplot(1, 3, 1), plt.imshow(img, 'gray'), plt.title('src'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(img2, 'gray'), plt.title('bilater'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(img3, 'gray'), plt.title('gauss'), plt.xticks([]), plt.yticks([])
plt.show()
