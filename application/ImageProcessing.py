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



# 一阶微分算子
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
import numpy as np
# 引入numpy模块进行矩阵的计算

class DifferentialDerivative(metaclass=ABCMeta):
    """微分求导算法"""

    def imgProcessing(self, img, width, height):
        """模板方法，进行图像处理"""
        # 这里特别需要注意：OpenCv for Python中，(x, y)坐标点的像素用img[y, x]表示
        newImg = np.zeros([height, width], dtype=np.uint8)
        for y in range(0, height):
            for x in range(0, width):
                # 因为是采用(3*3)的核进行处理，所以最边上一圈的像素无法处理，需保留原值
                if (y != 0 and y != height-1 and x != 0 and x != width-1):
                    value = self.derivation(img, x, y)
                    # 小于0的值置为0，大于255的值置为255
                    value = 0 if value < 0 else (255 if value > 255 else value)
                    newImg[y, x] = value
                else:
                    newImg[y, x] = img[y, x]
        return newImg

    @abstractmethod
    def derivation(self, img, x, y):
        """具体的步骤由子类实现"""
        pass

class DifferentialDerivativeX(DifferentialDerivative):
    """水平微分求导算法"""

    def derivation(self, img, x, y):
        """Gx=f(x-1,y-1) + 2f(x-1,y) + f(x-1,y+1) - f(x+1,y-1) - 2f(x+1,y) - f(x+1, y+1)"""
        pix = img[y-1, x-1] + 2 * img[y, x-1] + img[y+1, x-1] - img[y-1, x+1] - 2 *img[y, x+1] - img[y+1, x+1]
        return pix


class DifferentialDerivativeY(DifferentialDerivative):
    """垂直微分求导算法"""

    def derivation(self, img, x, y):
        """Gy=f(x-1,y-1) + 2f(x,y-1) + f(x+1,y-1) - f(x-1,y+1) - 2f(x,y+1) - f(x+1,y+1)"""
        pix = img[y-1, x-1] + 2*img[y-1, x] + img[y-1, x+1] - img[y+1, x-1] - 2*img[y+1, x] - img[y+1, x+1]
        return pix


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

def differentialDerivativeOpenCv():
    img = cv2.imread("E:\\TestImages\\person.jpg")

    # 转换成单通道灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
    # 进行微分计算后，可能会出现负值，将每个像素加上最小负数的绝对值
    absX = cv2.convertScaleAbs(x)  # 转回uint8
    absY = cv2.convertScaleAbs(y)
    # img = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    cv2.imshow("First order differential X", absX)
    cv2.imshow("First order differential Y", absY)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def differentialDerivative():
    img = cv2.imread("E:\\TestImages\\person.jpg")

    # 转换成单通道的灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 均值滤波
    # img = cv2.blur(img, (3, 3))

    # 获取图片的宽和高
    width = img.shape[1]
    height = img.shape[0]
    # 进行微分求导
    derivativeX = DifferentialDerivativeX()
    imgX = derivativeX.imgProcessing(img, width, height)
    derivativeY = DifferentialDerivativeY()
    imgY = derivativeY.imgProcessing(img, width, height)
    # 实现Sobel微分算子
    imgScobel = cv2.addWeighted(imgX, 0.5, imgY, 0.5, 0)

    cv2.imshow("First order differential X", imgX)
    cv2.imshow("First order differential Y", imgY)
    cv2.imshow("First order differential Scobel", imgScobel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# testImageProcessing()
# differentialDerivativeOpenCv()
differentialDerivative()

