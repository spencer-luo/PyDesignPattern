#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 7/21/2018

# Version 1.0
#=======================================================================================================================

class Employee:
    """公司员工"""

    def __init__(self, name):
        self.__name = name

    def doPerformance(self, skill):
        print(self.__name + "的表演:", end="")
        skill()


def sing():
    """唱歌"""
    print("唱一首歌")

def dling():
    """拉Ukulele"""
    print("拉一曲Ukulele")

def joke():
    """说段子"""
    print("说一搞笑段子")

def performMagicTricks():
    """表演魔术"""
    print("神秘魔术")

def skateboarding():
    """玩滑板"""
    print("酷炫滑板")


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Skill(metaclass=ABCMeta):
    """技能的抽象类"""

    @abstractmethod
    def performance(self):
        """技能表演"""
        pass

class NewEmployee:
    """公司新员工"""

    def __init__(self, name):
        self.__name = name

    def doPerformance(self, skill):
        print(self.__name + "的表演:", end="")
        skill.performance()

class Sing(Skill):
    """唱歌"""
    def performance(self):
        print("唱一首歌")

class Joke(Skill):
    """说段子"""
    def performance(self):
        print("说一搞笑段子")

class Dling(Skill):
    """拉Ukulele"""
    def performance(self):
        print("拉一曲Ukulele")

class PerformMagicTricks(Skill):
    """表演魔术"""
    def performance(self):
        print("神秘魔术")

class Skateboarding(Skill):
    """玩滑板"""
    def performance(self):
        print("酷炫滑板")


# 基于框架的实现
#==============================

# Test
#=======================================================================================================================

def testSkill():
    helen = Employee("Helen")
    helen.doPerformance(sing)
    frank = Employee("Frank")
    frank.doPerformance(dling)
    jacky = Employee("Jacky")
    jacky.doPerformance(joke)
    chork = Employee("Chork")
    chork.doPerformance(performMagicTricks)
    Kerry = Employee("Kerry")
    Kerry.doPerformance(skateboarding)

def testStrategySkill():
    helen = NewEmployee("Helen")
    helen.doPerformance(Sing())
    frank = NewEmployee("Frank")
    frank.doPerformance(Dling())
    jacky = NewEmployee("Jacky")
    jacky.doPerformance(Joke())
    chork = NewEmployee("Chork")
    chork.doPerformance(PerformMagicTricks())
    Kerry = NewEmployee("Kerry")
    Kerry.doPerformance(Skateboarding())


def isEvenNumber(num):
    return num % 2 == 0

def isGreaterThanTen(num):
    return num > 10

def getEvenNumbers(fun, elements):
    newList = []
    for item in elements:
        if (fun(item)):
            newList.append(item)
    return newList

def testCallback():
    elements = [2, 3, 6, 9, 12, 15, 18]
    # list1 = getEvenNumbers(isEvenNumber, elements)
    # list2 = getEvenNumbers(isGreaterThanTen, elements)
    list1 = list(filter(lambda x: x % 2 == 0, elements))
    list2 = list(filter(lambda x: x > 10, elements))
    print("所有的偶数：", list1)
    print("大于10的数：", list2)


# testSkill()
testStrategySkill()
# testCallback()