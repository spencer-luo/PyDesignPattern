#!/usr/bin/python
# Authoer: Administrator
# Date: 4/24/2018

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Chef(metaclass=ABCMeta):
    "厨师"

    @abstractmethod
    def cooking(self, originalMaterial):
        pass


class SteamedChef(Chef):
    "清蒸大厨"

    def cooking(self, originalMaterial):
        print(originalMaterial + "清蒸中...")
        return "清蒸" + originalMaterial


class StirFriedChef(Chef):
    "爆炒大厨"

    def cooking(self, originalMaterial):
        print(originalMaterial + "爆炒中...")
        return "香辣炒" + originalMaterial


class Order(metaclass=ABCMeta):
    "订单"

    def __init__(self, originalMaterial):
        self._chef = None
        self._originalMaterial = originalMaterial

    @abstractmethod
    def processingOrder(self):
        pass

class SteamedOrder(Order):
    "清蒸"

    def __init__(self, originalMaterial):
        super().__init__(originalMaterial)
        self._chef = SteamedChef()

    def processingOrder(self):
        if(self._chef is not None):
            return self._chef.cooking(self._originalMaterial)
        return ""


class SpicyOrder(Order):
    "香辣炒"

    def __init__(self, originalMaterial):
        super().__init__(originalMaterial)
        self._chef = StirFriedChef()

    def processingOrder(self):
        if (self._chef is not None):
            return self._chef.cooking(self._originalMaterial)
        return ""


class Waiter:
    "服务员"

    def __init__(self, name):
        self.__name = name
        self.__order = None

    def receiveOrder(self, order):
        self.__order = order

    def placeOrder(self):
        food = self.__order.processingOrder()
        print(food)



# class Customer:
#     "顾客"
#
#     def __init__(self, name):
#         self.__name = name
#
#     def order(self):

# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================

# 基于框架的实现
#==============================


# Test
#=======================================================================================================================

def testOrder():
    # o = Order("dd");
    # o.processingOrder()
    waiter = Waiter("1号服务员")
    order = SteamedOrder("大闸蟹")
    waiter.receiveOrder(order)
    waiter.placeOrder()


testOrder()