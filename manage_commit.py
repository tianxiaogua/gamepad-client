import serial
import serial.tools.list_ports
import time
import _thread

class c_wired_connect:  # 有线连接
    run_status = 0

    def __init__(self):
        self.run_status = 1

    def communication_handle(self, threadName): # 通信
        print("create", threadName)
        while self.run_status:
            # 创建新线程
            # 获取所有串口设备实例。
            # 如果没找到串口设备，则输出：“无串口设备。”
            # 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
            ports_list = list(serial.tools.list_ports.comports())
            if len(ports_list) <= 0:
                print("无串口设备。")
            else:
                print("可用的串口设备如下：")
                for comport in ports_list:
                    print(list(comport)[0], list(comport)[1])
            time.sleep(1)

    def init_wired_connect(self):
        _thread.start_new_thread(self.communication_handle, ("Thread-window", ))

    def deinit_wired_connect(self):
        self.run_status = 0
