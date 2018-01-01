#!/usr/bin/python
# Authoer: Administrator
# Date: 12/2/2017

# Version 1.0
#=======================================================================================================================

class Coffee:
    "咖啡"

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getTaste(self):
        pass


class CaffeLatte(Coffee):
    "拿铁咖啡"

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "轻柔而香醇。"

class MochaCoffee(Coffee):
    "摩卡咖啡"

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "丝滑与醇厚。"

class Coffeemaker:
    "咖啡机"

    @staticmethod
    def makeCoffee(coffeeBean):
        coffee = None
        if(coffeeBean == "拿铁风味咖啡豆"):
            coffee = CaffeLatte("拿铁咖啡")
        elif(coffeeBean == "摩卡风味咖啡豆"):
            coffee = MochaCoffee("摩卡咖啡")
        else:
            coffee = Coffee()
        return coffee



# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================

from enum import Enum
# Python3.4 之后支持枚举Enum的语法

class PenType(Enum):
    "画笔类型"
    PenTypeLine = 1
    PenTypeRect = 2
    PenTypeEllipse = 3


class Pen:
    "画笔"

    def __init__(self, name):
        self.__name = name

    def getType(self):
        pass

    def getName(self):
        return self.__name


class LinePen(Pen):
    "直线画笔"

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeLine

class RectanglePen(Pen):
    "矩形画笔"

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeRect


class EllipsePen(Pen):
    "椭圆画笔"

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeEllipse


class PenFactory:
    "画笔工厂类"

    def __init__(self):
        "定义一个字典(key:PenType，value：Pen)来存放对象,确保每一个类型只会有一个对象"
        self.__pens = {}

    def getSingleObj(self, penType, name):
        "获得唯一实例的对象"
        if (self.__pens.get(penType) is None):
            # 如果该对象不存在，则创建一个对象并存到字典中
            self.__pens[penType] = LinePen(name)
        # 否则直接返回字典中的对象
        return self.__pens[penType]

    def createPen(self, penType):
        "创建画笔"
        # Python中没有switch/case的语法，我们通过字典来来模拟switch/case的实现方式
        switcher = {
            PenType.PenTypeLine : self.getSingleObj(PenType.PenTypeLine, "直线画笔"),
            PenType.PenTypeRect : self.getSingleObj(PenType.PenTypeRect, "矩形画笔"),
            PenType.PenTypeEllipse : self.getSingleObj(PenType.PenTypeEllipse, "椭圆画笔"),
        }
        return switcher.get(penType, "create pen error")


# 基于框架的实现
#==============================


# Test
#=======================================================================================================================
def testCoffeeMaker():
    latte = Coffeemaker.makeCoffee("拿铁风味咖啡豆")
    print(latte.getName(), "已为您准备好了，口感：" + latte.getTaste() + "请慢慢享用！")
    mocha = Coffeemaker.makeCoffee("摩卡风味咖啡豆")
    print(mocha.getName(), "已为您准备好了，口感：" + mocha.getTaste() + "请慢慢享用！")


def testPenFactory():
    factory = PenFactory()
    linePen = factory.createPen(PenType.PenTypeLine)
    print("创建了 " + linePen.getName() + ", 对象id：" + str(id(linePen)))
    rectPen = factory.createPen(PenType.PenTypeRect)
    print("创建了 " + rectPen.getName() + ", 对象id："+ str(id(rectPen)))
    rectPen2 = factory.createPen(PenType.PenTypeRect)
    print("创建了 " + rectPen2.getName() + ", 对象id：" + str(id(rectPen2)))
    ellipsePen = factory.createPen(PenType.PenTypeEllipse)
    print("创建了 " + ellipsePen.getName() + ", 对象id：" + str(id(ellipsePen)))


# testCoffeeMaker()
testPenFactory()