#!/usr/local/bin/pyenv python
# Created by carrot at 2018/6/24

"""
模版匹配
"""

import cv2 as cv
import numpy as np


def main():
    im = cv.imread('src.jpg')
    imgray = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
    t = cv.imread('src1.png', 0)
    w, h = t.shape[::-1]
    
    res = cv.matchTemplate(imgray, t, cv.TM_CCOEFF_NORMED)
    threshold = 0.6
    
    loc = np.where(res >= threshold)
    print(loc)
    print(len(loc[0]))
    print(zip(*loc[::-1]))
    count = 0
    for pt in zip(*loc[::-1]):
        count +=1
        cv.rectangle(im, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    print(count)
    cv.imwrite('mutl_match.png', im)


if __name__ == "__main__":
    main()
