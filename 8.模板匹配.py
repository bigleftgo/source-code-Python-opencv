#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np


#模版匹配
def template_image():
    tpl = cv.imread("tpl.png")
    target = cv.imread("weld.png")
    cv.imshow("template image", tpl)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    #三种方法：0到1,平方；相关性比较；相关性因子
    th, tw = tpl.shape[:2]#高；宽
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)#md是方法
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)#匹配的最大值和最小值
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc#1SQDIFF方法，最小值是匹配区域，tl是左上角坐标；3找最大；5找最大
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)#br是右下角
        cv.rectangle(target, tl, br, (0, 0, 255), 2)#红色，2是线宽度
        cv.imshow("match-"+np.str(md), target)#
        #cv.imshow("match-"+np.str(md), result)


src = cv.imread("weld.png")
cv.namedWindow('input image',cv.WINDOW_NORMAL)
cv.imshow("input image", src)
template_image()
cv.waitKey(0)
cv.destroyAllWindows()
