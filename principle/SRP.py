#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 8/7/2018

# Single Responsibility Principle, SRP


# class Animal:
#     """动物"""
#
#     def __init__(self, name):
#         self.__name = name
#
#     def running(self):
#         print(self.__name + "在跑...")
#
#
# Animal("猫").running()
# Animal("狗").running()


# # First method
# class Animal:
#     """动物"""
#
#     def __init__(self, name, type):
#         self.__name = name
#         self.__type = type
#
#     def running(self):
#         if(self.__type == "水生"):
#             print(self.__name + "在水里游...")
#         else:
#             print(self.__name + "在陆上跑...")
#
#
# Animal("狗", "陆生").running()
# Animal("鱼", "水生").running()


# # Second method
# class Animal:
#     """动物"""
#
#     def __init__(self, name):
#         self.__name = name
#
#     def running(self):
#         print(self.__name + "在陆上跑...")
#
#     def swimming(self):
#         print(self.__name + "在水里游...")
#
#
# Animal("狗").running()
# Animal("鱼").swimming()



# Third methold
class TerrestrialAnimal():
    """陆生生物"""

    def __init__(self, name):
        self.__name = name

    def running(self):
        print(self.__name + "在陆上跑...")


class AquaticAnimal():
    """水生生物"""

    def __init__(self, name):
        self.__name = name

    def swimming(self):
        print(self.__name + "在水里游...")


TerrestrialAnimal("狗").running()
AquaticAnimal("鱼").swimming()