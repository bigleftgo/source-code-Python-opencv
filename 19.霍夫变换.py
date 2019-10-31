#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#直线检测
#使用霍夫直线变换做直线检测，前提条件：边缘检测已经完成
import cv2 as cv
import numpy as np

#标准霍夫线变换
def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)  #apertureSize参数默认其实就是3
    cv.imshow("edges", edges)
    lines = cv.HoughLines(edges, 0.8, np.pi/360, 200)
    mask = np.zeros([600,800,3],np.uint8)
    for line in lines:
        rho, theta = line[0]  #line[0]存储的是点到直线的极径和极角，其中极角是弧度表示的。
        a = np.cos(theta)   #theta是弧度
        b = np.sin(theta)
        x0 = a * rho    #代表x = r * cos（theta）
        y0 = b * rho    #代表y = r * sin（theta）
        x1 = int(x0 + 1000 * (-b)) #计算直线起点横坐标
        y1 = int(y0 + 1000 * a)    #计算起始起点纵坐标
        x2 = int(x0 - 1000 * (-b)) #计算直线终点横坐标
        y2 = int(y0 - 1000 * a)    #计算直线终点纵坐标    注：这里的数值1000给出了画出的线段长度范围大小，数值越小，画出的线段越短，数值越大，画出的线段越长
        cv.line(mask, (x1, y1), (x2, y2), (0, 0, 255), 2)    #点的坐标必须是元组，不能是列表。
    # cv.namedWindow('image-lines', cv.WINDOW_NORMAL)
    cv.imshow("image-lines", mask)
    cv.imwrite("gooddad.png",mask)

# #统计概率霍夫线变换
# def line_detect_possible_demo(image):
#     gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
#     edges = cv.Canny(gray, 50, 150, apertureSize=3)  # apertureSize参数默认其实就是3
#     lines = cv.HoughLinesP(edges, 1, np.pi / 180, 60, minLineLength=60, maxLineGap=15)
#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
#     cv.imshow("line_detect_possible_demo",image)



def main():
    src = cv.imread('goodgirl.png')
    print(src.shape)
    # cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
    # cv.imshow('input_image', src)
    line_detection(src)
    src = cv.imread('goodson.png') #调用上一个函数后，会把传入的src数组改变，所以调用下一个函数时，要重新读取图片
    # line_detect_possible_demo(src)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':  # 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
    main()