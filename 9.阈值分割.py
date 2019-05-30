#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np


#图像二值化 0白色 1黑色
#全局阈值
def threshold_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #cv.imshow("原来", gray)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    #二值化，OTSU方法，大律法,在otsu全局自适应阈值，参数0可改为任意数字但不起作用
    print("threshold value：%s" % ret)#显示阈值
    cv.imshow("OTSU", binary)

    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    #TRIANGLE法,，全局自适应阈值, 参数0可改为任意数字但不起作用，适用于单个波峰
    print("threshold value：%s" % ret)
    cv.imshow("TRIANGLE", binary)#TRIANGLE方法

    ret, binary = cv.threshold(gray, 60, 255, cv.THRESH_BINARY)
    # 自定义阈值为150,大于150的是白色 小于的是黑色
    print("threshold value：%s" % ret)
    cv.imshow("binary", binary)

    ret, binary = cv.threshold(gray, 60, 255, cv.THRESH_BINARY_INV)
    # 反了，自定义阈值为150,大于150的是黑色 小于的是白色
    print("threshold value：%s" % ret)
    cv.imshow("invert color", binary)

    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TRUNC)
    # 截断 大于150的是改为150  小于150的保留
    print("threshold value：%s" % ret)
    cv.imshow("cut1", binary)

    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TOZERO)
    # 截断 小于150的是改为150  大于150的保留
    print("threshold value：%s" % ret)
    cv.imshow("cut2", binary)


src = cv.imread("weld.png")
cv.namedWindow('input image',cv.WINDOW_NORMAL)
cv.imshow("input image", src)
threshold_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
