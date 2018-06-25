# -*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('xiami.jpg', 0)

# 拉普拉斯算子
laplacian = cv2.Laplacian(img, cv2.CV_64F)
# sobel算子 x方向
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# sobel算子 y方向
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# scharr x方向
scharrX = cv2.Scharr(img, cv2.CV_64F, 1, 0)
# scharr算子 y方向
scharrY = cv2.Scharr(img, cv2.CV_64F, 0, 1)

imgs = [img, laplacian, sobelX, sobely, scharrX, scharrY]
titles = ["src", 'laplacian', 'sobelX', 'sobelY', 'scharrX', 'scharrY']

for i in range(len(imgs)):
    plt.subplot(3, 2, i + 1), plt.imshow(imgs[i], 'gray'), plt.title(titles[i]), plt.xticks([]), plt.yticks([])
plt.show()
