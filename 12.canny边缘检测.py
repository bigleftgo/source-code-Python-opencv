#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2 as cv


#边缘检测述算法
def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)#高斯模糊
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)#转换为灰度图
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0) #16位整型，xy方向梯度
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)#50,150是高低阈值，在1:2或者1:3之间
    #edge_output=cv.Canny(gray,50,150)#不进行梯度计算也能进行canny计算
    cv.imshow("canny edge", edge_output)
    dst = cv.bitwise_and(image, image, mask=edge_output)#彩色，按位与
    cv.imshow("color edge", dst)


src = cv.imread("weld.png")
cv.namedWindow('input image',cv.WINDOW_NORMAL)
cv.imshow("input image", src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
