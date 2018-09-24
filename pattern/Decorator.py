#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 11/26/2017

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Person(metaclass=ABCMeta):
    """人"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("着装：")


class Engineer(Person):
    """工程师"""

    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def getSkill(self):
        return self.__skill

    def wear(self):
        print("我是 " + self.getSkill() + "工程师 " + self._name, end="， ")
        super().wear()

class Teacher(Person):
    "教师"

    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def getTitle(self):
        return self.__title

    def wear(self):
        print("我是 " + self._name + self.getTitle(), end="， ")
        super().wear()

class ClothingDecorator(Person):
    """服装装饰器的基类"""

    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    """休闲裤装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条卡其色休闲裤")


class BeltDecorator(ClothingDecorator):
    """腰带装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条银色针扣头的黑色腰带")

class LeatherShoesDecorator(ClothingDecorator):
    """皮鞋装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一双深色休闲皮鞋")

class KnittedSweaterDecorator(ClothingDecorator):
    """针织毛衣装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一件紫红色针织毛衣")


class WhiteShirtDecorator(ClothingDecorator):
    """白色衬衫装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一件白色衬衫")


class GlassesDecorator(ClothingDecorator):
    """眼镜装饰器"""

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一副方形黑框眼镜")




# Test
#=======================================================================================================================
def testDecorator():
    tony = Engineer("Tony", "客户端")
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    shirt = WhiteShirtDecorator(shoes)
    sweater = KnittedSweaterDecorator(shirt)
    glasses = GlassesDecorator(sweater)
    glasses.wear()

    print()
    decorateTeacher = GlassesDecorator(WhiteShirtDecorator(LeatherShoesDecorator(Teacher("wells", "教授"))))
    decorateTeacher.wear()


def testDecorator2():
    tony = Engineer("Tony", "客户端")
    sweater = KnittedSweaterDecorator(tony)
    shirt = WhiteShirtDecorator(sweater)
    glasses = GlassesDecorator(shirt)
    glasses.wear()

# testDecorator()
# testDecorator2()