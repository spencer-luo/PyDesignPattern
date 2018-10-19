#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 5/19/2018

# Version 1.0
#=======================================================================================================================
class Engineer:
    """工程师"""

    def __init__(self, name):
        self.__name = name
        self.__workItems = []

    def addWorkItem(self, item):
        self.__workItems.append(item)

    def forget(self):
        self.__workItems.clear()
        print(self.__name + "工作太忙了，都忘记要做什么了！")

    def writeTodoList(self):
        """将工作项记录TodoList"""
        todoList = TodoList()
        for item in self.__workItems:
            todoList.writeWorkItem(item)
        return todoList

    def retrospect(self, todoList):
        """回忆工作项"""
        self.__workItems = todoList.getWorkItems()
        print(self.__name + "想起要做什么了！")

    def showWorkItem(self):
        if(len(self.__workItems)):
            print(self.__name + "的工作项：")
            for idx in range(0, len(self.__workItems)):
                print(str(idx + 1) + ". " + self.__workItems[idx] + ";")
        else:
            print(self.__name + "暂无工作项！")


class TodoList:
    """工作项"""

    def __init__(self):
        self.__workItems = []

    def writeWorkItem(self, item):
        self.__workItems.append(item)

    def getWorkItems(self):
        return self.__workItems


class TodoListCaretaker:
    """TodoList管理类"""

    def __init__(self):
        self.__todoList = None

    def setTodoList(self, todoList):
        self.__todoList = todoList

    def getTodoList(self):
        return self.__todoList


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
from copy import deepcopy

class Memento:
    """备忘录"""

    def setAttributes(self, dict):
        """深度拷贝字典dict中的所有属性"""
        self.__dict__ = deepcopy(dict)

    def getAttributes(self):
        """获取属性字典"""
        return self.__dict__


class Caretaker:
    """备忘录管理类"""

    def __init__(self):
        self._mementos = {}

    def addMemento(self, name, memento):
        self._mementos[name] = memento

    def getMemento(self, name):
        return self._mementos[name]

class Originator:
    """备份发起人"""

    def createMemento(self):
        memento = Memento()
        memento.setAttributes(self.__dict__)
        return memento

    def restoreFromMemento(self, memento):
        self.__dict__.update(memento.getAttributes())


# 基于框架的实现
#==============================

# Test
#=======================================================================================================================

def testEngineer():
    tony = Engineer("Tony")
    tony.addWorkItem("解决线上部分用户因昵称太长而无法显示全的问题")
    tony.addWorkItem("完成PDF的解析")
    tony.addWorkItem("在阅读器中显示PDF第一页的内容")
    tony.showWorkItem()
    caretaker = TodoListCaretaker()
    caretaker.setTodoList(tony.writeTodoList())

    print()
    tony.forget()
    tony.showWorkItem()

    print()
    tony.retrospect(caretaker.getTodoList())
    tony.showWorkItem()

# testEngineer()