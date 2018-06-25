# -*- coding:utf-8 -*-

"""
Canny 边界检测
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


def hist1():
    img = cv2.imread('xiami.jpg')
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


def hist2():
    img = cv2.imread('xiami.jpg')
    color = ('r', 'g', 'b')

    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


if __name__ == "__main__":
    hist1()
    hist2()
