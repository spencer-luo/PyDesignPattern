##!/usr/bin/python

# Version 1.0
########################################################################################################################
# from abc import ABCMeta, abstractmethod
# # 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
#
# class Person:
#     """请假申请人"""
#     def __init__(self, name, dayoff, reason):
#         self.__name = name
#         self.__dayoff = dayoff
#         self.__reason = reason
#         self.__leader = None
#
#     def getName(self):
#         return self.__name
#
#     def getDayOff(self):
#         return self.__dayoff
#
#     def getReason(self):
#         return self.__reason
#
#     def setLeader(self, leader):
#         self.__leader = leader
#
#     def reuqest(self):
#         print("%s 申请请假 %d 天。请假事由：%s" % (self.__name, self.__dayoff, self.__reason) )
#         if( self.__leader is not None):
#             self.__leader.handleRequest(self)
#
#
# class Manager(metaclass=ABCMeta):
#     """公司管理人员"""
#
#     def __init__(self, name, title):
#         self.__name = name
#         self.__title = title
#         self._nextHandler = None
#
#     def getName(self):
#         return self.__name
#
#     def getTitle(self):
#         return self.__title
#
#     def setNextHandler(self, nextHandler):
#         self._nextHandler = nextHandler
#
#     @abstractmethod
#     def handleRequest(self, person):
#         pass
#
# class Supervisor(Manager):
#     """主管"""
#
#     def __init__(self, name, title):
#         super().__init__(name, title)
#
#     def handleRequest(self, person):
#         if(person.getDayOff() <= 2):
#             print("同意 %s 请假，签字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()) )
#         if(self._nextHandler is not None):
#             self._nextHandler.handleRequest(person)
#
#
# class DepartmentManager(Manager):
#     """部门总监"""
#     def __init__(self, name, title):
#         super().__init__(name, title)
#
#     def handleRequest(self, person):
#         if(person.getDayOff() >2 and person.getDayOff() <= 5):
#             print("同意 %s 请假，签字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()))
#         if(self._nextHandler is not None):
#             self._nextHandler.handleRequest(person)
#
# class CEO(Manager):
#     """CEO"""
#
#     def __init__(self, name, title):
#         super().__init__(name, title)
#
#     def handleRequest(self, person):
#         if (person.getDayOff() > 5 and person.getDayOff() <= 22):
#             print("同意 %s 请假，签字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()))
#
#         if (self._nextHandler is not None):
#             self._nextHandler.handleRequest(person)
#
# class Administrator(Manager):
#     """行政人员"""
#
#     def __init__(self, name, title):
#         super().__init__(name, title)
#
#     def handleRequest(self, person):
#         print("%s 的请假申请已审核，情况属实！已备案处理。处理人：%s(%s)\n" % (person.getName(), self.getName(), self.getTitle()))


# Version 2.0
########################################################################################################################
# 代码框架
##################
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Request:
    """请求(内容)"""

    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None

    def getName(self):
        return self.__name

    def getDayOff(self):
        return self.__dayoff

    def getReason(self):
        return self.__reason


class Responsible(metaclass=ABCMeta):
    """责任人抽象类"""

    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self._nextHandler = None

    def getName(self):
        return self.__name

    def getTitle(self):
        return self.__title

    def setNextHandler(self, nextHandler):
        self._nextHandler = nextHandler

    def getNextHandler(self):
        return self._nextHandler

    def handleRequest(self, request):
        """请求处理"""
        # 当前责任人处理请求
        self._handleRequestImpl(request)
        # 如果存在下一个责任人，则将请求传递(提交)给下一个责任人
        if (self._nextHandler is not None):
            self._nextHandler.handleRequest(request)

    @abstractmethod
    def _handleRequestImpl(self, request):
        """真正处理请求的方法"""
        pass


# 基于框架的实现
##################
class Person:
    """请求者(请假人)"""

    def __init__(self, name):
        self.__name = name
        self.__leader = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setLeader(self, leader):
        self.__leader = leader

    def getLeader(self):
        return self.__leader

    def sendReuqest(self, request):
        print("%s 申请请假 %d 天。请假事由：%s" % (self.__name, request.getDayOff(), request.getReason()))
        if (self.__leader is not None):
            self.__leader.handleRequest(request)


class Supervisor(Responsible):
    """主管"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() <= 2):
            print("同意 %s 请假，签字人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))


class DepartmentManager(Responsible):
    """部门总监"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() > 2 and request.getDayOff() <= 5):
            print("同意 %s 请假，签字人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))


class CEO(Responsible):
    """CEO"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if (request.getDayOff() > 5 and request.getDayOff() <= 22):
            print("同意 %s 请假，签字人：%s(%s)" % (request.getName(), self.getName(), self.getTitle()))


class Administrator(Responsible):
    """行政人员"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        print("%s 的请假申请已审核，情况属实！已备案处理。处理人：%s(%s)\n" % (request.getName(), self.getName(), self.getTitle()))

# Test
########################################################################################################################
# def testAskForLeave():
#     directLeader = Supervisor("Eren", "客户端研发部经理")
#     departmentLeader = DepartmentManager("Eric", "技术研发中心总监")
#     ceo = CEO("Helen", "创新文化公司CEO")
#     administrator = Administrator("Nina", "行政中心总监")
#     directLeader.setNextHandler(departmentLeader)
#     departmentLeader.setNextHandler(ceo)
#     ceo.setNextHandler(administrator)
#
#     sunny = Person("Sunny", 1, "参加MDCC大会。")
#     sunny.setLeader(directLeader)
#     sunny.reuqest()
#     tony = Person("Tony", 5, "家里有紧急事情！")
#     tony.setLeader(directLeader)
#     tony.reuqest()
#     pony = Person("Pony", 15, "出国深造。")
#     pony.setLeader(directLeader)
#     pony.reuqest()


def testChainOfResponsibility():
    directLeader = Supervisor("Eren", "客户端研发部经理")
    departmentLeader = DepartmentManager("Eric", "技术研发中心总监")
    ceo = CEO("Helen", "创新文化公司CEO")
    administrator = Administrator("Nina", "行政中心总监")
    directLeader.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(ceo)
    ceo.setNextHandler(administrator)

    sunny = Person("Sunny")
    sunny.setLeader(directLeader)
    sunny.sendReuqest(Request(sunny.getName(), 1, "参加MDCC大会。"))
    tony = Person("Tony")
    tony.setLeader(directLeader)
    tony.sendReuqest(Request(tony.getName(), 5, "家里有紧急事情！"))
    pony = Person("Pony")
    pony.setLeader(directLeader)
    pony.sendReuqest(Request(pony.getName(), 15, "出国深造。"))


# testAskForLeave()
testChainOfResponsibility()