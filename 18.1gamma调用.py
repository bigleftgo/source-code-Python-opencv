#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np

def gamma_image(image):
    img1 = np.power(image/float(np.max(image)), 1/2.3)
    img2 = np.power(image/float(np.max(image)), 1/1.5)
    cv.imshow('gamma=1/2.3',img1)
    cv.imshow('gamma=1/1.5',img2)

def main():
    src = cv.imread('hanji.png',0)
    cv.imshow("input image", src)
    gamma_image(src)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':  # 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
    main()