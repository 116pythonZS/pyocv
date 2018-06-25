# -*- coding:utf-8 -*-

"""
Canny 边界检测
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('xiami.jpg', 0)
im = img.copy()
imgs = [im]
for i in range(5):
    im = cv2.pyrUp(im)
    # cv2.imwrite("./up_%d.jpg" %i, im)
    imgs.append(im)

for idx in range(len(imgs)):
    plt.subplot(1, len(imgs), idx + 1), plt.imshow(imgs[idx], 'gray'), plt.title('src_%d' % idx), plt.xticks(
            []), plt.yticks([])
plt.show()
