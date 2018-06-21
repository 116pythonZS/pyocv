#!/usr/local/bin/pyenv python
# -*- coding : utf-8 -*-
# Created by carrot at 2018/6/20

"""
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


def read(filename):
    im = cv2.imread(filename, 0)
    print(im.shape)


def show(filename):
    img = cv2.imread(filename, 0)
    cv2.imshow("WindowName", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show2(filename):
    img = cv2.imread(filename, 0)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyWindow('image')


def r_w(filename):
    img = cv2.imread(filename, 0)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('new.jpg', img)
        cv2.destroyAllWindows()


def plt_show(filename):
    img = cv2.imread(filename, 0)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()
