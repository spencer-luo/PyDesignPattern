#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 7/29/2018

# class TerrestrialAnimal():
#     """陆生生物"""
#
#     def __init__(self, name):
#         self.__name = name
#
#     def running(self):
#         print(self.__name + "在陆上跑...")
#
#
# class AquaticAnimal():
#     """水生生物"""
#
#     def __init__(self, name):
#         self.__name = name
#
#     def swimming(self):
#         print(self.__name + "在水里游...")
#
#
# TerrestrialAnimal("狗").running()
# AquaticAnimal("鱼").swimming()


from abc import ABCMeta, abstractmethod

class Animal:
    """动物"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def running(self):
        pass

class TerrestrialAnimal(Animal):
    """陆生生物"""

    def __init__(self, name):
        super().__init__(name)

    def running(self):
        print(self._name + "在陆上跑...")


class AquaticAnimal(Animal):
    """水生生物"""

    def __init__(self, name):
        super().__init__(name)

    def running(self):
        print(self._name + "在水里游...")

class BirdAnimal(Animal):
    """鸟类动物"""

    def __init__(self, name):
        super().__init__(name)

    def running(self):
        print(self._name + "在天空飞...")


class Monkey(TerrestrialAnimal):
    """猴子"""

    def __init__(self, name):
        super().__init__(name)

    def climbing(self):
        print(self._name + "在爬树，动作灵活轻盈...")


class Zoo:
    """动物园"""

    def __init__(self):
        self.__animals =[]

    def addAnimal(self, animal):
        self.__animals.append(animal)

    def displayActivity(self):
        print("观察每一种动物的活动方式：")
        for animal in self.__animals:
            animal.running()

    def monkeyClimbing(self, monkey):
        monkey.climbing()


def testZoo():
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal("狗"))
    zoo.addAnimal(AquaticAnimal("鱼"))
    zoo.addAnimal(BirdAnimal("鸟"))
    monkey = Monkey("猴子")
    zoo.addAnimal(monkey)
    zoo.displayActivity()
    print()
    print("观察猴子的爬树行为：")
    zoo.monkeyClimbing(monkey)


testZoo()
