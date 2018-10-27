#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 7/15/2018

# Version 1.0
#=======================================================================================================================
# class FilterScreen:
#     """过滤网"""
#
#     def doFilter(self, rawMaterials):
#         for material in rawMaterials:
#             if (material == "豆渣"):
#                 rawMaterials.remove(material)
#         return rawMaterials


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Filter(metaclass=ABCMeta):
    """过滤器"""

    @abstractmethod
    def doFilter(self, elements):
        """过滤方法"""
        pass


class FilterChain(Filter):
    """过滤器链"""

    def __init__(self):
        self._filters = []

    def addFilter(self, filter):
        self._filters.append(filter)

    def removeFilter(self, filter):
        self._filters.remove(filter)

    def doFilter(self, elements):
        for filter in self._filters:
            elements = filter.doFilter(elements)
        return elements


# 基于框架的实现
#==============================
class FilterScreen(Filter):
    """过滤网"""

    def doFilter(self, elements):
        for material in elements:
            if (material == "豆渣"):
                elements.remove(material)
        return elements


import re
# 引入正则表达式库

class SensitiveFilter(Filter):
    """敏感词过滤"""

    def __init__(self):
        self.__sensitives = ["黄色", "台独", "贪污"]

    def doFilter(self, elements):
        # 敏感词列表转换成正则表达式
        regex = ""
        for word in self.__sensitives:
            regex += word + "|"
        regex = regex[0: len(regex) - 1]

        # 对每个元素进行过滤
        newElements = []
        for element in elements:
            item, num = re.subn(regex, "", element)
            newElements.append(item)

        return newElements


class HtmlFilter(Filter):
    """HTML特殊字符转换"""

    def __init__(self):
        self.__wordMap = {
            "&": "&amp;",
            "'": " &apos;",
            ">": "&gt;",
            "<": "&lt;",
            "\"": " &quot;",
        }

    def doFilter(self, elements):
        newElements = []
        for element in elements:
            for key, value in self.__wordMap.items():
                element = element.replace(key, value)
            newElements.append(element)
        return newElements


# Test
#=======================================================================================================================

def testFilterScreen():
    rawMaterials = ["豆浆", "豆渣"]
    print("过滤前：", rawMaterials)
    filter = FilterScreen()
    filteredMaterials = filter.doFilter(rawMaterials)
    print("过滤后：",filteredMaterials)



def testFilter():
    rawMaterials = ["豆浆", "豆渣"]
    print("过滤前：", rawMaterials)
    filteredMaterials = list(filter(lambda material: material == "豆浆", rawMaterials))
    print("过滤后：", filteredMaterials)

def isSoybeanMilk(material):
    return material == "豆浆"



def testFiltercontent():
    contents = [
        '有人出售黄色书：<黄情味道>',
        '有人企图搞台独活动, ——"造谣咨询"',
    ]
    print("过滤前的内容：", contents)
    filterChain = FilterChain()
    filterChain.addFilter(SensitiveFilter())
    filterChain.addFilter(HtmlFilter())
    newContents = filterChain.doFilter(contents)
    print("过滤后的内容：", newContents)


# testFilterScreen()
# testFilter()
testFiltercontent()
