#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 9/16/2018

# type()
#=======================================================================================================================
# class ClassA:
#     name = "type test"
#
# a = ClassA()
# b = 3.0
#
# print(type(a))
# print(type(b))
# print(type("This is string"))
# print()
#
# print(a.__class__)
# print(b.__class__)



# ClassVariable = type('ClassA', (object,), dict(name="type test"))
# a = ClassVariable()
# print(type(a))
# print(a.name)

# isinstance()
#=======================================================================================================================
class BaseClass:
    name = "Base"

class SubClass(BaseClass):
    pass


base = BaseClass()
sub = SubClass()

# print(isinstance(base, BaseClass))
# print(isinstance(base, SubClass))
# print()
#
# print(isinstance(sub, SubClass))
# print(isinstance(sub, BaseClass))


# print(issubclass(SubClass, BaseClass))
# print(issubclass(BaseClass, SubClass))
# print(SubClass.__bases__)


# Version 2.0
#=======================================================================================================================
# class MyClass:
#     pass
#
# m = MyClass()
# print(type(MyClass))
# print(type(m))
# print()
#
# print(isinstance(m, MyClass))
# print(isinstance(MyClass, type))



# MetaClass
#=======================================================================================================================
# class CustomMetaclass(type):
#     pass
#
# class CustomClass(metaclass=CustomMetaclass):
#     pass
#
# print(type(object))
# print(type(type))
# print()
#
# obj = CustomClass()
# print(type(CustomClass))
# print(type(obj))
#
# print()
# print(isinstance(obj, CustomClass))
# print(isinstance(obj, object))



# CustomMetaClass
#=======================================================================================================================
class CustomMetaclass(type):

    def __init__(cls, what, bases=None, dict=None):
        print("CustomMetaclass.__init__ cls:", cls)
        super().__init__(what, bases, dict)

    def __call__(cls, *args, **kwargs):
        print("CustomMetaclass.__call__ args:", args, kwargs)
        self = super(CustomMetaclass, cls).__call__(*args, **kwargs)
        print("CustomMetaclass.__call__ self:", self)
        return self

class CustomClass(metaclass=CustomMetaclass):

    def __init__(self, *args, **kwargs):
        print("CustomClass.__init__ self:", self)
        super().__init__()

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        print("CustomClass.__new__, self:", self)
        return self

    def __call__(self, *args, **kwargs):
        print("CustomClass.__call__ args:", args)

obj = CustomClass("Meta arg1", "Meta arg2", kwarg1=1, kwarg2=2)
print(type(CustomClass))
print(obj)
obj("arg1", "arg2")


# class Singleton2(type):
#     # def __init__(cls, name, bases, attrs):
#     #     super(Singleton2, cls).__init__(name, bases, attrs)
#     #     cls._instance = None
#
#     def __call__(cls, *args, **kwargs):
#         # if not cls._instance:
#         #     cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
#         return super(Singleton2, cls).__call__(*args, **kwargs)
#
# class MyClass(metaclass=Singleton2):
#     def __init__(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#
# # Test
# s0 = MyClass("Zhangsan")
# s1 = MyClass("Lisi")
# print(s0.getName(), s1.getName())
# print("id(s0):", id(s0), "id(s1):", id(s1))
# print("s0 == s1:", s0 == s1)

# object