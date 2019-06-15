#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np


def mesure_object(image):  # 测量对象，有没有超过精度要求；边界矩形
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)#otsu是直方图中有两个峰
    #二值化，黑色轮廓
    #0是阈值，255maxval
    #THRESH_BINARY过阈值设置为maxval，其他值为零；THRESH_BINARY_INV过阈值设置为零，其他值为maxval
    print('threshold value:%s' % ret)
    cv.imshow('binary image', binary)
    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # python4.0只返回两个值
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)  # 第i个轮廓面积
        x,y,w,h = cv.boundingRect(contour)  # 直(没有旋转)边界矩形
        rate=min(w,h)/max(w,h)#宽高比
        print('rectangle rate:%s'%rate)
        mm = cv.moments(contour)  # moments中心矩，可以求面积、质心
        print(type(mm))#是字典
        # 求质心
        if mm['m00'] == 0:
            continue
        else:
            cx = mm['m10']/mm['m00']
            cy = mm['m01']/mm['m00']
        cv.circle(image, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)  #绘制质心， 3是半径，-1填充
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2) # 绘制边界矩形
        print('contour area :%s' %area)
        approxCurve=cv.approxPolyDP(contour,4,True)#轮廓近似
    cv.imshow('measure contours',image)


def mesure_different_object(image):  # 测量矩形，圆，三角形；轮廓近似
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)#otsu是直方图中有两个峰
    #二值化，黑色轮廓
    #0是阈值，255maxval
    #THRESH_BINARY过阈值设置为maxval，其他值为零；THRESH_BINARY_INV过阈值设置为零，其他值为maxval
    print('threshold value:%s' % ret)
    cv.imshow('binary image', binary)
    dst=cv.cvtColor(binary,cv.COLOR_GRAY2BGR)#gray to bgr
    contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # python4.0只返回两个值
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)  # 第i个轮廓面积
        x,y,w,h = cv.boundingRect(contour)  # 直(没有旋转)边界矩形
        rate=min(w,h)/max(w,h)#宽高比
        print('rectangle rate:%s'%rate)
        mm = cv.moments(contour)  # moments中心矩，可以求面积、质心
        print(type(mm))#是字典
        # 求质心
        if mm['m00'] == 0:
            continue
        else:
            cx = mm['m10']/mm['m00']
            cy = mm['m01']/mm['m00']

        cv.circle(dst, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)  #绘制质心， 3是半径，-1填充
        cv.rectangle(dst,(x,y),(x+w,y+h),(0,0,255),2) # 绘制边界矩形
        print('contour area :%s' %area)
        approxCurve=cv.approxPolyDP(contour,4,True)#轮廓近似
        print(approxCurve.shape)
        if approxCurve.shape[0]>6:#寻找曲线6条线画出来的
            cv.drawContours(dst,contours,i,(0,255,0),2)
        if approxCurve.shape[0]==4:#寻找曲线4条线画出来的
            cv.drawContours(dst,contours,i,(0,0,255),2)
    cv.imshow('measure contours',image)



src = cv.imread("weld.png")
cv.namedWindow('input image', cv.WINDOW_NORMAL)
cv.imshow("input image", src)
mesure_object(src)
cv.waitKey(0)
cv.destroyAllWindows()
