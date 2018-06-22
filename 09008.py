# -*- coding:utf-8 -*-

"""
Canny 边界检测
"""
import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('xiami.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(1,2,1),plt.imshow(img,'gray'),plt.title('src'),plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(edges,'gray'),plt.title('dege'),plt.xticks([]), plt.yticks([])
plt.show()