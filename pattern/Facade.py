#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 6/23/2018

# Version 1.0
#=======================================================================================================================
class Register:
    "入学报到"

    def register(self, name):
        print("活动中心:" + name + "同学报到成功！")


class Payment:
    "缴费"

    def pay(self, name, money):
        print("缴费中心:" + "收到" + name + "同学" + str(money) + "元付款，缴费成功！")


class DormitoryManagementCenter:
    "宿舍管理中心(生活中心)"

    def provideLivingGoods(self, name):
        print("生活中心:" + name + "同学的生活用品已发放。")


class Dormitory:
    "宿舍"

    def meetRoommate(self, name):
        print("宿    舍:" + "大家好！这是刚来的" + name + "同学，是你们未来需要共度四年的室友！相互认识一下……")


class Volunteer:
    "迎新志愿者"

    def __init__(self, name):
        self.__name = name
        self.__register = Register()
        self.__payment = Payment()
        self.__lifeCenter = DormitoryManagementCenter()
        self.__dormintory = Dormitory()

    def welcomeFreshmen(self, name):
        print("你好," + name + "同学! 我是新生报到的志愿者" + self.__name
              + "，我将带你完成整个报到流程。")
        self.__register.register(name)
        self.__payment.pay(name, 10000)
        self.__lifeCenter.provideLivingGoods(name)
        self.__dormintory.meetRoommate(name)


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================


# 基于框架的实现
#==============================
from os import path
import logging

class ZIPModel:
    "ZIP模块，负责ZIP文件的压缩与解压"

    def compress(self, srcFilePath, dstFilePath):
        print("ZIP模块正在进行 '" + srcFilePath + "' 文件的压缩......")
        print("文件压缩成功，已保存至 '" + dstFilePath + "'")

    def decompress(self, srcFilePath, dstFilePath):
        print("ZIP模块正在进行 '" + srcFilePath + "' 文件的解压......")
        print("文件解压成功，已保存至 '" + dstFilePath+ "'")


class RARModel:
    "RAR模块，负责ZIP文件的压缩与解压"

    def compress(self, srcFilePath, dstFilePath):
        print("RAR模块正在进行 '" + srcFilePath + "' 文件的压缩......")
        print("文件压缩成功，已保存至 '" + dstFilePath + "'")

    def decompress(self, srcFilePath, dstFilePath):
        print("RAR模块正在进行 '" + srcFilePath + "' 文件的解压......")
        print("文件解压成功，已保存至 '" + dstFilePath + "'")


class ZModel:
    "7Z模块，负责7Z文件的压缩与解压"

    def compress(self, srcFilePath, dstFilePath):
        print("7Z模块正在进行 '" + srcFilePath + "' 文件的压缩......")
        print("文件压缩成功，已保存至 '" + dstFilePath + "'")

    def decompress(self, srcFilePath, dstFilePath):
        print("7Z模块正在进行 '" + srcFilePath + "' 文件的解压......")
        print("文件解压成功，已保存至 '" + dstFilePath + "'")


class CompressionFacade:
    "压缩系统的外观类"

    def __init__(self):
        self.__zipModel = ZIPModel()
        self.__rarModel = RARModel()
        self.__zModel = ZModel()

    def compress(self, srcFilePath, dstFilePath, type):
        "根据不同的压缩类型，压缩成不同的格式"
        # 获取新的文件名
        extName = "." + type
        fullName = dstFilePath + extName
        if (type.lower() == "zip") :
            self.__zipModel.compress(srcFilePath, fullName)
        elif(type.lower() == "rar"):
            self.__rarModel.compress(srcFilePath, fullName)
        elif(type.lower() == "7z"):
            self.__zModel.compress(srcFilePath, fullName)
        else:
            logging.error("Not support this format:" + str(type))
            return False
        return True

    def decompress(self, srcFilePath, dstFilePath):
        "从srcFilePath中获取后缀，根据不同的后缀名(拓展名)，进行不同格式的解压"
        baseName = path.basename(srcFilePath)
        extName = baseName.split(".")[1]
        if (extName.lower() == "zip") :
            self.__zipModel.decompress(srcFilePath, dstFilePath)
        elif(extName.lower() == "rar"):
            self.__rarModel.decompress(srcFilePath, dstFilePath)
        elif(extName.lower() == "7z"):
            self.__zModel.decompress(srcFilePath, dstFilePath)
        else:
            logging.error("Not support this format:" + str(extName))
            return False
        return True


# Test
#=======================================================================================================================
def testRegister():
    volunteer = Volunteer("Frank")
    volunteer.welcomeFreshmen("Tony")


def testCompression():
    facade = CompressionFacade()
    facade.compress("E:\生活中的设计模式\生活中的外观模式——学妹别慌，学长帮你.md",
                    "E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你", "zip")
    facade.decompress("E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你.zip",
                      "E:\解析文件\生活中的外观模式——学妹别慌，学长帮你.md")
    print()

    facade.compress("E:\生活中的设计模式\生活中的外观模式——学妹别慌，学长帮你.md",
                    "E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你", "rar")
    facade.decompress("E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你.rar",
                      "E:\解析文件\生活中的外观模式——学妹别慌，学长帮你.md")
    print()

    facade.compress("E:\生活中的设计模式\生活中的外观模式——学妹别慌，学长帮你.md",
                    "E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你", "7z")
    facade.decompress("E:\压缩文件\生活中的外观模式——学妹别慌，学长帮你.7z",
                      "E:\解析文件\生活中的外观模式——学妹别慌，学长帮你.md")
    print()


def testPath():
    filePath = "E:\解析文件\生活中的外观模式——学妹别慌，学长帮你.md"
    dirName = path.dirname(filePath)
    baseName = path.basename(filePath)
    fileName, extName = baseName.split('.')
    fullName = path.join(dirName, fileName + extName)
    i = 0


# testRegister()
testCompression()
# testPath()