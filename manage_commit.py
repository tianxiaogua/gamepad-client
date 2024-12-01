import serial
import serial.tools.list_ports
import time
import _thread

class c_wired_connect:  # 有线连接

    def __init__(self):
        self.run_status = 1
        self.serial_ = 1
        self.handle_recv_cb = 0 # 处理接收回调函数
        self.handle_write_cb = 0

    def serial_recv_data_cb_register(self, recv_func, write_func):
        self.handle_recv_cb = recv_func
        self.handle_write_cb = write_func

    def connect_serial(self, name, rate):
        # 创建Serial对象，初始化串口
        self.serial_ = serial.Serial(name, rate, timeout=1)  # Windows示例，COM1是串口号，9600是波特率，timeout是读超时时间
        _thread.start_new_thread(self.communication_handle, ("Thread-window",))

    def disconnect_serial(self):
        self.serial_.close()

    def get_connect_status(self):
        return self.serial_.isOpen()  # 或使用 ser.is_open（注意：在较新版本的PySerial中，推荐使用is_open）

    def refresh_serial_port(self):  # 刷新串口
        ports_list = list(serial.tools.list_ports.comports())
        if len(ports_list) <= 0:
            print("无串口设备。")
            return 0
        else:
            # print("可用的串口设备如下：")
            # for comport in ports_list:
            #     print(list(comport)[0], list(comport)[1])
            return ports_list

    def communication_handle(self, threadName):  # 通信
        print("create", threadName)
        while self.run_status:
            data = self.serial_.readline()
            self.handle_recv_cb(data)
            print(data)

    def init_wired_connect(self):
        # _thread.start_new_thread(self.communication_handle, ("Thread-window", ))
        pass

    def deinit_wired_connect(self):
        self.run_status = 0
