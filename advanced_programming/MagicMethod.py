#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 9/15/2018

# ClassA
#=======================================================================================================================
# class ClassA:
#     def __new__(cls):
#         print("ClassA.__new__")
#         return super().__new__(cls)
#
#     def __init__(self):
#         print("ClassA.__init__")
#
#     def __call__(self, *args):
#         print("ClassA.__call__ args:", args)
#
# a = ClassA()
# a("arg1", "arg2")

# ClassB
#=======================================================================================================================
# class Sample(object):
#     def __str__(self):
#         return "SAMPLE"
#
# class ClassB:
#
#     def __new__(cls):
#         print("ClassB.__new__")
#         return super().__new__(Sample)
#         # return Sample() # 也可以是这种写法
#
#     def __init__(self):
#         print("ClassB.__init__")
#
# b = ClassB()
# print(b)
# print(type(b))

# ClassC
#=======================================================================================================================
# class ClassC:
#     def __init__(self, *args, **kwargs):
#         print("init", args, kwargs)
#
#     def __new__(cls, *args, **kwargs):
#         print("new", args, kwargs)
#         return super().__new__(cls)
#
# c = ClassC("arg1", "arg2", a=1, b=2)



# ClassD
#=======================================================================================================================
# class ClassD:
#
#     def __new__(cls):
#         print("ClassB.__new__")
#         self = super().__new__(cls)
#         print(self)
#         return self
#
#     def __init__(self):
#         print("ClassC.__init__")
#         print(self)
#
# d = ClassD()



# Callable
#=======================================================================================================================
# def funTest(name):
#     print("This is test function, name:", name)
#
# print(callable(filter))
# print(callable(max))
# print(callable(object))
# print(callable(funTest))
# var = "Test"
# print(callable(var))
# funTest("Python")


# __call__
#=======================================================================================================================
class ClassE:

    def __call__(self, *args):
        print("This is __call__ function, args:", args)

e = ClassE()
print(callable(e))
e("arg1", "arg2")
