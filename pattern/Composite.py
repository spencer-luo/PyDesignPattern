#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 12/16/2017

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Component(metaclass=ABCMeta):
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


class CPU(Component):
    """中央处理器"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%sCPU:%s,可以进行高速计算。" % (indent, self._name))


class MemoryCard(Component):
    """内存条"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s内存:%s,可以缓存数据，读写速度快。" % (indent, self._name))


class HardDisk(Component):
    """硬盘"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s硬盘:%s,可以永久存储数据，容量大。" % (indent, self._name) )


class GraphicsCard(Component):
    """显卡"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s显卡:%s,可以高速计算和处理图形图像。" % (indent, self._name) )


class Battery(Component):
    """电源"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s电源:%s,可以持续给主板和外接配件供电。" % (indent, self._name) )


class Fan(Component):
    """风扇"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s风扇:%s，辅助CPU散热。" % (indent, self._name) )


class Displayer(Component):
    """"显示器"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s显示器:%s，负责内容的显示。" % (indent, self._name) )


class Composite(Component):
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


class Mainboard(Composite):
    """主板"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "主板:", end="")
        super().showInfo(indent)


class ComputerCase(Composite):
    """机箱"""

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "机箱:", end="")
        super().showInfo(indent)


class Computer(Composite):
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


# 基于框架的实现
#==============================


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

testComputer()