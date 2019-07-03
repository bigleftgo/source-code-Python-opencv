#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2 as cv
import numpy as np


# 分水岭算法
def water_image(image):
    print(image.shape)
    blurred = cv.pyrMeanShiftFiltering(image, 10, 100)  # 去除噪点

    # gray\binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 自动阈值
    cv.imshow("binary", binary)

    # morphology operation 把小孔洞填上
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))#矩形
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)#连续两次开操作，iterations迭代次数
    sure_bg = cv.dilate(mb, kernel, iterations=3)#连续3次腐蚀
    cv.imshow("morphology operation", sure_bg)

    # distance transform
    dist = cv.distanceTransform(mb, cv.DIST_L2, 5)#L2是欧几里得距离计算，掩膜大小为3×3
    dist_output = cv.normalize(dist, 0, 255, cv.NORM_MINMAX)#把dist的数组归一到0到1之间
    cv.imshow("dist_transform", dist_output *100)

    ret, surface = cv.threshold(dist, dist.max() * 0.1, 255, cv.THRESH_BINARY)#标记最亮的地方,然后二值化
    cv.imshow("surface-bin", surface)

    surface_fg = np.uint8(surface)#把浮点数转化为整型
    unknown = cv.subtract(sure_bg, surface_fg)#总减surface，unknown定义未知区域，连接区域
    ret, markers = cv.connectedComponents(surface_fg)#标记好了连接区域
    print(ret)

    # watershed transfrom,numpy操作
    markers += 1#确保背景是1不是0
    markers[unknown == 255] = 0#未知区域为0
    markers = cv.watershed(image, markers=markers)
    image[markers == -1] = [0, 0, 255]#红色
    cv.imshow("result", image)


def main():
    src = cv.imread("coin.jpg")#coin.jpg weld.png
    cv.imshow("input image", src)
    water_image(src)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':  # 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
    main()
