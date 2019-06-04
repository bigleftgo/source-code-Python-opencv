#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv


#高斯金字塔
def pyramid_demo(image):
    level = 3#金字塔的层数
    temp = image.copy()#拷贝图像
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)#down是降采样-尺寸变小，分辨率降低（缩小）
        pyramid_images.append(dst)
        cv.imshow("pyramid"+str(i), dst)
        temp = dst.copy()
    return pyramid_images


#拉普拉斯金字塔，拉普拉斯金字塔时，图像大小必须是2的n次方*2的n次方，不然会报错
def laplian_demo(image):
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range(level-1, -1, -1):#每次递减
        if(i-1) < 0 :#最后一个，原图
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])#up是还原
            lpls = cv.subtract(image, expand)#原图减expand
            cv.imshow("lpls_down"+str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i-1].shape[:2])
            lpls = cv.subtract(pyramid_images[i-1], expand)
            cv.imshow("lpls_down"+str(i), lpls)



src = cv.imread("weld.png")
cv.namedWindow('input image',cv.WINDOW_NORMAL)
cv.imshow("input image", src)
#pyramid_images(src)
laplian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
