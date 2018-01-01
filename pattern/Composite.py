#!/usr/bin/python
# Authoer: Administrator
# Date: 12/16/2017

# Version 1.0
#=======================================================================================================================
class Component:
    "组件，所有子配件的基类"

    def __init__(self, name):
        self._name = name

    def showInfo(self, indent = ""):
        pass

    def isComposite(self):
        return False

    def startup(self, indent = ""):
        print(indent + self._name + " 准备开始工作...")

    def shutdown(self, indent = ""):
        print(indent + self._name + " 即将结束工作...")


class CPU(Component):
    "中央处理器"

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent, end="")
        print("CPU:" + self._name + ",可以进行高速计算。")


class MemoryCard(Component):
    "内存条"

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent, end="")
        print("内存:" + self._name + ",可以缓存数据，读写速度快。")


class HardDisk(Component):
    "硬盘"

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent, end="")
        print("硬盘:" + self._name + ",可以永久存储数据，容量大。")


class GraphicsCard(Component):
    "显卡"

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent, end="")
        print("显卡:" + self._name + ",可以高速计算和处理图形图像。")


class Battery(Component):
    "电源"

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent, end="")
        print("电源:" + self._name + ",可以持续给主板和外接配件供电。")


class Fan(Component):
    "风扇"

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent, end="")
        print("风扇:" + self._name + "，辅助CPU散热。")


class Displayer(Component):
    "显示器"

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent, end="")
        print("显示器:" + self._name + "，负责内容的显示。")


class Composite(Component):
    "配件组合器"

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def showInfo(self, indent):
        print(self._name + ",由以下部件组成:")
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
        super().startup(indent)
        indent += "\t"
        for element in self._components:
            element.shutdown(indent)


class Mainboard(Composite):
    "主板"

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "主板:", end="")
        super().showInfo(indent)


class ComputerCase(Composite):
    "机箱"

    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "机箱:", end="")
        super().showInfo(indent)


class Computer(Composite):
    "电脑"

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
    cpu = CPU("Intel Core i5-6600K")
    memoryCard = MemoryCard("Kingston Fury DDR4")
    hardDisk = HardDisk("Kingston V300 ")
    graphicsCard = GraphicsCard("Colorful iGame750")
    mainBoard = Mainboard("GIGABYTE Z170M M-ATX")
    mainBoard.addComponent(cpu)
    mainBoard.addComponent(memoryCard)
    mainBoard.addComponent(hardDisk)
    mainBoard.addComponent(graphicsCard)

    battery = Battery("Antec VP 450P")
    fan = Fan("DEEPCOOL 120T")
    computerCase = ComputerCase("SAMA MATX")
    computerCase.addComponent(battery)
    computerCase.addComponent(mainBoard)
    computerCase.addComponent(fan)

    displayer = Displayer("AOC LV243XIP")

    computer = Computer("Tony DIY电脑")
    computer.addComponent(displayer)
    computer.addComponent(computerCase)

    computer.showInfo("")
    print("\n开机过程:")
    computer.startup("")
    print("\n关机过程:")
    computer.shutdown("")

testComputer()