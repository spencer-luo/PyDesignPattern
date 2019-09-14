#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 11/21/2017

# Version 1.0
#=======================================================================================================================
def testDataType():
    age = 18        # int
    weight = 62.51  # float
    isAdult = True  # bool，只有True和False两个枚举值
    name = "Tony"   # string
    print("age:", age, " type:", type(age))
    print("weight:", weight, " type:", type(weight))
    print("isAdult:", isAdult, " type:", type(isAdult))
    print("name:", name, " type:", type(name))

    # 变量的类型可以直接改变
    age = name
    print("age:", age)

    a = b = c = 5
    # a,b,c三个变量指向相同的内存空间，具有相同的值
    print("a:", a, "b:", b, "c:", c)
    print("id(a):", id(a), "id(b):", id(b), "id(c):", id(c))


def testList():
    list1 = ['Thomson', 78, 12.58, 'Sunny', 180.2]
    list2 = [123, 'Tony']
    print("list1:", list1)  # 输出完整列表
    print("list1[0]:", list1[0])  # 输出列表的第一个元素
    print("list1[1:3]:", list1[1:3])  # 输出第二个至第三个元素
    print("list1[2:]:", list1[2:])  # 输出从第三个开始至列表末尾的所有元素
    print("list2 * 2 :", list2 * 2)  # 输出列表两次
    print("list1 + list2 :", list1 + list2)  # 打印组合的列表
    list1[1] = 100
    print("设置list[1]:", list1)  # 输出完整列表
    list1.append("added data")
    print("list添加元素:", list1)  # 输出增加后的列表


def testTuple():
    tp1 = ('Thomson', 78, 12.58, 'Sunny', 180.2)
    tp2 = (123, 'Tony')
    print("tp1:", tp1)  # 输出完整元组
    print("tp2:", tp2)  # 输出完整元组
    print("tp1[0]:", tp1[0])  # 输出元组的第一个元素
    print("tp1[1:3]:", tp1[1:3])  # 输出第二个至第三个的元素
    print("tp1[2:]:", tp1[2:])  # 输出从第三个开始至列表末尾的所有元素
    print("tp2 * 2:", tp2 * 2)  # 输出元组两次
    print("tp1 + tp2:", tp1 + tp2)  # 打印组合的元组
    # tp1[1] = 100 # 不能修改元组内的元素


def testDictionary():
    dict1 = {}
    dict1['one'] = "This is one"
    dict1[2] = "This is two"
    dict2 = {'name': 'Tony', 'age': 24, 'height': 177}

    print("dict1:", dict1)
    print("dict1['one']:", dict1['one'])  # 输出键为'one' 的值
    print("dict1[2]:", dict1[2])  # 输出键为 2 的值
    print("dict2:", dict2) # 输出完整的字典
    print("dict2.keys():", dict2.keys())  # 输出所有键
    print("dict2.values():", dict2.values())  # 输出所有值


def testSet():
    friuts = {"apple", "orange", "strawberry", "banana", "apple", "strawberry"}
    print("friuts:", friuts)
    print("type of friuts:", type(friuts))
    arr = [1, 2, 3, 4, 5, 1]
    numbers = set(arr)
    print("numbers:", numbers)
    friuts.add(1)
    print("numbers add 1:", numbers)

class Test:
    "这是一个测试类"

    def __init__(self):
        self.__ivalue = 5

    def getvalue(self):
        return self.__ivalue

def testClass():
    t = Test()
    print(t.getvalue())


class Person:
    "人"
    visited = 0

    def __init__(self, name, age, height):
        self.__name = name      # 私有成员，访问权限为private
        self._age = age         # 保护成员，访问权限为protected
        self.height = height    # 公有成员，访问权限为public

    def getName(self):
        return self.__name

    def getAge(self):
        return self._age

    def showInfo(self):
        print("name:", self.__name)
        print("age:", self._age)
        print("height:", self.height)
        print("visited:", self.visited)
        Person.visited = Person.visited +1

class Teacher(Person):
    "老师"

    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.__title = None

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def showInfo(self):
        print("title:", self.__title)
        super().showInfo()


def testPerson():
    "测试方法"
    tony = Person("Tony", 25, 1.77)
    tony.showInfo()
    print()

    jenny = Teacher("Jenny", 34, 1.68)
    jenny.setTitle("教授")
    jenny.showInfo()


# testDataType()
testList()
# testTuple()
# testDictionary()
# testSet()
# testClass()

# testPerson()