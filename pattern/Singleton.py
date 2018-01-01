##!/usr/bin/python

# Version 1.0
########################################################################################################################

# 单例
# class Love(object):
#     "真爱"
#     __instance = None
#     __first_init = None
#
#     def __new__(cls, name):
#         if not cls.__instance:
#             Love.__instance = object.__new__(cls)
#         return cls.__instance
#
#     def __init__(self, name):
#         if not self.__first_init:
#             self.__name = name
#             Love.__first_init = True
#
#     def showMyLove(self):
#         print("I love", self.__name, "forever!")


# 各种singleton实现方式
########################################################################################################################
# class Singleton1(object):
#     "单例"
#     __instance = None
#     __first_init = None
#
#     def __new__(cls, name):
#         if not cls.__instance:
#             Singleton1.__instance = object.__new__(cls)
#         return cls.__instance
#
#     def __init__(self, name):
#         if not self.__first_init:
#             self.__name = name
#             Singleton1.__first_init = True
#
#     def getName(self):
#         return self.__name
#
# # Test
# s0 = Singleton1("Zhangsan")
# s1 = Singleton1("Lisi")
# print(s0.getName(), s1.getName())
# print("id(s0):", id(s0), "id(s1):", id(s1))
# print("s0 == s1:", s0 == s1)


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
@singletonDecorator
class Love:
    "真爱"
    def __init__(self, name):
        self.__name = name

    def showMyLove(self):
        print("I love", self.__name, "forever!")

# Test
########################################################################################################################
def TestLove():
    "测试程序"
    love0 = Love("Jenny")
    love1 = Love("Jean")
    love0.showMyLove()
    love1.showMyLove()
    print("id(love0):", id(love0), "id(love1):", id(love1))
    print("love0 == love1:", love0 == love1)


TestLove()



