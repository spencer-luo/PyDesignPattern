#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 9/24/2018

# Python中的装饰器
#=======================================================================================================================
# Python中函数的特殊功能
#==============================
def func(num):
    """定义内部函数并返回"""

    def firstInnerFunc():
        return "这是第一个内部函数"

    def secondInnerFunc():
        return "这是第二个内部函数"

    if num == 1:
        return firstInnerFunc
    else:
        return secondInnerFunc


# print(func(1))
# print(func(2))
# print(func(1)())
# print(func(2)())


# firstFunc = func(1)
# secondFunc = func(2)
# print(firstFunc)
# print(secondFunc)
# print(firstFunc())
# print(secondFunc())


# 装饰器修饰函数
#==============================
import logging
logging.basicConfig(level=logging.INFO)

def loggingDecorator(func):
    """记录日志的装饰器"""
    def wrapperLogging(*args, **kwargs):
        logging.info("开始执行 %s() ..." % func.__name__)
        func(*args, **kwargs)
        logging.info("%s() 执行完成！" % func.__name__)
    return wrapperLogging

def showInfo(*args, **kwargs):
    print("这是一个测试函数，参数：", args, kwargs)


# decoratedShowInfo = loggingDecorator(showInfo)
# decoratedShowInfo('arg1', 'arg2', kwarg1 = 1, kwarg2 = 2)


# def showMin(a, b):
#     print("%d、%d 中的最小值是：%d" % (a, b, a + b))
#
# decoratedShowMin = loggingDecorator(showMin)
# decoratedShowMin(2, 3)


# @loggingDecorator
# def showMin(a, b):
#     print("%d、%d 中的最小值是：%d" % (a, b, a + b))
#
# showMin(2, 3)


# 装饰器修饰类
#==============================
class ClassDecorator:
    """类装饰器，记录一个类被实例化的次数"""

    def __init__(self, func):
        self.__numOfCall = 0
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.__numOfCall += 1
        obj = self.__func(*args, *kwargs)
        print("创建%s的第%d个实例:%s" % (self.__func.__name__, self.__numOfCall, id(obj)))
        return obj

@ClassDecorator
class MyClass:

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


tony = MyClass("Tony")
karry = MyClass("Karry")
print(id(tony))
print(id(karry))
