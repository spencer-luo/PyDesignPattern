#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 5/20/2018

# 引入升级版备忘录模式关键类
from pattern.Memento import Originator, Caretaker, Memento
import logging

class TerminalCmd(Originator):
    """终端命令"""

    def __init__(self, text):
        self.__cmdName = ""
        self.__cmdArgs = []
        self.parseCmd(text)

    def parseCmd(self, text):
        """从字符串中解析命令"""
        subStrs = self.getArgumentsFromString(text, " ")
        # 获取第一个字段作为命令名称
        if(len(subStrs) > 0):
            self.__cmdName = subStrs[0]

        # 获取第一个字段之后的所有字符作为命令的参数
        if (len(subStrs) > 1):
            self.__cmdArgs = subStrs[1:]

    def getArgumentsFromString(self, str, splitFlag):
        """通过splitFlag进行分割，获得参数数组"""

        if (splitFlag == ""):
            logging.warning("splitFlag 为空!")
            return ""

        data = str.split(splitFlag)
        result = []
        for item in data:
            item.strip()
            if (item != ""):
                result.append(item)

        return result;

    def showCmd(self):
        print(self.__cmdName, self.__cmdArgs)

class TerminalCaretaker(Caretaker):
    """终端命令的备忘录管理类"""

    def showHistoryCmds(self):
        """显示历史命令"""
        for key, obj in self._mementos.items():
            name = ""
            value = []
            if(obj._TerminalCmd__cmdName):
                name = obj._TerminalCmd__cmdName
            if(obj._TerminalCmd__cmdArgs):
                value = obj._TerminalCmd__cmdArgs
            print("第%s条命令: %s %s" % (key, name, value) )


def testTerminal():
    cmdIdx = 0
    caretaker = TerminalCaretaker()
    curCmd = TerminalCmd("")
    while (True):
        strCmd = input("请输入指令：");
        strCmd = strCmd.lower()
        if (strCmd.startswith("q")):
            exit(0)
        elif(strCmd.startswith("h")):
            caretaker.showHistoryCmds()
        # 通过"!"符号表示获取历史的某个指令
        elif(strCmd.startswith("!")):
            idx = int(strCmd[1:])
            curCmd.restoreFromMemento(caretaker.getMemento(idx))
            curCmd.showCmd()
        else:
            curCmd = TerminalCmd(strCmd)
            curCmd.showCmd()
            caretaker.addMemento(cmdIdx, curCmd.createMemento())
            cmdIdx +=1


testTerminal()