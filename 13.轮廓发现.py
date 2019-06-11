#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np


#轮廓发现
def contours_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)#二值图像
    cv.imshow("binary image", binary)
    contours,heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #找出轮廓：1二值图像，2,tree是所有轮廓;external是外层，3.simple获取重点像素的
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), -1)#绘制轮廓,第i个轮廓，1是thickness；-1是填充轮廓
        print(i)
    cv.imshow("detect contours", image)


#边缘检测加边缘轮廓提取
def Canny_edge_contours_demo(image):
    blurred=cv.GaussianBlur(image,(3,3),0)
    gray=cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    edge_output=cv.Canny(gray,50,150)
    cv.imshow('Canny Edge',edge_output)
    contours,heriachy = cv.findContours(edge_output, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #找出轮廓：1二值图像，2,tree是所有轮廓;external是外层，3.simple获取重点像素的
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)#绘制轮廓,第i个轮廓，1是thickness线宽，描轮廓；-1是填充轮廓
        print(i)
    cv.imshow("detect contours", image)



src = cv.imread("weld.png")
cv.namedWindow('input image',cv.WINDOW_NORMAL)
cv.imshow("input image", src)
Canny_edge_contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
