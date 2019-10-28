#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np

"""
开运算:先进性腐蚀再进行膨胀就叫做开运算,它被用来去除噪声。
闭运算:先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点。
这里我们用到的函数是 cv2.morphologyEx()。
开闭操作作用：
1. 去除小的干扰块-开操作
2. 填充闭合区间-闭操作
3. 水平或垂直线提取,调整kernel的row，col值差异。
比如：采用开操作，kernel为(1, 15),提取垂直线，kernel为(15, 1),提取水平线，
"""

"""
其他形态学操作：
顶帽：原图像与开操作之间的差值图像
黑帽：比操作与原图像直接的差值图像
形态学梯度：其实就是一幅图像膨胀与腐蚀的差别。 结果看上去就像前景物体的轮廓
基本梯度：膨胀后图像减去腐蚀后图像得到的差值图像。
内部梯度：用原图减去腐蚀图像得到的差值图像。
外部梯度：膨胀后图像减去原图像得到的差值图像。
"""


def binary_open_demo(image):  # 二值图开操作去噪点
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 二值图像
    cv.imshow("binary", binary)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 矩形结构元
    dst = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel=kernel)
    cv.imshow("open_demo", dst)


def Gray_open_demo(image):  # 灰度图开操作去噪点
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))  # 矩形结构元
    dst = cv.morphologyEx(image, cv.MORPH_OPEN, kernel=kernel)
    cv.imshow("gray_open_demo", dst)


def close_demo(image):  # 二值图闭，弥补黑洞
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel=kernel)
    cv.imshow("open_demo", dst)


def gray_close_demo(image):  # 灰度图闭操作，弥补黑洞
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel=kernel)
    cv.imshow("gray_Close_demo", dst)


def tophat_morphology_demo(image): #顶帽操作
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel=kernel)
    cimg = np.array(gray.shape, np.uint8)
    cimg = 100#像素值加100
    dst = cv.add(dst, cimg)
    cv.imshow("top_hat_demo", dst)


def blackHat_morphology_demo(image): #黑帽操作
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel=kernel)
    cimg = np.ones(gray.shape, np.uint8)*100#构造数组
    dst = cv.add(dst, cimg)
    cv.imshow("BLACK_hat_demo", dst)


def main():
    src = cv.imread("weld.png")
    cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    # open_demo(src)
    # Gray_open_demo(src)
    # gray_close_demo(src)
    # close_demo(src)
    #tophat_morphology_demo(src)
    blackHat_morphology_demo(src)
    cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口
    cv.destroyAllWindows()  # 关闭所有窗口


if __name__ == '__main__':  # 插入到其他程序  （开闭操作.py） 在当前程序为true，在其他程序中为false，就只运行之前的程序
    main()  # 测试时候加上main()
