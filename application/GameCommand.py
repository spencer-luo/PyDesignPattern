#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Authoer: Spencer.Luo
# Date: 5/18/2018

from abc import ABCMeta, abstractmethod
import time

class GameRole:

    # 每次移动的步距
    STEP = 5

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__z = 0

    def leftMove(self):
        self.__x -= self.STEP

    def rightMove(self):
        self.__x += self.STEP

    def upMove(self):
        self.__y += self.STEP

    def downMove(self):
        self.__y -= self.STEP

    def jumpMove(self):
        self.__z += self.STEP

    def squatMove(self):
        self.__z -= self.STEP

    def attack(self):
        print("攻击...")

    def showPosition(self):
        print("x:" + str(self.__x) + ", y:" + str(self.__y) + ", z:" + str(self.__z))

class GameCommand(metaclass=ABCMeta):
    "游戏角色的命令类"

    def __init__(self, role):
        self._role = role

    def setRole(self, role):
        self._role = role

    @abstractmethod
    def execute(self):
        pass

class Left(GameCommand):
    "左移命令"

    def execute(self):
        self._role.leftMove()
        self._role.showPosition()

class Right(GameCommand):
    "右移命令"

    def execute(self):
        self._role.rightMove()
        self._role.showPosition()

class Up(GameCommand):
    "上移命令"

    def execute(self):
        self._role.upMove()
        self._role.showPosition()

class Down(GameCommand):
    "下移命令"

    def execute(self):
        self._role.downMove()
        self._role.showPosition()


class Jump(GameCommand):
    "弹跳命令"

    def execute(self):
        self._role.jumpMove()
        self._role.showPosition()
        # 跳起后空中停留半秒
        time.sleep(0.5)

class Squat(GameCommand):
    "下蹲命令"

    def execute(self):
        self._role.squatMove()
        self._role.showPosition()
        # 下蹲后伏地半秒
        time.sleep(0.5)


class Attack(GameCommand):
    "攻击命令"

    def execute(self):
        self._role.attack()

class MacroCommand(GameCommand):

    def __init__(self, role = None):
        super().__init__(role)
        self.__commands = []

    def addCommand(self, command):
        # 让所有的命令作用于同一个对象
        # command.setRole(self._role)
        self.__commands.append(command)

    def removeCommand(self, command):
        self.__commands.remove(command)

    def execute(self):
        for command in self.__commands:
            command.execute()

class GameInvoker:
    def __init__(self):
        self.__command = None

    def setCommand(self, command):
        self.__command = command
        return self

    def action(self):
        if self.__command is not None:
            self.__command.execute()

def testGame():
    role = GameRole()
    invoker = GameInvoker()
    while True:
        strCmd = input("请输入命令：");
        strCmd = strCmd.upper()
        if (strCmd == "L"):
            invoker.setCommand(Left(role)).action()
        elif (strCmd == "R"):
            invoker.setCommand(Right(role)).action()
        elif (strCmd == "U"):
            invoker.setCommand(Up(role)).action()
        elif (strCmd == "D"):
            invoker.setCommand(Down(role)).action()
        elif (strCmd == "JP"):
            cmd = MacroCommand()
            cmd.addCommand(Jump(role))
            cmd.addCommand(Squat(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "A"):
            invoker.setCommand(Attack(role)).action()
        elif (strCmd == "LU"):
            cmd = MacroCommand()
            cmd.addCommand(Left(role))
            cmd.addCommand(Up(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "LD"):
            cmd = MacroCommand()
            cmd.addCommand(Left(role))
            cmd.addCommand(Down(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "RU"):
            cmd = MacroCommand()
            cmd.addCommand(Right(role))
            cmd.addCommand(Up(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "RD"):
            cmd = MacroCommand()
            cmd.addCommand(Right(role))
            cmd.addCommand(Down(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "LA"):
            cmd = MacroCommand()
            cmd.addCommand(Left(role))
            cmd.addCommand(Attack(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "RA"):
            cmd = MacroCommand()
            cmd.addCommand(Right(role))
            cmd.addCommand(Attack(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "UA"):
            cmd = MacroCommand()
            cmd.addCommand(Up(role))
            cmd.addCommand(Attack(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "DA"):
            cmd = MacroCommand()
            cmd.addCommand(Down(role))
            cmd.addCommand(Attack(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "JA"):
            cmd = MacroCommand()
            cmd.addCommand(Jump(role))
            cmd.addCommand(Attack(role))
            cmd.addCommand(Squat(role))
            invoker.setCommand(cmd).action()
        elif (strCmd == "Q"):
            exit()


testGame()
