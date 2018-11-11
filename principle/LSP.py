#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 8/7/2018


# Liskov Substitution Principle, LSP

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


class Monkey(TerrestrialAnimal):
    """猴子"""

    def __init__(self, name):
        super().__init__(name)

    def climbing(self):
        print(self._name + "在爬树，动作灵活轻盈...")


# 修改Zoo类，增加climbing方法：
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