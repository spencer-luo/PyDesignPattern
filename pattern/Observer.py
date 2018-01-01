##!/usr/bin/python

# Version 1.0
########################################################################################################################
# class WaterHeater:
#     "热水器：战胜寒冬的有利武器"
#
#     def __init__(self):
#         self.__observers = []
#         self.__temperature = 25
#
#     def getTemperature(self):
#         return self.__temperature
#
#     def setTemperature(self, temperature):
#         self.__temperature = temperature
#         print("current temperature is:", self.__temperature)
#         self.notifies()
#
#     def addObserver(self, observer):
#         self.__observers.append(observer)
#
#     def notifies(self):
#         for o in self.__observers:
#             o.update(self)
#
#
# class Observer:
#     "洗澡模式和饮用模式的父类"
#
#     def update(self, waterHeater):
#         pass
#
#
# class WashingMode(Observer):
#     "该模式用于洗澡用"
#
#     def update(self, waterHeater):
#         if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
#             print("水已烧好，温度正好！可以用来洗澡了。")
#
#
# class DrinkingMode(Observer):
#     "该模式用于饮用"
#
#     def update(self, waterHeater):
#         if waterHeater.getTemperature() >= 100:
#             print("水已烧开！可以用来饮用了。")


# Version 2.0
########################################################################################################################

class Observer:
    "观察者的基类"

    def update(self, observable, object):
        pass


class Observable:
    "被观察者的基类"

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    "热水器：战胜寒冬的有利武器"

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("current temperature is:", self.__temperature)
        self.notifyObservers()


class WashingMode(Observer):
    "该模式用于洗澡用"

    def update(self, observable, object):
        if isinstance(observable,
                      WaterHeater) and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("水已烧好，温度正好！可以用来洗澡了。")


class DrinkingMode(Observer):
    "该模式用于饮用"

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已烧开！可以用来饮用了。")


def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)


testWaterHeater()
