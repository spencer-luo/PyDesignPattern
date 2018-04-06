#!/usr/bin/python
# Authoer: Administrator
# Date: 4/1/2018

# Version 1.0
#=======================================================================================================================

# from copy import copy, deepcopy
#
# class Person:
#     "人"
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.__petList = []
#
#     def showMyself(self):
#         print("我是" + self.__name + ",年龄" + str(self.__age) + ". 我养了这些宠物：")
#         for pet in self.__petList:
#             print(pet + "\t", end="")
#         print()
#
#     def addPet(self, pet):
#         self.__petList.append(pet)
#
#     def clone(self):
#         return copy(self)
#
#     def deepClone(self):
#         return deepcopy(self)
#
#     def coding(self):
#         print("我是码农，我在Coding改变世界...")
#
#     def reading(self):
#         print("阅读使我快乐！知识使我成长！如饥似渴地阅读是生活的一部分...")
#
#     def fallInLove(self):
#         print("春风吹，月亮明，花前月下好相约...")


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
from copy import copy, deepcopy

class Clone:
    "克隆的基类"

    def clone(self):
        "浅拷贝的方式克隆对象"
        return copy(self)

    def deepClone(self):
        "深拷贝的方式克隆对象"
        return deepcopy(self)

# 基于框架的实现
#==============================


class Person(Clone):
    "人"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__petList = []

    def showMyself(self):
        print("我是" + self.__name + ",年龄" + str(self.__age) + ". 我养了这些宠物：")
        for pet in self.__petList:
            print(pet + "\t", end="")
        print()

    def addPet(self, pet):
        self.__petList.append(pet)

    def coding(self):
        print("我是码农，我在Coding改变世界...")

    def reading(self):
        print("阅读使我快乐！知识使我成长！如饥似渴地阅读是生活的一部分...")

    def fallInLove(self):
        print("春风吹，月亮明，花前月下好相约...")


# Test
#=======================================================================================================================
def testProtoType():
    tony = Person("Tony", 26)
    tony.showMyself()
    tony.coding()

    tony1 = tony.clone()
    tony1.showMyself()
    tony1.reading()

    tony2 = tony.clone()
    tony2.showMyself()
    tony2.fallInLove()

def testProtoType2():
    tony = Person("Tony", 26)
    tony.addPet("小狗Coco")
    print("父本tony：", end="")
    tony.showMyself()

    tony1 = tony.deepClone()
    tony1.addPet("小猫Amy")
    print("副本tony1：", end="")
    tony1.showMyself()
    print("父本tony：", end="")
    tony.showMyself()

    tony2 = tony.clone()
    tony2.addPet("小兔Ricky")
    print("副本tony2：", end="")
    tony2.showMyself()
    print("父本tony：", end="")
    tony.showMyself()

def testList():
    list = [1, 2, 3];
    list1 = list;
    print("list's id:", id(list))
    print("list1's id:", id(list1))
    print("修改之前：")
    print("list:", list)
    print("list1:", list1)
    list1.append(4);
    print("修改之后：")
    print("list:", list)
    print("list1:", list1)

    tony = Person("Tony", 26)
    tony.addPet("小狗Coco")
    print("父本tony：", end="")
    tony.showMyself()

    tony1 = tony
    tony1.addPet("小猫Amy")
    print("副本tony1：", end="")
    tony1.showMyself()
    print("父本tony：", end="")
    tony.showMyself()


# testProtoType()
# testProtoType2()
testList()
