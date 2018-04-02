#!/usr/bin/python
# Authoer: Administrator
# Date: 4/1/2018

# Version 1.0
#=======================================================================================================================

from copy import copy, deepcopy

class Person:

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

    def clone(self):
        return copy(self)

    def deepClone(self):
        return deepcopy(self)

# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================


# 基于框架的实现
#==============================


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
    print("副本ton1：", end="")
    tony1.showMyself()
    print("父本tony：", end="")
    tony.showMyself()

    tony2 = tony.clone()
    tony2.addPet("小兔Ricky")
    print("副本ton1：", end="")
    tony2.showMyself()
    print("父本tony：", end="")
    tony.showMyself()

# testProtoType()
testProtoType2()

"""
prototype 原型模式
"""


class simpleLayer:
    background = [0, 0, 0, 0]
    content = "blank"

    def getContent(self):
        return self.content

    def getBackgroud(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def setParent(self, p):
        self.background[3] = p

    def fillBackground(self, back):
        self.background = back

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


# 新建图层，填充蓝底并画一只狗，
# if __name__ == "__main__":
def testLayer():
    # 浅拷贝后，直接对拷贝后引用（这里的数组）进行操作，原始对象中该引用的内容也会变动。
    dog_layer = simpleLayer()
    dog_layer.paint("狗")
    dog_layer.fillBackground([0, 0, 255, 0])
    print("原始的背景:", dog_layer.getBackgroud())
    print("原始的绘画:", dog_layer.getContent())
    another_dog_layer = dog_layer.clone()
    another_dog_layer.setParent(128)
    another_dog_layer.paint("小狗")
    print("原始的背景:", dog_layer.getBackgroud())
    print("原始的绘画:", dog_layer.getContent())
    print("原始的背景:", another_dog_layer.getBackgroud())
    print("原始的绘画:", another_dog_layer.getContent())

    print("---------------------------------------")
    # 深拷贝后，其对象内的引用内容也被进行了复制。
    dog_layer = simpleLayer()
    dog_layer.paint("狗")
    dog_layer.fillBackground([0, 0, 255, 0])
    print("原始的背景:", dog_layer.getBackgroud())
    print("原始的绘画:", dog_layer.getContent())
    another_dog_layer = dog_layer.deep_clone()
    another_dog_layer.setParent(128)
    another_dog_layer.paint("小狗")
    print("原始的背景:", dog_layer.getBackgroud())
    print("原始的绘画:", dog_layer.getContent())
    print("原始的背景:", another_dog_layer.getBackgroud())
    print("原始的绘画:", another_dog_layer.getContent())