#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 12/08/2018

# Version 1.0
#=======================================================================================================================
import random
# 引入随机数模块

class Camera:
    """相机机身"""

    # 对焦类型
    SingleFocus = "单点对焦"
    AreaFocus = "区域对焦"
    BigAreaFocus = "大区域对焦"
    Focus45 = "45点自动对焦"

    def __init__(self, name):
        self.__name = name
        self.__aperture = 0.0       # 光圈
        self.__shutterSpeed = 0     # 快门速度
        self.__ligthSensitivity = 0 # 感光度
        self.__lens = Lens()        # 镜头
        self.__sdCard = SDCard()    # SD卡
        self.__display = Display()  # 显示器

    def shooting(self):
        """拍照"""
        print("[开始拍摄中")
        imageLighting = self.__lens.collecting()
        # 通过快门、光圈和感光度、测光来控制拍摄的过程，省略此部分
        image = self.__transferImage(imageLighting)
        self.__sdCard.addImage(image)
        print("拍摄完成]")

    def viewImage(self, index):
        """查看图像"""
        print("查看第%d张图像：" % (index + 1))
        image = self.__sdCard.getImage(index)
        self.__display.showImage(image)

    def __transferImage(self, imageLighting):
        """接收光线并处理成数字信号，简单模拟"""
        print("接收光线并处理成数字信号")
        return Image(6000, 4000, imageLighting)

    def setting(self, aperture, shutterSpeed, ligthSensitivity):
        """设置相机的拍摄属性：光圈、快门、感光度"""
        self.__aperture = aperture
        self.__shutterSpeed = shutterSpeed
        self.__ligthSensitivity = ligthSensitivity

    def focusing(self, focusMode):
        """对焦，要通过镜头来调节焦点"""
        self.__lens.setFocus(focusMode)

    def showInfo(self):
        """显示相机的属性"""
        print("%s的设置   光圈：F%0.1f  快门：1/%d  感光度：ISO %d" %
              (self.__name, self.__aperture, self.__shutterSpeed, self.__ligthSensitivity))


class Lens:
    """镜头"""

    def __init__(self):
        self.__focusMode = ''   # 对焦
        self.__scenes = {0 : '风光', 1 : '生态', 2 : '人文', 3 : '纪实', 4 : '人像', 5 : '建筑'}

    def setFocus(self, focusMode):
        self.__focusMode = focusMode

    def collecting(self):
        """图像采集，采用随机的方式来模拟自然的拍摄过程"""
        print("采集光线，%s" % self.__focusMode)
        index = random.randint(0, len(self.__scenes)-1)
        scens = self.__scenes[index]
        return "美丽的 " + scens + " 图像"


class Display:
    """显示器"""

    def showImage(self, image):
        print("图片大小：%d x %d，  图片内容：%s" % (image.getWidth(), image.getHeight(), image.getPix()))


class SDCard:
    """SD存储卡"""

    def __init__(self):
        self.__images = []

    def addImage(self, image):
        print("存储图像")
        self.__images.append(image)

    def getImage(self, index):
        if (index >= 0 and index < len(self.__images)):
            return self.__images[index]
        else:
            return None


class Image:
    """图像(图片), 方便起见用字符串来代码图像的内容(像素)"""

    def __init__(self, width, height, pixels):
        self.__width = width
        self.__height = height
        self.__pixels = pixels

    def getWidth(self):
        return  self.__width

    def getHeight(self):
        return self.__height

    def getPix(self):
        return self.__pixels


# Version 2.0
#=======================================================================================================================
# 代码框架
#==============================

# 基于框架的实现
#==============================


# Test
#=======================================================================================================================
def testCamera():
    camera = Camera("EOS 80D")
    camera.setting(3.5, 60, 200)
    camera.showInfo()
    camera.focusing(Camera.BigAreaFocus)
    camera.shooting()
    print()

    camera.setting(5.6, 720, 100)
    camera.showInfo()
    camera.focusing(Camera.Focus45)
    camera.shooting()
    print()

    camera.viewImage(0)
    camera.viewImage(1)


testCamera()