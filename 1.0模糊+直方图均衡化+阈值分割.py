#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np


def mo_image(src1):
    src2 = cv.medianBlur(src1, 3)
    cv.namedWindow('medianblur',0)
    #cv.imwrite('m1.jpg',src2)
    cv.imshow("medianblur", src2)
    return src2


def clahe_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))#clipLimit是对比度的大小，tileGridSize是每次处理块的大小
    dst = clahe.apply(gray)
    cv.imshow("customize", dst)
    return dst


def threshold_image(image):
    #gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #cv.imshow("原来", gray)
    ret, binary = cv.threshold(image, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    #二值化，OTSU方法，大律法,在otsu全局自适应阈值，参数0可改为任意数字但不起作用
    print("threshold value：%s" % ret)#显示阈值
    cv.imshow("OTSU", binary)

    ret, binary = cv.threshold(image, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    #TRIANGLE法,，全局自适应阈值, 参数0可改为任意数字但不起作用，适用于单个波峰
    print("threshold value：%s" % ret)
    cv.imshow("TRIANGLE", binary)#TRIANGLE方法

    ret, binary = cv.threshold(image, 60, 255, cv.THRESH_BINARY)
    # 自定义阈值为150,大于150的是白色 小于的是黑色
    print("threshold value：%s" % ret)
    cv.imshow("binary", binary)


src = cv.imread("weld.png")
cv.namedWindow('input image',cv.WINDOW_NORMAL)
cv.imshow("input image", src)
src1=mo_image(src)
src2=clahe_image(src1)
cv.imshow('src2',src2)
threshold_image(src2)
cv.waitKey(0)
cv.destroyAllWindows()