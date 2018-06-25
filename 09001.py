# -*- coding:utf-8 -*-

import cv2
import numpy as np


def demo1():
    img = cv2.imread('index@2x.png')
    px = img[100, 100]
    print(px)
    blue = img[100, 100, 0]
    gree = img[100, 100, 1]
    red = img[100, 100, 2]
    print(blue)
    print(gree)
    print(red)
    img[100, 100,] = [0, 0, 0]
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def demo2():
    img = cv2.imread('index@2x.png')
    img.itemset((10, 10, 2), 0)
    img.itemset((10, 10, 1), 0)
    img.itemset((10, 10, 0), 0)
    print(img.shape)
    print(img.size)  # h*w
    print(img.dtype)


# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def demo3():
    img = cv2.imread('./roi.jpeg')
    ball = img[83:142, 362:418]
    rows, cols, channels = ball.shape
    img[283:342, 362:428] = ball
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def demo4():
    img = cv2.imread('./roi.jpeg')
    cv2.imshow('image1', img)

    b, g, r = cv2.split(img)
    img2 = cv2.merge((b, g, r))
    cv2.imshow('image2', img2)
    img3 = cv2.merge((b, g, r))
    img3[:, :, 2] = 0
    cv2.imshow('image3', img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # demo1()
    # demo2()
    demo3()
# demo4()
