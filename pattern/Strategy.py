#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 5/1/2018

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class IVehicle(metaclass=ABCMeta):
    """交通工具的抽象类"""

    @abstractmethod
    def running(self):
        pass


class SharedBicycle(IVehicle):
    """共享单车"""

    def running(self):
        print("骑共享单车(轻快便捷)", end='')


class ExpressBus(IVehicle):
    """快速公交"""

    def running(self):
        print("坐快速公交(经济绿色)", end='')

class Express(IVehicle):
    """快车"""

    def running(self):
        print("打快车(快速方便)", end='')


class Subway(IVehicle):
    """地铁"""

    def running(self):
        print("坐地铁(高效安全)", end='')


class Classmate:
    """参加聚餐的同学"""

    def __init__(self, name, vechicle):
        self.__name = name
        self.__vechicle = vechicle

    def attendTheDinner(self):
        print(self.__name + " ", end='')
        self.__vechicle.running()
        print(" 来参加聚餐！")


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Person:
    """人类"""

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def showMysef(self):
        print("%s 年龄：%d岁，体重：%0.2fkg，身高：%0.2fm" % (self.name, self.age, self.weight, self.height) )


class ICompare(metaclass=ABCMeta):
    """比较算法"""

    @abstractmethod
    def comparable(self, person1, person2):
        "person1 > person2 返回值>0，person1 == person2 返回0， person1 < person2 返回值小于0"
        pass


class CompareByAge(ICompare):
    """通过年龄排序"""

    def comparable(self, person1, person2):
        return person1.age - person2.age


class CompareByHeight(ICompare):
    """通过身高进行排序"""

    def comparable(self, person1, person2):
        return person1.height - person2.height


class CompareByHeightAndWeight(ICompare):
    """根据身高和体重的综合情况来排序
    (身高和体重的权重分别是0.6和0.4)"""

    def comparable(self, person1, person2):
        value1 = person1.height * 0.6 + person1.weight * 0.4
        value2 = person2.height * 0.6 + person2.weight * 0.4
        return value1 - value2


class SortPerson:
    "Person的排序类"

    def __init__(self, compare):
        self.__compare = compare

    def sort(self, personList):
        """排序算法
        这里采用最简单的冒泡排序"""
        n = len(personList)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if(self.__compare.comparable(personList[j], personList[j+1]) > 0):
                    tmp = personList[j]
                    personList[j] = personList[j+1]
                    personList[j+1] = tmp
            j += 1
        i += 1


# 基于框架的实现
#==============================


# Test
#=======================================================================================================================

def testTheDinner():
    sharedBicycle = SharedBicycle()
    joe = Classmate("Joe", sharedBicycle)
    joe.attendTheDinner()
    helen = Classmate("Helen", Subway())
    helen.attendTheDinner()
    henry = Classmate("Henry", ExpressBus())
    henry.attendTheDinner()
    ruby = Classmate("Ruby", Express())
    ruby.attendTheDinner()



def testSortPerson():
    personList = [
        Person("Tony", 2, 54.5, 0.82),
        Person("Jack", 31, 74.5, 1.80),
        Person("Nick", 54, 44.5, 1.59),
        Person("Eric", 23, 62.0, 1.78),
        Person("Helen", 16, 45.7, 1.60)
    ]
    ageSorter = SortPerson(CompareByAge())
    ageSorter.sort(personList)
    print("根据年龄进行排序后的结果：")
    for person in personList:
        person.showMysef()
    print()

    heightSorter = SortPerson(CompareByHeight())
    heightSorter.sort(personList)
    print("根据身高进行排序后的结果：")
    for person in personList:
        person.showMysef()
    print()

    # heightWeightSorter = SortPerson(CompareByHeightAndWeight())
    # heightWeightSorter.sort(personList)
    # print("根据身高和体重进行排序后的结果：")
    # for person in personList:
    #     person.showMysef()



from operator import itemgetter,attrgetter

def testPersonListInPython():
    "用Python的方式对Person进行排序"

    personList = [
        Person("Tony", 2, 54.5, 0.82),
        Person("Jack", 31, 74.5, 1.80),
        Person("Nick", 54, 44.5, 1.59),
        Person("Eric", 23, 62.0, 1.78),
        Person("Helen", 16, 45.7, 1.60)
    ]

    # 使用operator模块根据年龄、身高进行排序
    sortedPerons = sorted(personList, key = attrgetter('age'))
    sortedPerons1 = sorted(personList, key=attrgetter('height'))

    print("根据年龄进行排序后的结果：")
    for person in sortedPerons:
        person.showMysef()
    print()
    print("根据身高进行排序后的结果：")
    for person in sortedPerons1:
        person.showMysef()


    # print("根据身高和体重的综合情况来排序：")
    # sortedPerons1 = sorted(personList, key=attrgetter("height" + "weight"))
    # for person in sortedPerons1:
    #     person.showMysef()



# testTheDinner()
# testSortPerson()
testPersonListInPython()


# testArray()