#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 7/14/2018

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Expression(metaclass=ABCMeta):
    """抽象表达式"""

    @abstractmethod
    def interpreter(self, var):
        pass


class VarExpression(Expression):
    """变量解析器"""

    def __init__(self, key):
        self.__key = key

    def interpreter(self, var):
        return var.get(self.__key)


class SymbolExpression(Expression):
    """运算符解析器，运算符的抽象类"""

    def __init__(self, left, right):
        self._left = left
        self._right = right


class AddExpression(SymbolExpression):
    """加法解析器"""

    def __init__(self, left, right):
        super().__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) + self._right.interpreter(var)


class SubExpression(SymbolExpression):
    """减法解析器"""

    def __init__(self, left, right):
        super().__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) - self._right.interpreter(var)



class Stack:
    """封装一个堆栈类"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Calculator:
    """计算器类"""

    def __init__(self, text):
        self.__expression = self.parserText(text)

    def parserText(self, expText):
        # 定义一个栈，处理运算的先后顺序
        stack = Stack()
        left = right = None # 左右表达式
        idx = 0
        while(idx < len(expText)):
            if (expText[idx] == '+'):
                left = stack.pop()
                idx += 1
                right = VarExpression(expText[idx])
                stack.push(AddExpression(left, right))
            elif(expText[idx] == '-'):
                left = stack.pop()
                idx += 1
                right = VarExpression(expText[idx])
                stack.push(SubExpression(left, right))
            else:
                stack.push(VarExpression(expText[idx]))
            idx += 1
        return stack.pop()

    def run(self, var):
        return self.__expression.interpreter(var)





# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================


# 基于框架的实现
#==============================


# Test
#=======================================================================================================================

def testStack():
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())



def testCalculator():
    # 获取表达式
    expStr = input("请输入表达式：");
    # 获取各参数的键值对
    newExp, expressionMap = getMapValue(expStr)
    calculator = Calculator(newExp)
    result = calculator.run(expressionMap)
    print("运算结果为:" + expStr + " = " + str(result))

def getMapValue(expStr):
    preIdx = 0
    expressionMap = {}
    newExp = []
    for i in range(0, len(expStr)):
        if (expStr[i] == '+' or expStr[i] == '-'):
            key = expStr[preIdx:i]
            key = key.strip()  # 去除前后空字符
            newExp.append(key)
            newExp.append(expStr[i])
            var = input("请输入参数" + key + "的值：");
            var = var.strip()
            expressionMap[key] = float(var)
            preIdx = i + 1

    # 处理最后一个参数
    key = expStr[preIdx:len(expStr)]
    key = key.strip()  # 去除前后空字符
    newExp.append(key)
    var = input("请输入参数" + key + "的值：");
    var = var.strip()
    expressionMap[key] = float(var)

    return newExp, expressionMap


# testStack()
testCalculator()