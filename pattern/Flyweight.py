#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 6/4/2018

# Version 1.0
#=======================================================================================================================
import logging

class Pigment:
    "颜料"

    def __init__(self, color):
        self.__color = color
        self.__user = ""

    def getColor(self):
        return self.__color

    def setUser(self, user):
        self.__user = user
        return self

    def showInfo(self):
        print(self.__user + str("取得") + self.__color + "色颜料")

class PigmengFactory:
    "资料的工厂类"

    def __init__(self):
        self.__sigmentPool = {
            '红': Pigment('红'),
            '黄': Pigment('黄'),
            '蓝': Pigment('蓝'),
            '绿': Pigment('绿'),
            '紫': Pigment('紫'),
        }

    def getPigment(self, color):
        pigment = self.__sigmentPool.get(color)
        if pigment is None:
            logging.error("没有%s颜色的颜料！", color)
        return pigment


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================


# 基于框架的实现
#==============================


# Test
#=======================================================================================================================
def testPigment():
    factory = PigmengFactory()
    pigmentRed = factory.getPigment('红').setUser('梦之队')
    pigmentRed.showInfo()
    pigmentYellow = factory.getPigment('黄').setUser('梦之队')
    pigmentYellow.showInfo()
    pigmentBlue1 = factory.getPigment('蓝').setUser('梦之队')
    pigmentBlue1.showInfo()
    pigmentBlue2 = factory.getPigment('蓝').setUser('和平队')
    pigmentBlue2.showInfo()





# print("Blue1:" + str(id(pigmentBlue1)) + ", Bule2:" + str(id(pigmentBlue2))
#       + ", Blue1==Blue2:" + str(pigmentBlue1 == pigmentBlue2))



testPigment()