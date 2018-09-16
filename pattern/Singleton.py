##!/usr/bin/python

# Version 1.0
########################################################################################################################

class MyBeautifulGril(object):
    """我的漂亮女神"""
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifulGril.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("遇见" + name + "，我一见钟情！")
            MyBeautifulGril.__isFirstInit = True
        else:
            print("遇见" + name + "，我置若罔闻！")

    def showMyHeart(self):
        print(self.__name + "就我心中的唯一！")


# 各种singleton实现方式
########################################################################################################################
# class Singleton1(object):
#     """单例实现方式一"""
#     __instance = None
#     __isFirstInit = False
#
#     def __new__(cls, name):
#         if not cls.__instance:
#             Singleton1.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, name):
#         if not self.__isFirstInit:
#             self.__name = name
#             Singleton1.__isFirstInit = True
#
#     def getName(self):
#         return self.__name
#
# # Test
# tony = Singleton1("Tony")
# karry = Singleton1("Karry")
# print(tony.getName(), karry.getName())
# print("id(tony):", id(tony), "id(karry):", id(karry))
# print("tony == karry:", tony == karry)


# 方式二
#========================================================================================
# class Singleton2(type):
#     def __init__(cls, name, bases, attrs):
#         super(Singleton2, cls).__init__(name, bases, attrs)
#         cls._instance = None
#
#     def __call__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
#         return cls._instance
#
# class MyClass(metaclass=Singleton2):
#     pass
#     def __init__(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
# s0 = MyClass("Zhangsan")
# s1 = MyClass("Lisi")
# print(s0.getName(), s1.getName())
# print("id(s0):", id(s0), "id(s1):", id(s1))
# print("s0 == s1:", s0 == s1)


# 单例的装饰器
def singletonDecorator(cls, *args, **kwargs):
    "构造一个单例的装饰器"
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton

# @singletonDecorator
# class Singleton3:
#     "使用修饰器修饰的类为单例类"
#     def __init__(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
# s0 = Singleton3("Zhangsan")
# s1 = Singleton3("Lisi")
# print(s0.getName(), s1.getName())
# print("id(s0):", id(s0), "id(s1):", id(s1))
# print("s0 == s1:", s0 == s1)


# Version 2.0
########################################################################################################################
# @singletonDecorator
# class Love:
#     "真爱"
#     def __init__(self, name):
#         self.__name = name
#
#     def showMyHeart(self):
#         print("I love", self.__name, "forever!")

# Test
########################################################################################################################
def TestLove():
    jenny = MyBeautifulGril("Jenny")
    jenny.showMyHeart()
    kimi = MyBeautifulGril("Kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), " id(kimi):", id(kimi))


# TestLove()

