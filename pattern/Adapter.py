#!/usr/bin/python
# Authoer: Administrator
# Date: 4/24/2018

# Version 1.0
#=======================================================================================================================
class IHightPerson:
    "接口类，提供空实现的方法，由子类去实现"

    def getName(self):
        "获取姓名"
        pass

    def getHeight(self):
        "获取身高"
        pass


class HighPerson(IHightPerson):
    "个高的人"

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getHeight(self):
        return 170

class ShortPerson:
    "个矮的人"

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getRealHeight(self):
        return 160

    def getShoesHeight(self):
        return 6

class DecoratePerson(ShortPerson, IHightPerson):
    "有高跟鞋搭配的人"

    def getHeight(self):
        return super().getRealHeight() + super().getShoesHeight()


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================


# 基于框架的实现
#==============================


# Test
#=======================================================================================================================

def canPlayReceptionist(person):
    """
    是否可以成为(高级酒店)接待员
    :param person: IHightPerson的对象
    :return: 是否符合做接待员的条件
    """
    return person.getHeight() >= 165;


def testPerson():
    lira = HighPerson("Lira")
    print(lira.getName() + "身高" + str(lira.getHeight()) + "，完美如你，天生的美女！" )
    print("是否适合做接待员：", "符合" if canPlayReceptionist(lira) else "不符合")
    print()
    demi = DecoratePerson("Demi");
    print(demi.getName() + "身高" + str(demi.getHeight()) + "在高跟鞋的适配下，你身高不输高圆圆，气质不输范冰冰！")
    print("是否适合做接待员：", "符合" if canPlayReceptionist(lira) else "不符合")


testPerson()
