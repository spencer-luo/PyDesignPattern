# class A(object):  # -> don't forget the object specified as base
#
#     def __new__(cls):
#         print("A.__new__ called")
#         return super(A, cls).__new__(cls)
#         # return 20
#
#     def __init__(self):
#         print("A.__init__ called")
#         return 22
#
# print(A())
#
# class B:
#     __instance = None
#
#     def __new__(cls, name):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#             cls.name = name
#         return cls.__instance;
#
#     def __init__(self, name):
#         self.name = name
#
#
#     # def get
#
#     @classmethod
#     def getInstance(cls, name):
#         if B.__instance is None:
#             B.__instance = B(name)
#         return B.__instance
#
# # b1 = B("B1")
# # print("id:", id(b1), " name:", b1.name)
# # b2 = B("B2")
# # print("id:", id(b2), " name:", b2.name)
#
# # b = B("B")



class Foobar(object):
    # pass
    def __init__(self, name):
        self.name = name

print( type(Foobar) )
print(Foobar)
foo = Foobar("Test")
print( type(foo) )
print(foo.name)
foo2 = type(foo)("Text2")
print(foo2.name)
# print("Hello")
print(isinstance(foo, Foobar))
print(isinstance(Foobar, type))
print(isinstance(Foobar, object))



MyClass = type('MyClass', (), {})
print(MyClass)

# T = type
print(type("Test", (), {}))


# class MetaAAA(type):
#     pass
#     # def __prepare__(metacls, name, bases):
#     #     pass
#
#
# print(MetaAAA)
#
#
# class MyClassA(metaclass=MetaAAA):
#     pass
#
#     def test(self):
#         b = 5
#         b = True
#
# print(type(MyClassA))
#
#
#
# print("=====================")
# class B:
#     pass
#
# class C(B):
#     pass
#
# c = C()
# print(C.__bases__)
#
#
# print("Base===============")
# print(object.__bases__)
# print(type.__bases__)
# print(type(object))
# print(object.__class__)
# print(type(C))
# print(C.__class__)
#
# print("Callable:")
# print(callable(type))
# print(callable(object))
# print(type(object))
#
#
# print("DD====================")
# class DD:
#
#     def __call__(self, *args, **kwargs):
#         print("DD.__call__")
#         # print(args)
#         return self.__class__
#
#     def __init__(self, name):
#         self.name = name
# #
# # d = DD()
# # d("This is test")
# # DD("This is test")
# # id(d)
#
# # DD = DD()
# # DD("This is test")
# d = DD("Test")
# print(d)
# print(d.name)
# print(callable(DD))
# print(callable(d))
callable()

