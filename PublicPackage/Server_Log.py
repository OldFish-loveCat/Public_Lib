import time
import sys
import os

class LogServer:
    # 属性值
    def __init__(self):
        self.level = "info"  # 设置初始化日志等级为info
        self.msg = ""  # 初始化消息内容为空
        self.download_offset = False  # 初始化日志下载开关为关闭
        self.maxNum = 5
        self.maxByte = 3 * 1024  # 3kb
        self.addr = os.getcwd()
        self.filename = "markedlog"
        self.time_head = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
        self.head = "%s%s-%d [%s]" % (
            self.time_head, sys._getframe().f_code.co_filename.split("/")[-1], sys._getframe().f_lineno, self.level)

    # 封装函数，设置日志级别
    def SetLevel(self, level):
        """

        :param level: total include:"info","debug","warning","error","critical","download"
            "download"model means this log information need to be download
        :return: None
        """
        self.level = level
        if level == "download":
            self.download_offset = True
        else:
            pass
        return None

    def SetFile(self, addr, Maxbyte, MaxNume):
        """

        :param addr:(str)"download" model and the files' route
        :param Maxbyte: (int)"download" model and the file's maxsize
        :param MaxNume: (int)"download" model and the files' maxNum
        :return:
        """
        self.addr = addr
        self.maxByte = Maxbyte * 1024
        self.maxNum = MaxNume
        return None

    # 组合完整log信息函数
    def __log(self, msg):
        log_information = self.head + str(msg)
        return log_information

    def log(self, msg):
        print(self.__log(msg))
        if self.level == "download" and self.download_offset is True:
            # 此处实现一个存储文件的功能，在目标路径下存放maxNum个最大为maxByte KB大小的log文件
            pass


# if __name__ == '__main__':
#     pass
