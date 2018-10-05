#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 4/6/2018

# Version 1.0
#=======================================================================================================================
# from abc import ABCMeta, abstractmethod
# # 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
#
# class Toy(metaclass=ABCMeta):
#     """玩具"""
#
#     def __init__(self, name):
#         self._name = name
#         self.__components = []
#
#     def getName(self):
#         return self._name
#
#     def addComponent(self, component, count = 1, unit = "个"):
#         self.__components.append([component, count, unit])
#         print("%s 增加了 %d %s%s" % (self._name, count, unit, component) );
#
#     @abstractmethod
#     def feature(self):
#         pass
#
#
# class Car(Toy):
#     """小车"""
#
#     def feature(self):
#         print("我是 %s，我可以快速奔跑……" % self._name)
#
#
# class Manor(Toy):
#     """庄园"""
#
#     def feature(self):
#         print("我是 %s，我可供观赏，也可用来游玩！" % self._name)
#
#
# class ToyBuilder:
#     """玩具构建者"""
#
#     def buildCar(self):
#         car = Car("迷你小车")
#         print("正在构建 %s ……" % car.getName())
#         car.addComponent("轮子", 4)
#         car.addComponent("车身", 1)
#         car.addComponent("发动机", 1)
#         car.addComponent("方向盘")
#         return car
#
#     def buildManor(self):
#         manor = Manor("淘淘小庄园")
#         print("正在构建 %s ……" % manor.getName())
#         manor.addComponent('客厅', 1, "间")
#         manor.addComponent('卧室', 2, "间")
#         manor.addComponent("书房", 1, "间")
#         manor.addComponent("厨房", 1, "间")
#         manor.addComponent("花园", 1, "个")
#         manor.addComponent("围墙", 1, "堵")
#         return manor
#
#
# # Test
# #==============================
# def testBuilder():
#     builder = ToyBuilder()
#     car = builder.buildCar()
#     car.feature()
#
#     print()
#     mannor = builder.buildManor()
#     mannor.feature()




# Version 2.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Toy(metaclass=ABCMeta):
    """玩具"""

    def __init__(self, name):
        self._name = name
        self.__components = []

    def getName(self):
        return self._name

    def addComponent(self, component, count = 1, unit = "个"):
        self.__components.append([component, count, unit])
        # print("%s 增加了 %d %s%s" % (self._name, count, unit, component) );

    @abstractmethod
    def feature(self):
        pass


class Car(Toy):
    """小车"""

    def feature(self):
        print("我是 %s，我可以快速奔跑……" % self._name)


class Manor(Toy):
    """庄园"""

    def feature(self):
        print("我是 %s，我可供观赏，也可用来游玩！" % self._name)


class ToyBuilder(metaclass=ABCMeta):
    """玩具构建者"""

    @abstractmethod
    def buildProduct(self):
        pass


class CarBuilder(ToyBuilder):
    """车的构建类"""

    def buildProduct(self):
        car = Car("迷你小车")
        print("正在构建 %s ……" % car.getName())
        car.addComponent("轮子", 4)
        car.addComponent("车身", 1)
        car.addComponent("发动机", 1)
        car.addComponent("方向盘")
        return car


class ManorBuilder(ToyBuilder):
    """庄园的构建类"""

    def buildProduct(self):
        manor = Manor("淘淘小庄园")
        print("正在构建 %s ……" % manor.getName())
        manor.addComponent('客厅', 1, "间")
        manor.addComponent('卧室', 2, "间")
        manor.addComponent("书房", 1, "间")
        manor.addComponent("厨房", 1, "间")
        manor.addComponent("花园", 1, "个")
        manor.addComponent("围墙", 1, "堵")
        return manor

class BuilderMgr:
    """建构类的管理类"""

    def __init__(self):
        self.__carBuilder = CarBuilder()
        self.__manorBuilder = ManorBuilder()

    def buildCar(self, num):
        count = 0
        products = []
        while(count < num):
            car = self.__carBuilder.buildProduct()
            products.append(car)
            count +=1
            print("建造完成第 %d 辆 %s" % (count, car.getName()) )
        return products

    def buildManor(self, num):
        count = 0
        products = []
        while (count < num):
            manor = self.__manorBuilder.buildProduct()
            products.append(manor)
            count += 1
            print("建造完成第 %d 个 %s" % (count, manor.getName()))
        return products


# Test
# ==============================
def testAdvancedBuilder():
    builderMgr = BuilderMgr()
    builderMgr.buildManor(2)
    print()
    builderMgr.buildCar(4)


# testBuilder()
testAdvancedBuilder()
