#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 11/12/2017

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class ReceiveParcel(metaclass=ABCMeta):
    """接收包裹抽象类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def receive(self, parcelContent):
        pass


# class TonyReception(ReceiveParcel):
#     """Tony接收"""
#
#     def __init__(self, name, phoneNum):
#         super().__init__(name)
#         self.__phoneNum = phoneNum
#
#     def getPhoneNum(self):
#         return self.__phoneNum
#
#     def receive(self, parcelContent):
#         print("货物主人：%s，手机号：%s" % (self.getName(), self.getPhoneNum()) )
#         print("接收到一个包裹，包裹内容：%s" % parcelContent)
#
#
# class WendyReception(ReceiveParcel):
#     """Wendy代收"""
#
#     def __init__(self, name, receiver):
#         super().__init__(name)
#         self.__receiver = receiver
#
#     def receive(self, parcelContent):
#         print("我是%s的朋友，我来帮他代收快递！" % (self.__receiver.getName() + "") )
#         if(self.__receiver is not None):
#             self.__receiver.receive(parcelContent)
#         print("代收人：%s" % self.getName())


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Subject(metaclass=ABCMeta):
    """主题类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def request(self, content = ''):
        pass


class RealSubject(Subject):
    """真实主题类"""

    def request(self, content):
        print("RealSubject todo something...")


class ProxySubject(Subject):
    """代理主题类"""

    def __init__(self, name, subject):
        super().__init__(name)
        self._realSubject = subject

    def request(self, content = ''):
        self.preRequest()
        if(self._realSubject is not None):
            self._realSubject.request(content)
        self.afterRequest()

    def preRequest(self):
        print("preRequest")

    def afterRequest(self):
        print("afterRequest")


# 基于框架的实现
#==============================

class TonyReception(Subject):
    """Tony接收"""

    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum

    def getPhoneNum(self):
        return self.__phoneNum

    def request(self, content):
        print("货物主人：%s，手机号：%s" % (self.getName(), self.getPhoneNum()))
        print("接收到一个包裹，包裹内容：%s" % str(content))


class WendyReception(ProxySubject):
    """Wendy代收"""

    def __init__(self, name, receiver):
        super().__init__(name, receiver)

    def preRequest(self):
        print("我是%s的朋友，我来帮他代收快递！" % (self._realSubject.getName() + ""))

    def afterRequest(self):
        print("代收人：%s" % self.getName())


# Test
#=======================================================================================================================
def testReceiveParcel():
    tony = TonyReception("Tony", "18512345678")
    print("Tony接收：")
    tony.receive("雪地靴")
    print()

    print("Wendy代收：")
    wendy = WendyReception("Wendy", tony)
    wendy.receive("雪地靴")


def testProxy():
    realObj = RealSubject('RealSubject')
    proxyObj = ProxySubject('ProxySubject', realObj)
    proxyObj.request()

def testReceiveParcel2():
    tony = TonyReception("Tony", "18512345678")
    print("Tony接收：")
    tony.request("雪地靴")
    print()

    print("Wendy代收：")
    wendy = WendyReception("Wendy", tony)
    wendy.request("雪地靴")

# testReceiveParcel()
# testProxy()
testReceiveParcel2()

