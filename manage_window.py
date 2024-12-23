import vgamepad as vg
import time
import _thread
import time
import serial
import serial.tools.list_ports
import tkinter as tk  # 要使用，先导入
from cmp_wifi import *
from tkinter import *
from cmp_setting import app_set

class c_window_manage:  # 窗口管理
    p_window = 0
    def_function = 0

    text_box_serial_display = 0
    tupleVar = ['COM8 蓝牙链接上的标准串行 (COM8)', 'java', 'C', 'C++', 'C#']
    test_wifi_name = 0
    test_wifi_pass = 0
    ports_list = 0
    serial_connect_status = 0

    def __init__(self):
        self.p_window = tk.Tk()  # 创建一个窗口，因为后面还要用到所以用window这个变量来赋值，可以自行更改
        self.wifi_password = "0"
        self.serial_bite = 0
        self.test_wifi_pass = 0
        self.test_wifi_name = 0
        self.ports_list = 0

        self.serial_connect_status = 0
        self.serial_connect_button = 0
        self.serial_bit_textbox = 0
        self.target_serial = 0
        self.target_serial_rate = 0
        self.connect_serial_cb = 0
        self.refresh_serial_cb = 0
        self.get_connect_status_cb = 0
        self.disconnect_serial_cb = 0
        self.serial_write_cb = 0

        # self.tupleVar = 0
        self.optionMenu_serial = 0
        self.dropdown_serial = 0

        self.setting = app_set()


    def close_window_register(self, func):
        print("register close window")
        self.def_function = func

    def communicat_serial_register(self, connect, disconnect, refresh, status, write):
        self.refresh_serial_cb = refresh
        self.connect_serial_cb = connect
        self.get_connect_status_cb = status
        self.disconnect_serial_cb = disconnect
        self.serial_write_cb = write

    def communicat_serial_write(self, data):
        if self.serial_write_cb!=0:
            if not isinstance(data, str):
                data = str(data)  # 将数据转换为字符串
            self.serial_write_cb(data.encode())
        else:
            print("error!")

    def close_window(self):
        self.p_window.destroy()
        if self.def_function != 0:
            self.def_function()

    def win_fun_reset_serial(self):  # 刷新串口列表 Refreshing the serial port list
        print("刷新串口列表")
        self.ports_list = self.refresh_serial_cb()
        self.tupleVar = []
        for comport in self.ports_list:
            # print(list(comport)[0], list(comport)[1])
            self.tupleVar.append(""+list(comport)[0]+list(comport)[1])

        v = self.dropdown_serial
        self.optionMenu_serial['menu'].delete(0, 'end')
        for op in self.tupleVar:
            self.optionMenu_serial['menu'].add_command(label=op, command=lambda x=op: v.set(x))
        v.set(self.tupleVar[0])

    def win_fun_connect_serial(self):
        if self.serial_connect_status:
            self.disconnect_serial_cb()
            ret = self.get_connect_status_cb()
            if ~ret:
                self.serial_connect_button.config(text="断开")
                self.serial_connect_status = 0
                self.win_fun_insert_serial_text("断开\n")
        else:
            for comport in self.ports_list:
                if self.dropdown_serial.get() == ("" + list(comport)[0] + list(comport)[1]):
                    print(list(comport)[0] + list(comport)[1])
                    self.dropdown_serial.set(list(comport)[0])
                    print(list(comport)[1])
                    self.target_serial = list(comport)[0]
            self.target_serial_rate = self.serial_bit_textbox.get("1.0", "end")  # 获取文本输入框的内容
            self.setting.update_setting(his_serial_rate=self.target_serial_rate) # 把波特率储存到设置文件里
            self.win_fun_insert_serial_text("连接串口:"+self.target_serial+"  bate:"+self.target_serial_rate)
            self.connect_serial_cb(self.target_serial, int(self.target_serial_rate))
            ret = self.get_connect_status_cb()
            if ret:
                self.win_fun_insert_serial_text("串口已连接\n")
                self.serial_connect_button.config(text="连接")
                self.win_fun_insert_serial_text("连接\n")
                self.serial_connect_status = 1
            else:
                self.win_fun_insert_serial_text("串口连接失败\n")
                self.serial_connect_status = 0


        # self.p_window.update()



    def win_fun_reset_text_serial(self):
        self.text_box_serial_display.delete("1.0", tk.END)

    def win_fun_insert_serial_text(self, text=""):
        self.text_box_serial_display.insert(tk.END, text)
        self.text_box_serial_display.see(END)

    def win_fun_choose_text_serial(self, dropdown):
        print("choose:", dropdown)

    def win_fun_wifi_connect(self):
        self.wifi_password = self.test_wifi_pass.get("1.0", "end")  # 获取文本输入框的内容
        print("pass word:",self.wifi_password)  # 输出结果
        reminder = "发送WiFi->ssid:"+self.test_wifi_name+" password:"+self.wifi_password
        self.win_fun_insert_serial_text(reminder)
        commend = "AT+CWJAP="+self.test_wifi_name+","+self.wifi_password
        self.communicat_serial_write(commend)

        self.setting.update_setting(his_wifi_password=self.wifi_password)  # 把波特率储存到设置文件里

    def win_view_dropdown_serial(self, x_=200, y_=200):
        self.dropdown_serial = tk.StringVar()
        self.dropdown_serial.set("串口")
        # 这里必须要带*号，要不然解释器会认为是一个数据，只会显示一行的
        self.optionMenu_serial = tk.OptionMenu(self.p_window, self.dropdown_serial, *self.tupleVar, command=self.win_fun_choose_text_serial)
        self.optionMenu_serial.place(x=x_, y=y_, width=120)
        # optionMenu.pack()


    def win_view_text_serial(self, x_=20, y_=10):
        # 创建文本框
        self.text_box_serial_display = tk.Text(self.p_window)  # 创建文本框，指定宽和高
        self.text_box_serial_display.pack()  # 将文本框添加到窗口
        self.text_box_serial_display.place(x=x_, y=y_, width=600, height=400)
        # self.text_box_serial_display.configure(state='disabled')
        self.text_box_serial_display.see(END)

        # 滚动条
        scrollbar = tk.Scrollbar(self.p_window, command=self.text_box_serial_display.yview)
        scrollbar.place(x=x_+600, y=y_, width=20, height=400)

    def win_view_serial_set(self, x_=10, y_=12):
        button = tk.Button(self.p_window, text="刷新串口", command=self.win_fun_reset_serial)
        button.place(x=x_, y=y_)
        # button.pack()

        lable_wifi = tk.Label(self.p_window, text='波特率:')
        lable_wifi.place(x=x_, y=y_+50)

        self.serial_bit_textbox = tk.Text(self.p_window)  # 创建文本框，指定宽和高
        self.serial_bit_textbox.place(x=x_+80, y=y_+50, width=116, height=25)
        if self.setting.his_serial_rate != 0:
            self.serial_bit_textbox.insert(tk.END, self.setting.his_serial_rate)
        self.serial_connect_button = tk.Button(self.p_window, text="断开", command=self.win_fun_connect_serial)
        self.serial_connect_button.place(x=x_, y=y_+50+50)

        button = tk.Button(self.p_window, text="清除", command=self.win_fun_reset_text_serial)
        button.place(x=x_, y=y_+50+50+50)
        # button.pack()

    def win_view_wifi_set(self, x_=10, y_=110):
        lable_wifi = tk.Label(self.p_window, text='wifi:')
        lable_password = tk.Label(self.p_window, text='pass:')
        lable_wifi.place(x=x_, y=y_)
        lable_password.place(x=x_, y=y_+30)
        # 创建文本框
        test_wifi_name = tk.Text(self.p_window)  # 创建文本框，指定宽和高
        test_wifi_name.place(x=x_+40, y=y_, width=150, height=25)
        self.test_wifi_name = get_wifi_ssid()
        test_wifi_name.insert(tk.END, self.test_wifi_name)

        self.test_wifi_pass = tk.Text(self.p_window)  # 创建文本框，指定宽和高
        self.test_wifi_pass.place(x=x_ + 40, y=y_+30, width=150, height=25)
        if self.setting.his_wifi_password != 0:
            self.test_wifi_pass.insert(tk.END, self.setting.his_wifi_password)

        button = tk.Button(self.p_window, text="确定", command=self.win_fun_wifi_connect)
        button.place(x=x_, y=y_+65)

    def create_window_handle(self):
        print("create thread")

        self.p_window.title("win")
        self.p_window.geometry("850x700+300+300")
        self.p_window.resizable(False, False)

        self.win_view_dropdown_serial(x_=90, y_=10)  # 显示下拉框选择串口

        self.win_view_serial_set(x_=10, y_=12)  # 显示串口部分

        self.win_view_text_serial(x_=220, y_=12)  # 显示串口接收文本框

        self.win_view_wifi_set(x_=10, y_=170)  # 显示设置WiFi部分

        self.p_window.protocol("WM_DELETE_WINDOW", self.close_window)  # 接收到关闭点击操作的语句

        self.win_fun_reset_serial() # 程序启动刷新
        
        self.p_window.mainloop()  # 必须一直更新窗口，不然会未响应，如果要自行更新，可以用window.update()
        print("close window")

    def init_window(self):
        # 创建新线程
        # _thread.start_new_thread(self.create_window_handle, ("Thread-window", ))
        pass

