#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 11/21/2017

# Version 1.0
#=======================================================================================================================
def testDataType():
    age = 18        # int
    weight = 62.51  # float
    name = "Tony"  # string
    print("age:", age)
    print("weight:", weight)
    print("name:", name)
    # 变量的类型可以直接改变
    age = name
    print("age:", age)

    a = b = c = 5
    # a,b,c三个变量指向相同的内存空间，具有相同的值
    print("a:", a, "b:", b, "c:", c)
    print("id(a):", id(a), "id(b):", id(b), "id(c):", id(c))


def testList():
    list = ['Thomson', 78, 12.58, 'Sunny', 180.2]
    tinylist = [123, 'Tony']
    print(list)  # 输出完整列表
    print(list[0])  # 输出列表的第一个元素
    print(list[1:3])  # 输出第二个至第三个元素
    print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
    print(tinylist * 2)  # 输出列表两次
    print(list + tinylist)  # 打印组合的列表
    list[1] = 100
    print(list)  # 输出完整列表
    list.append("added data")
    print(list)  # 输出增加后的列表


def testTuple():
    tuple = ('Thomson', 78, 12.58, 'Sunny', 180.2)
    tinytuple = (123, 'Tony')
    print(tuple)  # 输出完整元组
    print(tuple[0])  # 输出元组的第一个元素
    print(tuple[1:3])  # 输出第二个至第三个的元素
    print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
    print(tinytuple * 2)  # 输出元组两次
    print(tuple + tinytuple)  # 打印组合的元组
    # tuple[1] = 100 # 不能修改元组内的元素


def testDictionary():
    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"
    tinydict = {'name': 'Tony', 'age': 24, 'height': 177}

    print(dict['one'])  # 输出键为'one' 的值
    print(dict[2])  # 输出键为 2 的值
    print(tinydict) # 输出完整的字典
    print(tinydict.keys())  # 输出所有键
    print(tinydict.values())  # 输出所有值


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
        self.__name = name
        self._age = age
        self.height = height

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
    print();

    jenny = Teacher("Jenny", 34, 1.68);
    jenny.setTitle("教授");
    jenny.showInfo();

testPerson()

# testDataType()
# testList()
# testTuple()
# testDictionary()
# testClass()

# testPerson()