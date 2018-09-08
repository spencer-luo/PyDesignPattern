#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 11/17/2017

# Version 1.0
#=======================================================================================================================
class HouseInfo:
    """房源信息"""

    def __init__(self, area, price, hasWindow, hasBathroom, hasKitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__hasWindow = hasWindow
        self.__hasBathroom = hasBathroom
        self.__hasKitchen = hasKitchen
        self.__address = address
        self.__owner = owner

    def getAddress(self):
        return self.__address

    def getOwnerName(self):
        return self.__owner.getName()

    def showInfo(self, isShowOwner = True):
        print("面积:" + str(self.__area) + "平米",
              "价格:" + str(self.__price) + "元",
              "窗户:" + ("有" if self.__hasWindow else "没有"),
              "卫生间:" + self.__hasBathroom,
              "厨房:" + ("有" if self.__hasKitchen else "没有"),
              "地址:" + self.__address,
              "房东:" + self.getOwnerName() if isShowOwner else "")


class HousingAgency:
    """房屋中介"""

    def __init__(self, name):
        self.__houseInfos = []
        self.__name = name

    def getName(self):
        return self.__name

    def addHouseInfo(self, houseInfo):
        self.__houseInfos.append(houseInfo)

    def removeHouseInfo(self, houseInfo):
        for info in self.__houseInfos:
            if(info == houseInfo):
                self.__houseInfos.remove(info)

    def getSearchCondition(self, description):
        """这里有一个将用户描述信息转换成搜索条件的逻辑
        (为节省篇幅这里原样返回描述)"""
        return description

    def getMatchInfos(self, searchCondition):
        """根据房源信息的各个属性查找最匹配的信息
        (为节省篇幅这里略去匹配的过程，全部输出)"""
        print(self.getName(), "为您找到以下最适合的房源：")
        for info in self.__houseInfos:
            info.showInfo(False)
        return  self.__houseInfos

    def signContract(self, houseInfo, period):
        """与房东签订协议"""
        print(self.getName(), "与房东", houseInfo.getOwnerName(), "签订", houseInfo.getAddress(),
              "的房子的的租赁合同，租期", period, "年。 合同期内", self.getName(), "有权对其进行使用和转租！")

    def signContracts(self, period):
        for info in self.__houseInfos :
            self.signContract(info, period)


class HouseOwner:
    """房东"""

    def __init__(self, name):
        self.__name = name
        self.__houseInfo = None

    def getName(self):
        return self.__name

    def setHouseInfo(self, address, area, price, hasWindow, bathroom, kitchen):
        self.__houseInfo = HouseInfo(area, price, hasWindow, bathroom, kitchen, address, self)

    def publishHouseInfo(self, agency):
        agency.addHouseInfo(self.__houseInfo)
        print(self.getName() + "在", agency.getName(), "发布房源出租信息：")
        self.__houseInfo.showInfo()


class Customer:
    """用户，租房的贫下中农"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def findHouse(self, description, agency):
        print("我是" + self.getName() + ", 我想要找一个\"" + description + "\"的房子")
        print()
        return agency.getMatchInfos(agency.getSearchCondition(description))

    def seeHouse(self, houseInfos):
        """去看房，选择最使用的房子
        (这里省略看房的过程)"""
        size = len(houseInfos)
        return houseInfos[size-1]

    def signContract(self, houseInfo, agency, period):
        """与中介签订协议"""
        print(self.getName(), "与中介", agency.getName(), "签订", houseInfo.getAddress(),
              "的房子的租赁合同, 租期", period, "年。合同期内", self.__name, "有权对其进行使用！")

# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================
class InteractiveObject:
    """进行交互的对象"""
    pass

class InteractiveObjectImplA:
    """实现类A"""
    pass

class InteractiveObjectImplB:
    """实现类B"""
    pass

class Meditor:
    """中介类"""

    def __init__(self):
        self.__interactiveObjA = InteractiveObjectImplA()
        self.__interactiveObjB = InteractiveObjectImplB()

    def interative(self):
        """进行交互的操作"""
        # 通过self.__interactiveObjA和self.__interactiveObjB完成相应的交互操作
        pass


# 基于框架的实现
#==============================
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
from enum import Enum
# Python3.4 之后支持枚举Enum的语法

class DeviceType(Enum):
    "设备类型"
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3

class DeviceItem:
    """设备项"""

    def __init__(self, id, name, type, isDefault = False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__isDefault = isDefault

    def __str__(self):
        return "type:" + str(self.__type) + " id:" + str(self.__id) \
               + " name:" + str(self.__name) + " isDefault:" + str(self.__isDefault)

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def isDefault(self):
        return self.__isDefault


class DeviceList:
    """设备列表"""

    def __init__(self):
        self.__devices = []

    def add(self, deviceItem):
        self.__devices.append(deviceItem)

    def getCount(self):
        return len(self.__devices)

    def getByIdx(self, idx):
        if idx < 0 or idx >= self.getCount():
            return None
        return self.__devices[idx]

    def getById(self, id):
        for item in self.__devices:
            if( item.getId() == id):
                return item
        return None

class DeviceMgr(metaclass=ABCMeta):

    @abstractmethod
    def enumerate(self):
        """枚举设备列表
        (在程序初始化时，有设备插拔时都要重新获取设备列表)"""
        pass

    @abstractmethod
    def active(self, deviceId):
        """选择要使用的设备"""
        pass

    @abstractmethod
    def getCurDeviceId(self):
        """获取当前正在使用的设计ID"""
        pass


class SpeakerMgr(DeviceMgr):
    """扬声器设备管理类"""

    def __init__(self):
        self.__curDeviceId = None

    def enumerate(self):
        """枚举设备列表
        (真实的项目应该通过驱动程序去读取设备信息，这里只用初始化来模拟)"""
        devices = DeviceList()
        devices.add(DeviceItem("369dd760-893b-4fe0-89b1-671eca0f0224", "Realtek High Definition Audio", DeviceType.TypeSpeaker))
        devices.add(DeviceItem("59357639-6a43-4b79-8184-f79aed9a0dfc", "NVIDIA High Definition Audio", DeviceType.TypeSpeaker, True))
        return devices

    def active(self, deviceId):
        """激活指定的设备作为当前要用的设备"""
        self.__curDeviceId = deviceId

    def getCurDeviceId(self):
        return self.__curDeviceId


class DeviceUtil:
    """设备工具类"""

    def __init__(self):
        self.__mgrs = {}
        self.__mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()
        # 为节省篇幅，MicrophoneMgr和CameraMgr不再实现
        # self.__microphoneMgr = MicrophoneMgr()
        # self.__cameraMgr = CameraMgr

    def __getDeviceMgr(self, type):
        return self.__mgrs[type]

    def getDeviceList(self, type):
        return self.__getDeviceMgr(type).enumerate()

    def active(self, type, deviceId):
        self.__getDeviceMgr(type).active(deviceId)

    def getCurDeviceId(self, type):
        return self.__getDeviceMgr(type).getCurDeviceId()


# Test
#=======================================================================================================================

def testRenting():
    myHome = HousingAgency("我爱我家")
    zhangsan = HouseOwner("张三");
    zhangsan.setHouseInfo("上地西里", 20, 2500, 1, "独立卫生间", 0)
    zhangsan.publishHouseInfo(myHome)
    lisi = HouseOwner("李四")
    lisi.setHouseInfo("当代城市家园", 16, 1800, 1, "公用卫生间", 0)
    lisi.publishHouseInfo(myHome)
    wangwu = HouseOwner("王五")
    wangwu.setHouseInfo("金隅美和园", 18, 2600, 1, "独立卫生间", 1)
    wangwu.publishHouseInfo(myHome)
    print()

    myHome.signContracts(3)
    print()

    tony = Customer("Tony")
    houseInfos = tony.findHouse("18平米左右，要有独卫，要有窗户，最好是朝南，有厨房更好！价位在2000左右", myHome)
    print()
    print("正在看房，寻找最合适的住巢……")
    print()
    AppropriateHouse = tony.seeHouse(houseInfos)
    tony.signContract(AppropriateHouse, myHome, 1)


def testDevices():
    deviceUtil = DeviceUtil()
    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)
    print("麦克风设备列表：")
    if deviceList.getCount() > 0:
        # 设置第一个设备为要用的设备
        deviceUtil.active(DeviceType.TypeSpeaker, deviceList.getByIdx(0).getId())
    for idx in range(0, deviceList.getCount()):
        device = deviceList.getByIdx(idx)
        print(device)
    print("当前使用的设备："
          + deviceList.getById(deviceUtil.getCurDeviceId(DeviceType.TypeSpeaker)).getName())


# testRenting()
testDevices()
