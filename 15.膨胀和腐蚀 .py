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


def gray_erode_demo(image):#灰度图腐蚀
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))#MORPH_RECT矩形结构元
    dst = cv.erode(image, kernel=kernel)#腐蚀
    cv.imshow("gray_erode_demo", dst)


def dilate_demo(image):#二值图膨胀
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.dilate(binary, kernel=kernel)
    cv.imshow("dilate_demo", dst)


def gray_dilate_demo(image):#二值图膨胀
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.dilate(image, kernel=kernel)
    cv.imshow("gray_dilate_demo", dst)


def main():
    src = cv.imread("weld.png")
    cv.namedWindow('input image',cv.WINDOW_NORMAL)
    cv.imshow("input image", src)
    gray_erode_demo(src)
    gray_dilate_demo(src)
    # erode_demo(src)
    # dilate_demo(src)
    cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口
    cv.destroyAllWindows()  # 关闭所有窗口


if __name__ == '__main__':#cam.py 为true
    main()#测试时候加上main()
