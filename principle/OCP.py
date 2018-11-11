#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 8/7/2018

# Open Close Principle，OCP



# class Zoo:
#     """动物园"""
#
#     def __init__(self):
#         self.__animals =[
#             TerrestrialAnimal("狗"),
#             AquaticAnimal("鱼")
#         ]
#
#     def displayActivity(self):
#         for animal in self.__animals:
#             if isinstance(animal, TerrestrialAnimal):
#                 animal.running()
#             else:
#                 animal.swimming()
#
# zoo = Zoo()
# zoo.displayActivity()



# def displayActivity(self):
# 	for animal in self.__animals:
# 		if isinstance(animal, TerrestrialAnimal):
# 			animal.running()
# 		elif isinstance(animal, BirdAnimal)
# 			animal.flying()
# 		else:
# 			animal.swimming()



from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Animal(metaclass=ABCMeta):
    """动物"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def moving(self):
        pass

class TerrestrialAnimal(Animal):
    """陆生生物"""

    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(self._name + "在陆上跑...")


class AquaticAnimal(Animal):
    """水生生物"""

    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(self._name + "在水里游...")


class BirdAnimal(Animal):
    """鸟类动物"""

    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(self._name + "在天空飞...")


class Zoo:
    """动物园"""

    def __init__(self):
        self.__animals =[]

    def addAnimal(self, animal):
        self.__animals.append(animal)

    def displayActivity(self):
        print("观察每一种动物的活动方式：")
        for animal in self.__animals:
            animal.moving()


def testZoo():
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal("狗"))
    zoo.addAnimal(AquaticAnimal("鱼"))
    zoo.addAnimal(BirdAnimal("鸟"))
    zoo.displayActivity()



testZoo()