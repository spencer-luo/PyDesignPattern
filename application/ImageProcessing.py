#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 6/30/2018

import cv2
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class ImageProcessor(metaclass=ABCMeta):
    "图像处理的接口类"

    @abstractmethod
    def processing(self, img):
        "图像处理的抽象方法"
        pass

class EdgeExtractionProcessor(ImageProcessor):
    "边缘提取算法"

    def processing(self, img):
        super().processing(img)
        print("真正的核心算法:边缘提取算法")
        newImg = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)
        return newImg


class ImageDecorator(ImageProcessor):
    "图像装饰器"

    def __init__(self, processor):
        self._decorator = processor

    def processing(self, img):
        tmpImg = self.preProcessing(img)
        return self._decorator.processing(tmpImg)

    @abstractmethod
    def preProcessing(self, img):
        "预处理方法，由子类实现"
        pass


class GrayProcessor(ImageDecorator):
    "灰度化处理器"

    def __init__(self, processor):
        super().__init__(processor)

    def preProcessing(self, img):
        print("灰度化处理...")
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换了灰度化


class GradientProcessor(ImageDecorator):
    "梯度化处理器"

    def __init__(self, processor):
        super().__init__(processor)

    def preProcessing(self, img):
        print("梯度化处理...")
        x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
        y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
        absX = cv2.convertScaleAbs(x)  # 转回uint8
        absY = cv2.convertScaleAbs(y)
        return cv2.addWeighted(absX, 0.5, absY, 0.5, 0)


def testImageProcessing():
    img = cv2.imread("E:\\TestImages\\bird.jpg")
    print("灰度化 --> 梯度化 --> 核心算法:边缘提取算法：")
    resultImg1 = GrayProcessor(GradientProcessor(EdgeExtractionProcessor())).processing(img)
    print()

    print("梯度化 --> 灰度化 --> 核心算法:边缘提取算法：")
    resultImg2 = GradientProcessor(GrayProcessor(EdgeExtractionProcessor())).processing(img)
    print()

    cv2.imshow("The result of image process1", resultImg1)
    cv2.imshow("The result of image process2", resultImg2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

testImageProcessing()