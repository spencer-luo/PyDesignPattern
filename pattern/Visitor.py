#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 6/30/2018

# Version 1.0
#=======================================================================================================================
# from abc import ABCMeta, abstractmethod
# # 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
#
# class DesignPatternBook:
#     "《从生活的角度解读设计模式》一书"
#     def getName(self):
#         return "《从生活的角度解读设计模式》"
#
#
# class Reader(metaclass=ABCMeta):
#     "访问者，也就是读者"
#
#     @abstractmethod
#     def read(self, book):
#         pass
#
# class Engineer(Reader):
#
#     def read(self, book):
#         print("技术狗读" + book.getName() + "一书后的感受：能抓住模式的核心思想，深入浅出，很有见地！")
#
#
# class ProductManager(Reader):
#     "产品经理"
#
#     def read(self, book):
#         print("产品经理读" + book.getName() + "一书后的感受：配图非常有趣，文章很有层次感！")
#
# class OtherFriend(Reader):
#     "IT圈外的朋友"
#
#     def read(self, book):
#         print("IT圈外的朋友读" + book.getName() + "一书后的感受：技术的内容一脸蒙蔽，但故事很精彩，像是看小说或是故事集！")

# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class DataNode(metaclass=ABCMeta):
    "数据结构类"

    @abstractmethod
    def accept(self, visit):
        "接受访问者的访问"
        pass

class Visitor(metaclass=ABCMeta):
    "访问者"

    @abstractmethod
    def visit(self, data):
        "对数据对象的访问操作"
        pass


class ObjectStructure:
    "数据结构的管理类，也是数据对象的一个容器，可遍历容器内的所有元素"

    def __init__(self):
        self.__datas = []

    def add(self, dataElement):
        self.__datas.append(dataElement)

    def action(self, visitor):
        "进行数据访问的操作"
        for data in self.__datas:
            visitor.visit(data)


# 基于框架的实现
#==============================
class DesignPatternBook:
    "《从生活的角度解读设计模式》一书"

    def getName(self):
        return "《从生活的角度解读设计模式》"

    def accept(self, visitor):
        visitor.visit(self)

class Engineer(Visitor):

    def visit(self, book):
        print("技术狗读" + book.getName() + "一书后的感受：能抓住模式的核心思想，深入浅出，很有见地！")


class ProductManager(Visitor):
    "产品经理"

    def visit(self, book):
        print("产品经理读" + book.getName() + "一书后的感受：配图非常有趣，文章很有层次感！")

class OtherFriend(Visitor):
    "IT圈外的朋友"

    def visit(self, book):
        print("IT圈外的朋友读" + book.getName() + "一书后的感受：技术的内容一脸蒙蔽，但故事很精彩，像是看小说或是故事集！")


# Test
#=======================================================================================================================

def testBook():
    book = DesignPatternBook()
    fans = [Engineer(), ProductManager(), OtherFriend()];
    for fan in fans:
        fan.read(book)

def testVisitBook():
    book = DesignPatternBook()
    objMgr = ObjectStructure()
    objMgr.add(book)
    objMgr.action(Engineer())
    objMgr.action(ProductManager())
    objMgr.action(OtherFriend())


testBook()
# testVisitBook()
