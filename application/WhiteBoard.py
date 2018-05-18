#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 4/21/2018

# Version 1.0
#=======================================================================================================================
from enum import Enum
# Python3.4 之后支持枚举Enum的语法

class ShapeType(Enum):
    "形状类型"
    ShapeTypeLine = 1
    ShapeTypeRect = 2
    ShapeTypeEllipse = 3


class Shape:
    "形状"

    def __init__(self, name):
        self.__name = name

    def getType(self):
        pass

    def getName(self):
        return self.__name


class Line(Shape):
    "直线"

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return ShapeType.ShapeTypeLine

class Rectangle(Shape):
    "矩形"

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return ShapeType.ShapeTypeRect


class Ellipse(Shape):
    "椭圆"

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return ShapeType.ShapeTypeEllipse

class ShapeFactory:
    "形状的工厂类"

    @staticmethod
    def createShape(self, type):
        pass

    def createPen(self, penType):
        "创建形状"
        # Python中没有switch/case的语法，我们通过字典来来模拟switch/case的实现方式
        switcher = {
            ShapeType.ShapeTypeLine : Line("直线"),
            ShapeType.ShapeTypeRect : Rectangle("矩形"),
            ShapeType.ShapeTypeEllipse : Ellipse("椭圆"),
        }
        return switcher.get(penType, "create pen error")

class ShapeType(Enum):
    "形状类型"
    ColorRed = 1
    ColorGreen = 2
    ColorBlue = 3

class Color:
    "颜色"

    def __init__(self, value):
        self.__value = value

    def getType(self):
        pass

# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================


# 基于框架的实现
#==============================


# Test
#=======================================================================================================================

