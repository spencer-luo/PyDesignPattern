#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 11/26/2017

# Version 1.0
#=======================================================================================================================
class Person:
    "人"

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def wear(self):
        print("我的着装是：")


class Engineer(Person):
    "工程师"

    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def getSkill(self):
        return self.__skill

    def wear(self):
        print("我是" + self.getSkill() + "工程师" + self.getName())
        super().wear()

class Teacher(Person):
    "教师"

    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def getTitle(self):
        return self.__title

    def wear(self):
        print("我是" + self.getName() + self.getTitle())
        super().wear()

class ClothingDecorator(Person):
    "服装装饰器"

    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()


class CasualPantDecorator(ClothingDecorator):
    "休闲裤"

    def __init__(self, person):
        super().__init__(person)

    def wear(self):
        super().wear()
        print("一条卡其色休闲裤")


class BeltDecorator(ClothingDecorator):
    "腰带"

    def __init__(self, person):
        super().__init__(person)

    def wear(self):
        super().wear()
        print("一条银色针扣头的黑色腰带")

class LeatherShoesDecorator(ClothingDecorator):
    "皮鞋"

    def __init__(self, person):
        super().__init__(person)

    def wear(self):
        super().wear()
        print("一双深色休闲皮鞋")

class KnittedSweaterDecorator(ClothingDecorator):
    "针织毛衣"

    def __init__(self, person):
        super().__init__(person)

    def wear(self):
        super().wear()
        print("一件紫红色针织毛衣")


class WhiteShirtDecorator(ClothingDecorator):
    "白色衬衫"

    def __init__(self, person):
        super().__init__(person)

    def wear(self):
        super().wear()
        print("一件白色衬衫")


class GlassesDecorator(ClothingDecorator):
    "眼镜"

    def __init__(self, person):
        super().__init__(person)

    def wear(self):
        super().wear()
        print("一副方形黑框眼镜")

# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================


# 基于框架的实现
#==============================


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
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    sweater = KnittedSweaterDecorator(shoes)
    shirt = WhiteShirtDecorator(sweater)
    glasses = GlassesDecorator(shirt)
    glasses.wear()

# testDecorator()
testDecorator2()