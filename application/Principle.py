#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 6/30/2018

# class Animal:
#     """动物"""
#
#     def __init__(self, name):
#         self.__name = name
#
#     def moving(self):
#         print(self.__name + "在跑...")
#
#
# Animal("猫").moving()
# Animal("狗").moving()



# class Animal:
#     """动物"""
#
#     def __init__(self, name, type):
#         self.__name = name
#         self.__type = type
#
#     def moving(self):
#         if(self.__type == "水生"):
#             print(self.__name + "在水里游...")
#         else:
#             print(self.__name + "在陆上跑...")
#
#
# Animal("狗", "陆生").moving()
# Animal("鱼", "水生").moving()


# class Animal:
#     """动物"""
#
#     def __init__(self, name):
#         self.__name = name
#
#     def moving(self):
#         print(self.__name + "在陆上跑...")
#
#     def swimming(self):
#         print(self.__name + "在水里游...")
#
#
# Animal("狗").moving()
# Animal("鱼").swimming()


# class TerrestrialAnimal():
#     """陆生生物"""
#
#     def __init__(self, name):
#         self.__name = name
#
#     def moving(self):
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
# TerrestrialAnimal("狗").moving()
# AquaticAnimal("鱼").swimming()

# 开放封闭原则和里氏替换原则
#=======================================================================================================================
# from abc import ABCMeta, abstractmethod
#
# class Animal(metaclass=ABCMeta):
#     """动物"""
#
#     def __init__(self, name):
#         self._name = name
#
#     @abstractmethod
#     def moving(self):
#         pass
#
# class TerrestrialAnimal(Animal):
#     """陆生生物"""
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def moving(self):
#         print(self._name + "在陆上跑...")
#
#     def checkFood(self, food):
#         food.category() == ""
#
#
# class AquaticAnimal(Animal):
#     """水生生物"""
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def moving(self):
#         print(self._name + "在水里游...")
#
# class BirdAnimal(Animal):
#     """鸟类动物"""
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def moving(self):
#         print(self._name + "在天空飞...")
#
#
# class Monkey(TerrestrialAnimal):
#     """猴子"""
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def climbing(self):
#         print(self._name + "在爬树，动作灵活轻盈...")
#
#
# class Zoo:
#     """动物园"""
#
#     def __init__(self):
#         self.__animals =[]
#
#     def addAnimal(self, animal):
#         self.__animals.append(animal)
#
#     def displayActivity(self):
#         print("观察每一种动物的活动方式：")
#         for animal in self.__animals:
#             animal.moving()
#
#     def monkeyClimbing(self, monkey):
#         monkey.climbing()
#
# def testZoo():
#     zoo = Zoo()
#     zoo.addAnimal(TerrestrialAnimal("狗"))
#     zoo.addAnimal(AquaticAnimal("鱼"))
#     zoo.addAnimal(BirdAnimal("鸟"))
#     monkey = Monkey("猴子")
#     zoo.addAnimal(monkey)
#     zoo.displayActivity()
#     print()
#     print("观察猴子的爬树行为：")
#     zoo.monkeyClimbing(monkey)
#
# testZoo()



# class Dog:
#     def eat(self, meat):
#         pass
#
# class Fish:
#     def eat(self, grass):
#         pass


# from abc import ABCMeta, abstractmethod
# # 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
#
# class Animal(metaclass=ABCMeta):
#     """动物"""
#
#     def __init__(self, name):
#         self._name = name
#
#     def eat(self, food):
#         if(self.checkFood(food)):
#             print(self._name + "进食" + food.getName())
#         else:
#             print(self._name + "不吃" + food.getName())
#
#     @abstractmethod
#     def checkFood(self, food):
#         pass
#
# class Dog(Animal):
#     """狗"""
#
#     def __init__(self):
#         super().__init__("狗")
#
#     def checkFood(self, food):
#         return food.category() == "肉类"
#
# class Swallow(Animal):
#     """燕子"""
#
#     def __init__(self):
#         super().__init__("燕子")
#
#     def checkFood(self, food):
#         return food.category() == "昆虫"
#
# class Food(metaclass=ABCMeta):
#     """食物"""
#
#     def __init__(self, name):
#         self._name = name
#
#     def getName(self):
#         return self._name
#
#     @abstractmethod
#     def category(self):
#         """食物类别"""
#         pass
#
#     @abstractmethod
#     def nutrient(self):
#         """营养成分"""
#         pass
#
#
# class Meat(Food):
#     """肉"""
#     def __init__(self):
#         super().__init__("肉")
#
#     def category(self):
#         return "肉类"
#
#     def nutrient(self):
#         return "蛋白质、脂肪"
#
#
# class Worm(Food):
#     """虫子"""
#     def __init__(self):
#         super().__init__("虫子")
#
#     def category(self):
#         return "昆虫"
#
#     def nutrient(self):
#         return "蛋白质含、微量元素"
#
#
# def testFood():
#     dog = Dog()
#     swallow = Swallow()
#     meat = Meat()
#     worm = Worm()
#     dog.eat(meat)
#     dog.eat(worm)
#     swallow.eat(meat)
#     swallow.eat(worm)
#
# testFood()




from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Animal(metaclass=ABCMeta):
    """(脊椎)动物"""

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    @abstractmethod
    def feature(self):
        pass

    @abstractmethod
    def moving(self):
        pass


class IRunnable(metaclass=ABCMeta):
    """奔跑的接口"""

    @abstractmethod
    def running(self):
        pass

class IFlyable(metaclass=ABCMeta):
    """飞行的接口"""

    @abstractmethod
    def flying(self):
        pass

class INatatory(metaclass=ABCMeta):
    """游泳的接口"""

    @abstractmethod
    def swimming(self):
        pass


class MammalAnimal(Animal, IRunnable):
    """哺乳动物"""

    def __init__(self, name):
        super().__init__(name)

    def feature(self):
        print(self._name + "的生理特征：恒温，胎生，哺乳。")

    def running(self):
        print("在陆上跑...")

    def moving(self):
        print(self._name + "的活动方式：", end="")
        self.running()


class BirdAnimal(Animal, IFlyable):
    """鸟类动物"""

    def __init__(self, name):
        super().__init__(name)

    def feature(self):
        print(self._name + "的生理特征：恒温，卵生，前肢成翅。")

    def flying(self):
        print("在天空飞...")

    def moving(self):
        print(self._name + "的活动方式：", end="")
        self.flying()

class FishAnimal(Animal, INatatory):
    """鱼类动物"""

    def __init__(self, name):
        super().__init__(name)

    def feature(self):
        print(self._name + "的生理特征：流线型体形，用鳃呼吸。")

    def swimming(self):
        print("在水里游...")

    def moving(self):
        print(self._name + "的活动方式：", end="")
        self.swimming()


class Bat(MammalAnimal, IFlyable):
    """蝙蝠"""

    def __init__(self, name):
        super().__init__(name)

    def running(self):
        print("行走功能已经退化。")

    def flying(self):
        print("在天空飞...", end="")

    def moving(self):
        print(self._name + "的活动方式：", end="")
        self.flying()
        self.running()

class Swan(BirdAnimal, IRunnable, INatatory):
    """天鹅"""

    def __init__(self, name):
        super().__init__(name)

    def running(self):
        print("在陆上跑...", end="")

    def swimming(self):
        print("在水里游...", end="")

    def moving(self):
        print(self._name + "的活动方式：", end="")
        self.running()
        self.swimming()
        self.flying()

class CrucianCarp(FishAnimal):
    """鲫鱼"""

    def __init__(self, name):
        super().__init__(name)


def testAnimal():
    bat = Bat("蝙蝠")
    bat.feature()
    bat.moving()
    swan = Swan("天鹅")
    swan.feature()
    swan.moving()
    crucianCarp = CrucianCarp("鲫鱼")
    crucianCarp.feature()
    crucianCarp.moving()


testAnimal()