#!/usr/bin/python
# Authoer: Administrator
# Date: 12/7/2017

# Version 1.0
#=======================================================================================================================

class Customer:
    "客户"

    def __init__(self, name):
        self.__name = name
        self.__num = 0
        self.__clinics = None

    def getName(self):
        return self.__name

    def register(self, system):
        system.pushCustomer(self)

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    def setClinic(self, clinic):
        self.__clinics = clinic

    def getClinic(self):
        return self.__clinics


class Iterator:
    "迭代器"

    def __init__(self, data):
        self.__data = data
        self.toBegin()

    def toBegin(self):
        "将指针移至起始位置"
        self.__curIdx = -1

    def toEnd(self):
        "将指针移至结尾位置"
        self.__curIdx = len(self.__data)

    def next(self):
        "往前移动一个元素"
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def previous(self):
        "往后移动一个元素"
        if (self.__curIdx > 0):
            self.__curIdx -= 1
            return True
        else:
            return False

    def current(self):
        "获取当前的元素"
        return self.__data[self.__curIdx] if (len(self.__data) >= self.__curIdx) else None


class NumeralSystem:
    "排号系统"

    __clinics = ("1号分诊室", "2号分诊室", "3号分诊室")

    def __init__(self, name):
        self.__customers = []
        self.__curNum = 0
        self.__name = name

    def pushCustomer(self, customer):
        customer.setNum(self.__curNum + 1)
        click = NumeralSystem.__clinics[self.__curNum % len(NumeralSystem.__clinics)]
        customer.setClinic(click)
        self.__curNum += 1
        self.__customers.append(customer)
        print(customer.getName() + "您好！您已在" + self.__name+ "成功挂号，序号："
              + str(customer.getNum()).zfill(4) + "，请耐心等待！")

    def getIterator(self):
        return Iterator(self.__customers)


    def visit(self):
        for customer in self.__customers:
            print("下一位病人", str(customer.getNum()).zfill(4), customer.getName(),
                  "请到", customer.getClinic(), "就诊。")


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================


# 基于框架的实现
#==============================


# Test
#=======================================================================================================================

def testIterator():
    numeralSystem = NumeralSystem("挂号台")
    lily = Customer("Lily")
    lily.register(numeralSystem);
    pony = Customer("Pony")
    pony.register(numeralSystem)
    nick = Customer("Nick")
    nick.register(numeralSystem)
    tony = Customer("Tony")
    tony.register(numeralSystem)
    print()

    print("从前往后遍历:")
    iterator = numeralSystem.getIterator()
    while(iterator.next()):
        customer = iterator.current()
        print("下一位病人", str(customer.getNum()).zfill(4), customer.getName(), "请到", customer.getClinic(),  "就诊。")

    print("从后往前遍历:")
    iterator.toEnd()
    while (iterator.previous()):
        customer = iterator.current()
        print("下一位病人", str(customer.getNum()).zfill(4), customer.getName(), "请到", customer.getClinic(), "就诊。")


    # numeralSystem.visit()



testIterator()