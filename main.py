#!/usr/local/bin/pyenv python
# -*- coding : utf-8 -*-
# Created by carrot at 2018/6/20

"""
"""

from gui import read
import cv2 as cv

src_file_name = './src.jpg'


def main():
    # read.read(src_file_name)
    # read.show2(src_file_name)
    # read.r_w(src_file_name)
    # read.plt_show(src_file_name)
    pass


if __name__ == "__main__":
    main()
    im = cv.imread('fb.jpg',0)
    print(im.shape)
    w, h = im.shape[::-1]
    print(w, h)
