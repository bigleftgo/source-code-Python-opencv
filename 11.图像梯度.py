#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np
#sobel算子
def sobel_image(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)#x方向导数，32位浮点数，防止计算超出255，无法正确显示结果
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)#y方向导数
    gradx = cv.convertScaleAbs(grad_x)#把求出为负数的导数取绝对值，然后转回到8位灰度图像
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x", gradx)#颜色变化在水平分层，x方向梯度
    cv.imshow("gradient-y", grady)#颜色变化在垂直分层
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient", gradxy)


#图像梯度：scharr算子：增强边缘,增强sobel
def scharr_image(image):
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)#x方向导数
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)#y方向导数
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x", gradx)#颜色变化在水平分层
    cv.imshow("gradient-y", grady)#颜色变化在垂直分层
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient", gradxy)


#拉普拉斯算子
def lapalian_image(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian_demo", lpls)

#自定义拉普拉斯算子
def lapalian_customize_image(image):
    kernel=np.array([0,1,0],[1,-4,1],[0,1,0])#二维，3*3,拉普拉斯默认4领域；[1,1,1],[1,-8,1],[1,1,1]
    dst=cv.filter2D(image,cv.CV_32F,kernel=kernel)
    lpls=cv.convertScaleAbs(dst)
    cv.imshow("lapalian_demo", lpls)


src = cv.imread("weld.png")
cv.namedWindow('input image',cv.WINDOW_NORMAL)
cv.imshow("input image", src)
#sobel_image(src)
#scharr_image(src)
lapalian_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
