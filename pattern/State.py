##!/usr/bin/python

# Version 1.0
########################################################################################################################
# from abc import ABCMeta, abstractmethod
# # 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
#
# class Water:
#     """水(H2O)"""
#
#     def __init__(self, state):
#         self.__temperature = 25 # 默认25℃常温
#         self.__state = state
#
#     def setState(self, state):
#         self.__state = state
#
#     def changeState(self, state):
#         if (self.__state):
#             print("由", self.__state.getName(), "变为", state.getName())
#         else:
#             print("初始化为", state.getName())
#         self.__state = state
#
#     def getTemperature(self):
#         return self.__temperature
#
#     def setTemperature(self, temperature):
#         self.__temperature = temperature
#         if (self.__temperature <= 0):
#             self.changeState(SolidState("固态"))
#         elif (self.__temperature <= 100):
#             self.changeState(LiquidState("液态"))
#         else:
#             self.changeState(GaseousState("气态"))
#
#     def riseTemperature(self, step):
#         self.setTemperature(self.__temperature + step)
#
#     def reduceTemperature(self, step):
#         self.setTemperature(self.__temperature - step)
#
#     def behavior(self):
#         self.__state.behavior(self)
#
#
# class State(metaclass=ABCMeta):
#     """状态类"""
#
#     def __init__(self, name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#     @abstractmethod
#     def behavior(self, water):
#         """不同状态下的行为"""
#         pass
#
#
# class SolidState(State):
#     """固态"""
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def behavior(self, water):
#         print("我性格高冷，当前体温" + str(water.getTemperature()) +
#               "℃，我坚如钢铁，仿如一冷血动物，请用我砸人，嘿嘿……")
#
#
# class LiquidState(State):
#     """液态"""
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def behavior(self, water):
#         print("我性格温和，当前体温" + str(water.getTemperature()) +
#               "℃，我可滋润万物，饮用我可让你活力倍增……")
#
#
# class GaseousState(State):
#     """气态"""
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def behavior(self, water):
#         print("我性格热烈，当前体温" + str(water.getTemperature()) +
#               "℃，飞向天空是我毕生的梦想，在这你将看不到我的存在，我将达到无我的境界……")


# Version 2.0
########################################################################################################################
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Context(metaclass=ABCMeta):
    """状态模式的上下文环境类"""

    def __init__(self):
        self.__states = []
        self.__curState = None
        # 状态发生变化依赖的属性, 当这一变量由多个变量共同决定时可以将其单独定义成一个类
        self.__stateInfo = 0

    def addState(self, state):
        if (state not in self.__states):
            self.__states.append(state)

    def changeState(self, state):
        if (state is None):
            return False
        if (self.__curState is None):
            print("初始化为", state.getName())
        else:
            print("由", self.__curState.getName(), "变为", state.getName())
        self.__curState = state
        self.addState(state)
        return True

    def getState(self):
        return self.__curState

    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if( state.isMatch(stateInfo) ):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo


class State:
    """状态的基类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isMatch(self, stateInfo):
        "状态的属性stateInfo是否在当前的状态范围内"
        return False

    @abstractmethod
    def behavior(self, context):
        pass



# Demo 实现

class Water(Context):
    """水(H2O)"""

    def __init__(self):
        super().__init__()
        self.addState(SolidState("固态"))
        self.addState(LiquidState("液态"))
        self.addState(GaseousState("气态"))
        self.setTemperature(25)

    def getTemperature(self):
        return self._getStateInfo()

    def setTemperature(self, temperature):
        self._setStateInfo(temperature)

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        state = self.getState()
        if(isinstance(state, State)):
            state.behavior(self)


# 单例的装饰器
def singleton(cls, *args, **kwargs):
    "构造一个单例的装饰器"
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


@singleton
class SolidState(State):
    """固态"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, context):
        print("我性格高冷，当前体温", context._getStateInfo(),
              "℃，我坚如钢铁，仿如一冷血动物，请用我砸人，嘿嘿……")


@singleton
class LiquidState(State):
    """液态"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return (stateInfo >= 0 and stateInfo < 100)

    def behavior(self, context):
        print("我性格温和，当前体温", context._getStateInfo(),
              "℃，我可滋润万物，饮用我可让你活力倍增……")

@singleton
class GaseousState(State):
    """气态"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self, context):
        print("我性格热烈，当前体温", context._getStateInfo(),
              "℃，飞向天空是我毕生的梦想，在这你将看不到我的存在，我将达到无我的境界……")


# Test
########################################################################################################################
def testState():
    # water = Water(LiquidState("液态"))
    water = Water()
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()


testState()


# t1 = State("State1")
# t2 = State("State2")
# t3 = SolidState("State3")
# t4 = SolidState("State4")
# print(t1.getName(), t2.getName(), t3.getName(), t4.getName())
# print(id(t1), id(t2), id(t3), id(t4))
# print(t1 == t2)
# print(t3 == t4)


