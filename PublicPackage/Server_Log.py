import time
import sys
import os


class LogServer:
    # 属性
    def __init__(self):
        self.level = "info"  # 设置初始化日志等级为info
        self.msg = ""  # 初始化消息内容为空
        self.download_offset = False  # 初始化日志下载开关为关闭
        self.maxNum = 5
        self.maxByte = 3 * 1024  # 3kb
        self.addr = "D:\\LogFiles"
        self.filename = "\markedlog"
        self.filesuffix = ".log"
        self.time_head = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())

    def SetFile(self, addr, Maxbyte, MaxNum):
        """

        :param addr:(str)"download" model and the files' route
        :param Maxbyte: (int)"download" model and the file's maxsize
        :param MaxNum: (int)"download" model and the files' maxNum
        :return:
        """
        self.addr = addr
        self.maxByte = Maxbyte * 1024
        self.maxNum = MaxNum
        return None

    # 组合完整log信息函数
    def _log(self, loca, msg):
        time_head = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
        head = "%s%s [%s]" % (time_head, loca, self.level)
        log_information = head + str(msg)
        return log_information

    def log(self, level, msg):
        self.level = level
        if self.level == "download":
            self.download_offset = True
        name = os.path.basename(sys._getframe().f_back.f_code.co_filename)
        num = str(sys._getframe().f_back.f_lineno)
        loca = '{}-{}'.format(name, num)
        print(self._log(loca, msg))
        if self.download_offset is True:
            self.DealLog(self._log(loca, msg))

    def saveFiles(self, msg):  # 创建文件夹
        filepath = self.addr + self.filename + self.filesuffix
        with open(filepath, mode='a+', newline='') as f:
            f.write(msg)
            f.write("\n")
            f.close()

    def DealLog(self, msg):
        self.saveFiles(msg)


if __name__ == '__main__':
    a = LogServer()
    while True:
        a.log("error", "sdajdlajdl aljldjaljs kldajl kjdlka jld akj")
        time .sleep(0.5)

