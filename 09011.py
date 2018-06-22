# -*- coding:utf-8 -*-

"""
Canny 边界检测
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
直方图均衡化
"""


def hist_equalization_numpy():
	img = cv2.imread('xiami.jpg')
	# 灰度
	imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	# flatten() 将数组变成一维
	hist, bins = np.histogram(imgGray.flatten(), 256, [0, 256]);
	# 计算累计分布图
	cdf = hist.cumsum()
	cdf_normalized = cdf * hist.max() / cdf.max()

	# 构建Numpy掩模数组, cdf 为原始数组, 当数组元素为0时, 掩盖(计算时被忽略)
	cdf_m = np.ma.masked_equal(cdf, 0)
	cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
	# 对被掩盖的元素赋值, 这里赋值为0
	cdf2 = np.ma.filled(cdf_m, 0).astype('uint8')
	img2 = cdf2[imgGray]

	plt.subplot(1, 2, 1), plt.imshow(img2), plt.xticks([]), plt.yticks([])

	plt.subplot(1, 2, 2),
	# plt.plot(cdf_normalized, color='b')
	plt.plot(cdf_m, color = 'b')
	plt.hist(img2.flatten(), 256, [0, 256], color = 'r')
	plt.xlim(0, 256)
	plt.legend(('cdf', 'histogram'), loc = 'upper left')
	plt.show()


def hist_equalize_opencv():
	img = cv2.imread('xiami.jpg', 0)
	equ = cv2.equalizeHist(img)
	res = np.hstack((img, equ))
	cv2.imwrite('xiami_equalizeHist.jpg', res)


# CLAHE 算法
def hist_equalize_opencv_clahe():
	img = cv2.imread('xiami.jpg', 0)
	equ = cv2.equalizeHist(img)
	clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
	claheImg = clahe.apply(img)
	res = np.hstack((img, equ, claheImg))
	cv2.imwrite('xiami_equalizeHist_2.jpg', res)
	cv2.matchTemplate()


if __name__ == "__main__":
	# hist_equalization_numpy()
	# hist_equalize_opencv()
	hist_equalize_opencv_clahe()
