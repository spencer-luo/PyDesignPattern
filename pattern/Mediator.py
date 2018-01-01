#!/usr/bin/python
# Authoer: Administrator
# Date: 11/17/2017

# Version 1.0
#=======================================================================================================================
class HouseInfo:
    "房源信息"

    def __init__(self, area, price, hasWindow, bathroom, kitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__window = hasWindow
        self.__bathroom = bathroom
        self.__kitchen = kitchen
        self.__address = address
        self.__owner = owner

    def getAddress(self):
        return self.__address

    def getOwnerName(self):
        return self.__owner.getName()

    def showInfo(self, isShowOwner = True):
        print("面积:" + str(self.__area) + "平米",
              "价格:" + str(self.__price) + "元",
              "窗户:" + ("有" if self.__window else "没有"),
              "卫生间:" + self.__bathroom,
              "厨房:" + ("有" if self.__kitchen else "没有"),
              "地址:" + self.getAddress(),
              "房东:" + self.getOwnerName() if isShowOwner else "")



class HousingAgency:
    "房屋中介"

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
        "这里有一个将用户描述信息转换成搜索条件的逻辑。(为节省篇幅这里原样返回描述)"
        return description

    def getMatchInfos(self, searchCondition):
        "根据房源信息的各个属性查找最匹配的信息。(为节省篇幅这里略去匹配的过程，全部输出)"
        print(self.getName(), "为您找以下最适合的房源：")
        for info in self.__houseInfos:
            info.showInfo(False)
        return  self.__houseInfos

    def signContract(self, houseInfo, time):
        "与房东签订协议"
        print(self.getName(), "与房东", houseInfo.getOwnerName(), "签订", houseInfo.getAddress(),
              "的房子的的租赁合同，租期", time, "年。 合同期内", self.getName(), "有权对其进行使用和转租！")

    def signContracts(self, time):
        for info in self.__houseInfos :
            self.signContract(info, time)


class HouseOwner:
    "房东"

    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__houseInfo = None

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def setHouseInfo(self, area, price, hasWindow, bathroom, kitchen):
        self.__houseInfo = HouseInfo(area, price, hasWindow, bathroom, kitchen, self.getAddress(), self)

    def publishHouseInfo(self, agency):
        agency.addHouseInfo(self.__houseInfo)
        print(self.getName() + "在", agency.getName(), "发布房源出租信息：")
        self.__houseInfo.showInfo()


class Custom:
    "用户，租房人"

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def findHouse(self, description, agency):
        print("我是" + self.getName() + ", 我想要找一个\"" + description + "\"的房子")
        print()
        return agency.getMatchInfos(agency.getSearchCondition(description))

    def seeHouse(self, houseInfos):
        "去看房，选择最使用的房子。(这里省略看房的过程)"
        size = len(houseInfos)
        return houseInfos[size-1]

    def signContract(self, houseInfo, agency, time):
        "与中介签订协议"
        print(self.getName(), "与中介", agency.getName(), "签订", houseInfo.getAddress(),
              "的房子的租赁合同, 租期", time, "年。合同期内", self.__name, "有权对其进行使用！")


# class ZhangSan(HouseOwner):
#     "张三"
#
#     def __init__(self, name, address):
#         super().__init__(name, address)
#         self.houseInfo = HouseInfo(20, 2500, 1, "独立卫生间", 0, address, name)
#
# class LiSi(HouseOwner):
#     "李四"
#
#     def __init__(self, name, address):
#         super().__init__(name, address)
#         self.houseInfo = HouseInfo(16, 1800, 1, "公用卫生间", 0, address, name)
#
#
# class WangWu(HouseOwner):
#     "王五"
#
#     def __init__(self, name, address):
#         super().__init__(name, address)
#         self.houseInfo = HouseInfo(18, 2600, 1, "独立卫生间", 1, address, name)

# area, price, hasWindow, bathroom, kitchen, address, owner

# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================


# 基于框架的实现
#==============================


# Test
#=======================================================================================================================

def testRenting():
    myHome = HousingAgency("我爱我家")
    zhangsan = HouseOwner("张三", "上地西里");
    zhangsan.setHouseInfo(20, 2500, 1, "独立卫生间", 0)
    zhangsan.publishHouseInfo(myHome)
    lisi = HouseOwner("李四", "当代城市家园")
    lisi.setHouseInfo(16, 1800, 1, "公用卫生间", 0)
    lisi.publishHouseInfo(myHome)
    wangwu = HouseOwner("王五", "金隅美和园")
    wangwu.setHouseInfo(18, 2600, 1, "独立卫生间", 1)
    wangwu.publishHouseInfo(myHome)
    print()

    myHome.signContracts(3)
    print()

    tony = Custom("Tony")
    houseInfos = tony.findHouse("18平米左右，要有独卫，要有窗户，最好是朝南，有厨房更好！价位在2000左右", myHome)
    print()
    print("正在看房，寻找最合适的住巢……")
    print()
    AppropriateHouse = tony.seeHouse(houseInfos)
    tony.signContract(AppropriateHouse, myHome, 1)

testRenting()