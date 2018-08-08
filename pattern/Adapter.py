#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 4/24/2018

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class IHightPerson(metaclass=ABCMeta):
    """接口类，提供空实现的方法，由子类去实现"""

    @abstractmethod
    def getName(self):
        """获取姓名"""
        pass

    @abstractmethod
    def getHeight(self):
        """获取身高"""
        pass

    @abstractmethod
    def appearance(self, person):
        """外貌"""
        pass


class HighPerson(IHightPerson):
    """个高的人"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getHeight(self):
        return 170

    def appearance(self):
        print(self.getName() + "身高" + str(self.getHeight()) + "，完美如你，天生的美女！")


class ShortPerson:
    """个矮的人"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getRealHeight(self):
        return 160

    def getShoesHeight(self):
        return 6


class DecoratePerson(ShortPerson, IHightPerson):
    """有高跟鞋搭配的人"""

    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        return super().getName()

    def getHeight(self):
        return super().getRealHeight() + super().getShoesHeight()

    def appearance(self):
        print(self.getName() + "身高" + str(self.getHeight()) + ", 在高跟鞋的适配下，你身高不输高圆圆，气质不输范冰冰！")


class Hotel:
    """(高级)酒店"""

    def recruit(self, person):
        """
        :param person: IHightPerson的对象
        """
        suitable = self.receptionistSuitable(person)
        print(person.getName() + "是否适合做接待员：", "符合" if suitable else "不符合")

    def receptionistSuitable(self, person):
        """
        是否可以成为(高级酒店)接待员
        :param person: IHightPerson的对象
        :return: 是否符合做接待员的条件
        """
        return person.getHeight() >= 165;


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Target(metaclass=ABCMeta):
    """目标类"""

    @abstractmethod
    def function(self):
        pass


class Adaptee:
    """源对象类"""

    def speciaficFunction(self):
        print("被适配对象的特殊功能")

class Adapter(Adaptee, Target):
    """适配器"""

    def function(self):
        print("进行功能的转换")



# 基于框架的实现
#==============================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
import os
# 导入os库,用于文件、路径相关的解析

class Page:
    """电子书一页的内容"""
    def __init__(self, pageNum):
        self.__pageNum = pageNum

    def getContent(self):
        return "第 " + str(self.__pageNum) + " 页的内容..."


class Catalogue:
    """目录结构"""

    def __init__(self, title):
        self.__title = title
        self.__chapters = []

    def addChapter(self, title):
        self.__chapters.append(title)

    def showInfo(self):
        print("书名：" + self.__title)
        print("目录:")
        for chapter in self.__chapters:
            print("    " + chapter)


class IBook(metaclass=ABCMeta):
    """电子书文档的接口类"""

    @abstractmethod
    def parseFile(self, filePath):
        """解析文档"""
        pass

    @abstractmethod
    def getCatalogue(self):
        """获取目录"""
        pass

    @abstractmethod
    def getPageCount(self):
        """获取页数"""
        pass

    @abstractmethod
    def getPage(self, pageNum):
        """获取第pageNum页的内容"""
        pass


class TxtBook(IBook):
    """TXT解析类"""

    def parseFile(self, filePath):
        # 模拟文档的解析
        print(filePath + " 文件解析成功")
        self.__title = os.path.splitext(filePath)[0]
        self.__pageCount = 500
        return True

    def getCatalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.addChapter("第一章 标题")
        catalogue.addChapter("第二章 标题")
        return catalogue

    def getPageCount(self):
        return self.__pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class EpubBook(IBook):
    """Epub解析类"""

    def parseFile(self, filePath):
        # 模拟文档的解析
        print(filePath + " 文件解析成功")
        self.__title = os.path.splitext(filePath)[0]
        self.__pageCount = 800
        return True

    def getCatalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.addChapter("第一章 标题")
        catalogue.addChapter("第二章 标题")
        return catalogue

    def getPageCount(self):
        return self.__pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class Outline:
    """第三方PDF解析库的目录类"""
    def __init__(self):
        self.__outlines = []

    def addOutline(self, title):
        self.__outlines.append(title)

    def getOutlines(self):
        return self.__outlines


class PdfPage:
    "PDF页"

    def __init__(self, pageNum):
        self.__pageNum = pageNum

    def getPageNum(self):
        return self.__pageNum


class ThirdPdf:
    """第三方PDF解析库"""

    def __init__(self):
        self.__pageSize = 0

    def open(self, filePath):
        print("第三方库解析PDF文件：" + filePath)
        self._title = os.path.splitext(filePath)[0]
        self.__pageSize = 1000
        return True

    def getOutline(self):
        outline = Outline()
        outline.addOutline("第一章 PDF电子书标题")
        outline.addOutline("第二章 PDF电子书标题")
        return outline

    def pageSize(self):
        return self.__pageSize

    def page(self, index):
        return PdfPage(index)

class PdfAdapterBook(ThirdPdf, IBook):
    """对第三方的PDF解析库重新进行包装"""

    def parseFile(self, filePath):
        # 模拟文档的解析
        rtn = super().open(filePath)
        if(rtn):
            print(filePath + "文件解析成功")
        return rtn

    def getCatalogue(self):
        outline = self.getOutline()
        print("将Outline结构的目录转换成Catalogue结构的目录")
        catalogue = Catalogue(self._title)
        for title in outline.getOutlines():
            catalogue.addChapter(title)
        return catalogue

    def getPageCount(self):
        return super().pageSize()

    def getPage(self, pageNum):
        page = self.page(pageNum)
        print("将PdfPage的面对象转换成Page的对象")
        return Page(page.getPageNum())


class Reader:
    "阅读器"

    def __init__(self, name):
        self.__name = name
        self.__filePath = ""
        self.__curBook = None
        self.__curPageNum = -1

    def __initBook(self, filePath):
        self.__filePath = filePath
        extName = os.path.splitext(filePath)[1]
        if(extName.lower() == ".epub"):
            self.__curBook = EpubBook()
        elif(extName.lower() == ".txt"):
            self.__curBook = TxtBook()
        elif(extName.lower() == ".pdf"):
            self.__curBook = PdfAdapterBook()
        else:
            self.__curBook = None

    def openFile(self, filePath):
        self.__initBook(filePath)
        if(self.__curBook is not None):
            rtn = self.__curBook.parseFile(filePath)
            if(rtn):
                self.__curPageNum = 1
            return rtn
        return False

    def closeFile(self):
        print("关闭 " + self.__filePath + " 文件")
        return True

    def showCatalogue(self):
        catalogue = self.__curBook.getCatalogue()
        catalogue.showInfo()

    def prePage(self):
        print("往前翻一页：", end="")
        return self.gotoPage(self.__curPageNum - 1)

    def nextPage(self):
        print("往后翻一页：", end="")
        return self.gotoPage(self.__curPageNum + 1)

    def gotoPage(self, pageNum):
        if(pageNum > 1 and pageNum < self.__curBook.getPageCount() -1):
            self.__curPageNum = pageNum

        print("显示第" + str(self.__curPageNum) + "页")
        page = self.__curBook.getPage(self.__curPageNum)
        page.getContent()
        return page


# Test
#=======================================================================================================================

def testPerson():
    lira = HighPerson("Lira")
    lira.appearance()
    demi = DecoratePerson("Demi");
    demi.appearance()
    hotel = Hotel()
    hotel.recruit(lira)
    hotel.recruit(demi)

def testAdapter():
    adpater = Adapter()
    adpater.function()

def testReader():
    reader = Reader("阅读器")
    if(not reader.openFile("平凡的世界.txt")):
        return
    reader.showCatalogue()
    reader.prePage()
    reader.nextPage()
    reader.nextPage()
    reader.closeFile()
    print()

    if (not reader.openFile("追风筝的人.epub")):
        return
    reader.showCatalogue()
    reader.nextPage()
    reader.nextPage()
    reader.prePage()
    reader.closeFile()
    print()

    if (not reader.openFile("如何从生活中领悟设计模式.pdf")):
        return
    reader.showCatalogue()
    reader.nextPage()
    reader.nextPage()
    reader.closeFile()


# testPerson()
testAdapter()
# testReader()