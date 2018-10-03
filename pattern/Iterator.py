#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 12/7/2017

# Version 1.0
#=======================================================================================================================

class Customer:
    """客户"""

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


class NumeralIterator:
    """迭代器"""

    def __init__(self, data):
        self.__data = data
        self.toBegin()

    def toBegin(self):
        """将指针移至起始位置"""
        self.__curIdx = -1

    def toEnd(self):
        """将指针移至结尾位置"""
        self.__curIdx = len(self.__data)

    def next(self):
        """移动至下一个元素"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def previous(self):
        "移动至上一个元素"
        if (self.__curIdx > 0):
            self.__curIdx -= 1
            return True
        else:
            return False

    def current(self):
        """获取当前的元素"""
        return self.__data[self.__curIdx] if (self.__curIdx < len(self.__data) and self.__curIdx >= 0) else None


class NumeralSystem:
    """排号系统"""

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
        print("%s 您好！您已在%s成功挂号，序号：%04d，请耐心等待！"
              % (customer.getName(), self.__name, customer.getNum()) )

    def getIterator(self):
        return NumeralIterator(self.__customers)


    # def visit(self):
    #     for customer in self.__customers:
    #         print("下一位病人 %04d(%s) 请到 %s 就诊。"
    #               % (customer.getNum(), customer.getName(), customer.getClinic()) )


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================


# 基于框架的实现
#==============================


# Test
#=======================================================================================================================

def testHospital():
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

    iterator = numeralSystem.getIterator()
    while(iterator.next()):
        customer = iterator.current()
        print("下一位病人 %04d(%s) 请到 %s 就诊。"
              % (customer.getNum(), customer.getName(), customer.getClinic()) )


    # print("从前往后遍历:")
    # iterator = numeralSystem.getIterator()
    # while(iterator.next()):
    #     customer = iterator.current()
    #     print("下一位病人", str(customer.getNum()).zfill(4), customer.getName(), "请到", customer.getClinic(),  "就诊。")
    #
    # print("从后往前遍历:")
    # iterator.toEnd()
    # while (iterator.previous()):
    #     customer = iterator.current()
    #     print("下一位病人", str(customer.getNum()).zfill(4), customer.getName(), "请到", customer.getClinic(), "就诊。")


    # numeralSystem.visit()



def testLoop():
    arr = [0, 1, 2, 3, 4, 5, 6, 7 ,8 , 9];
    for e in arr:
        print(e, end="\t")


#  方法一：使用()定义生成器
gen = (x * x for x in range(10))

#  方法二：使用yield定义generator函数
def fibonacci(maxNum):
    """斐波那契数列的生成器"""
    a = b = 1
    for i in range(maxNum):
        yield a
        a, b = b, a + b

def testIterable():
    print("方法一，0-9的平方数：")
    for e in gen:
        print(e, end="\t")
    print()

    print("方法二，斐波那契数列：")
    fib = fibonacci(10)
    for n in fib:
        print(n, end="\t")
    print()

    print("内置容器的for循环：")
    arr = [x * x for x in range(10)]
    for e in arr:
        print(e, end="\t")
    print()

    print()
    print(type(gen))
    print(type(fib))
    print(type(arr))


from collections import Iterable, Iterator
# 引入Iterable和Iterator

def testIsIterator():
    print("是否为Iterable对象：")
    print(isinstance([], Iterable))
    print(isinstance({}, Iterable))
    print(isinstance((1, 2, 3), Iterable))
    print(isinstance(set([1, 2, 3]), Iterable))
    print(isinstance("string", Iterable))
    print(isinstance(gen, Iterable))
    print(isinstance(fibonacci(10), Iterable))
    print("是否为Iterator对象：")
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))
    print(isinstance((1, 2, 3), Iterator))
    print(isinstance(set([1, 2, 3]), Iterable))
    print(isinstance("string", Iterator))
    print(isinstance(gen, Iterator))
    print(isinstance(fibonacci(10), Iterator))


def testNextItem():
    print("将Iterable对象转成Iterator对象：")
    l = [1, 2, 3]
    itrL = iter(l)
    print(next(itrL))
    print(next(itrL))
    print(next(itrL))

    print("next()函数遍历迭代器元素：")
    fib = fibonacci(4)
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    # print(next(fib))


testHospital()
# testLoop()
# testIterable()
# testIsIterator()
# testNextItem()

