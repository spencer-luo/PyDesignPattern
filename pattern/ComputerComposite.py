#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 12/16/2017

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class ComputerComponent(metaclass=ABCMeta):
    """组件，所有子配件的基类"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def showInfo(self, indent = ""):
        pass

    def isComposite(self):
        return False

    def startup(self, indent = ""):
        print("%s%s 准备开始工作..." % (indent, self._name) )

    def shutdown(self, indent = ""):
        print("%s%s 即将结束工作..." % (indent, self._name) )


class CPU(ComputerComponent):
    """中央处理器"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%sCPU:%s,可以进行高速计算。" % (indent, self._name))


class MemoryCard(ComputerComponent):
    """内存条"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s内存:%s,可以缓存数据，读写速度快。" % (indent, self._name))


class HardDisk(ComputerComponent):
    """硬盘"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s硬盘:%s,可以永久存储数据，容量大。" % (indent, self._name) )


class GraphicsCard(ComputerComponent):
    """显卡"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s显卡:%s,可以高速计算和处理图形图像。" % (indent, self._name) )


class Battery(ComputerComponent):
    """电源"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s电源:%s,可以持续给主板和外接配件供电。" % (indent, self._name) )


class Fan(ComputerComponent):
    """风扇"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s风扇:%s，辅助CPU散热。" % (indent, self._name) )


class Displayer(ComputerComponent):
    """"显示器"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s显示器:%s，负责内容的显示。" % (indent, self._name) )


class ComputerComposite(ComputerComponent):
    """配件组合器"""

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def showInfo(self, indent):
        print("%s,由以下部件组成:" % (self._name) )
        indent += "\t"
        for element in self._components:
            element.showInfo(indent)

    def isComposite(self):
        return True

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def startup(self, indent):
        super().startup(indent)
        indent += "\t"
        for element in self._components:
            element.startup(indent)

    def shutdown(self, indent):
        super().shutdown(indent)
        indent += "\t"
        for element in self._components:
            element.shutdown(indent)


class Mainboard(ComputerComposite):
    """主板"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "主板:", end="")
        super().showInfo(indent)


class ComputerCase(ComputerComposite):
    """机箱"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "机箱:", end="")
        super().showInfo(indent)


class Computer(ComputerComposite):
    """电脑"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "电脑:", end="")
        super().showInfo(indent)


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================

from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Component(metaclass=ABCMeta):
    """组件"""

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def isComposite(self):
        return False

    @abstractmethod
    def feature(self, indent):
        # indent 仅用于内容输出时的缩进
        pass

class Composite(Component):
    """复合组件"""

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def isComposite(self):
        return True

    def feature(self, indent):
        indent += "\t"
        for component in self._components:
            print(indent, end="")
            component.feature(indent)



class ComponentImplA(Component):
    "Test"

    def __init__(self, name):
        super().__init__(name)

    def feature(self):
        print("name：%s" % self._name)


# 基于框架的实现
#==============================
import os
# 引入 os 模块

class FileDetail(Component):
    """谇详情"""
    def __init__(self, name):
        super().__init__(name)
        self._size = 0

    def setSize(self, size):
        self._size = size

    def getFileSize(self):
        return self._size

    def feature(self, indent):
        # 文件大小，单位：KB，精确度：2位小数
        fileSize = round(self._size / float(1024), 2)
        print("文件名称：%s， 文件大小：%sKB" % (self._name, fileSize) )


class FolderDetail(Composite):
    """文件夹详情"""

    def __init__(self, name):
        super().__init__(name)
        self._count = 0

    def setCount(self, fileNum):
        self._count = fileNum

    def getCount(self):
        return self._count

    def feature(self, indent):
        print("文件夹名：%s， 文件数量：%d。包含的文件：" % (self._name, self._count) )
        super().feature(indent)


def scanDir(rootPath, folderDetail):
    """扫描某一文件夹下的所有目录"""
    if not os.path.isdir(rootPath):
        raise ValueError("rootPath不是有效的路径：%s" % rootPath)

    if folderDetail is None:
        raise ValueError("folderDetail不能为空!")


    fileNames = os.listdir(rootPath)
    for fileName in fileNames:
        filePath = os.path.join(rootPath, fileName)
        if os.path.isdir(filePath):
            folder = FolderDetail(fileName)
            scanDir(filePath, folder)
            folderDetail.addComponent(folder)
        else:
            fileDetail = FileDetail(fileName)
            fileDetail.setSize(os.path.getsize(filePath))
            folderDetail.addComponent(fileDetail)
            folderDetail.setCount(folderDetail.getCount() + 1)



# Test
#=======================================================================================================================
def testComputer():
    mainBoard = Mainboard("GIGABYTE Z170M M-ATX")
    mainBoard.addComponent(CPU("Intel Core i5-6600K"))
    mainBoard.addComponent(MemoryCard("Kingston Fury DDR4"))
    mainBoard.addComponent(HardDisk("Kingston V300 "))
    mainBoard.addComponent(GraphicsCard("Colorful iGame750"))

    computerCase = ComputerCase("SAMA MATX")
    computerCase.addComponent(mainBoard)
    computerCase.addComponent(Battery("Antec VP 450P"))
    computerCase.addComponent(Fan("DEEPCOOL 120T"))

    computer = Computer("Tony DIY电脑")
    computer.addComponent(computerCase)
    computer.addComponent(Displayer("AOC LV243XIP"))

    computer.showInfo("")
    print("\n开机过程:")
    computer.startup("")
    print("\n关机过程:")
    computer.shutdown("")


def testComposite():
    tony = ComponentImplA("Tony")
    tony.feature()
    karry = ComponentImplA("Karry")
    composite = Composite("Composite")
    composite.addComponent(tony)
    composite.addComponent(karry)
    composite.feature()


def testDir():
    folder = FolderDetail("生活中的设计模式")
    scanDir("E:\生活中的设计模式", folder)
    folder.feature("")

    # isDir = os.path.isfile("D:\Test\file1.txt")
    # print(isDir)

# testComputer()
# testComposite()
testDir()