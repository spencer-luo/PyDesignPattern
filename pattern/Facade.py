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


# Test
#=======================================================================================================================
def testRegister():
    volunteer = Volunteer("Frank")
    volunteer.welcomeFreshmen("Tony")


testRegister()