#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np


def erode_demo(image):#二值图腐蚀
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))#MORPH_RECT矩形结构元
    dst = cv.erode(binary, kernel=kernel)#腐蚀
    cv.imshow("erode_demo", dst)


def dilate_demo(image):#二值图膨胀
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.dilate(binary, kernel=kernel)
    cv.imshow("dilate_demo", dst)



src = cv.imread("weld.png")
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)#NORMAL
cv.imshow("input image", src)
#erode_demo(src)
#dilate_demo(src)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
dst = cv.dilate(src, kernel=kernel)#灰度图膨胀
#dst = cv.erode(src, kernel=kernel)
cv.imshow("dilate", dst)
cv.waitKey(0)
cv.destroyAllWindows()
