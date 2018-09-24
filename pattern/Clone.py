#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 4/1/2018

# Version 1.0
#=======================================================================================================================
# from copy import copy, deepcopy
#
# class Person:
#     """人"""
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def showMyself(self):
#         print("我是" + self.__name + ",年龄" + str(self.__age) + ".")
#
#     def coding(self):
#         print("我是码农，我用程序改变世界，Coding...")
#
#     def reading(self):
#         print("阅读使我快乐！知识使我成长！如饥似渴地阅读是生活的一部分...")
#
#     def fallInLove(self):
#         print("春风吹，月亮明，花前月下好相约...")
#
#     def clone(self):
#         return copy(self)


# 浅拷贝与深拷贝
#=======================================================================================================================
from copy import copy, deepcopy

class PetStore:
    """宠物店"""

    def __init__(self, name):
        self.__name = name
        self.__petList = []

    def setName(self, name):
        self.__name = name

    def showMyself(self):
        print("%s 宠物店有以下宠物：" % self.__name)
        for pet in self.__petList:
            print(pet + "\t", end="")
        print()

    def addPet(self, pet):
        self.__petList.append(pet)


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
from copy import copy, deepcopy

class Clone:
    """克隆的基类"""

    def clone(self):
        """浅拷贝的方式克隆对象"""
        return copy(self)

    def deepClone(self):
        """深拷贝的方式克隆对象"""
        return deepcopy(self)


# 基于框架的实现
#==============================
class Person(Clone):
    """人"""

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showMyself(self):
        print("我是" + self.__name + ",年龄" + str(self.__age) + ".")

    def coding(self):
        print("我是码农，我用程序改变世界，Coding...")

    def reading(self):
        print("阅读使我快乐！知识使我成长！如饥似渴地阅读是生活的一部分...")

    def fallInLove(self):
        print("春风吹，月亮明，花前月下好相约...")


# Test
#=======================================================================================================================

def testClone():
    tony = Person("Tony", 27)
    tony.showMyself()
    tony.coding()

    tony1 = tony.clone()
    tony1.showMyself()
    tony1.reading()

    tony2 = tony.clone()
    tony2.showMyself()
    tony2.fallInLove()


def testPetStore():
    petter = PetStore("Petter")
    petter.addPet("小狗Coco")
    print("父本petter：", end="")
    petter.showMyself()
    print()

    petter1 = deepcopy(petter)
    petter1.addPet("小猫Amy")
    print("副本petter1：", end="")
    petter1.showMyself()
    print("父本petter：", end="")
    petter.showMyself()
    print()

    petter2 = copy(petter)
    petter2.addPet("小兔Ricky")
    print("副本petter2：", end="")
    petter2.showMyself()
    print("父本petter：", end="")
    petter.showMyself()


def testList():
    list = [1, 2, 3];
    list1 = list;
    print("id(list):", id(list))
    print("id(list1):", id(list1))
    print("修改之前：")
    print("list:", list)
    print("list1:", list1)
    list1.append(4);
    print("修改之后：")
    print("list:", list)
    print("list1:", list1)

    # petter = PetStore("Petter")
    # petter.addPet("小狗Coco")
    # print("父本tony：", end="")
    # petter.showMyself()
    #
    # petter1 = petter
    # petter1.addPet("小猫Amy")
    # print("副本tony1：", end="")
    # petter1.showMyself()
    # print("父本tony：", end="")
    # petter.showMyself()

testClone()
# testPetStore()
# testList()
