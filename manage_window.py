import vgamepad as vg
import time
import _thread
import time
import serial
import serial.tools.list_ports
import tkinter as tk#要使用，先导入


class c_window_manage:  # 窗口管理
    p_window = 0
    def_function = 0
    text_box_serial_display = 0
    tupleVar = ('COM8 蓝牙链接上的标准串行 (COM8)', 'java', 'C', 'C++', 'C#')

    def __init__(self):
        self.p_window = tk.Tk()  # 创建一个窗口，因为后面还要用到所以用window这个变量来赋值，可以自行更改

    def close_window_register(self, func):
        print("register close window")
        self.def_function = func

    def close_window(self):
        self.p_window.destroy()
        if self.def_function != 0:
            self.def_function()

    def win_fun_reset_serial(self):  # 刷新串口列表 Refreshing the serial port list
        print("asdsaasd")

    def win_fun_reset_text_serial(self):
        self.text_box_serial_display.insert(tk.END, "asdasdasdasds")
        time.sleep(1)
        self.text_box_serial_display.delete("1.0", tk.END)
        self.text_box_serial_display.insert(tk.END, "sdakshjgdahsgdh")

    def win_fun_choose_text_serial(self, dropdown):
        print("choose:", dropdown)

    def win_view_dropdown_serial(self, x_=200, y_=200):
        dropdown = tk.StringVar()
        dropdown.set("串口")
        # 这里必须要带*号，要不然解释器会认为是一个数据，只会显示一行的
        optionMenu = tk.OptionMenu(self.p_window, dropdown, *self.tupleVar, command=self.win_fun_choose_text_serial)
        optionMenu.place(x=x_, y=y_, width=120)
        # optionMenu.pack()

    def win_view_button_reset_serial(self, x_=200, y_=200):
        button = tk.Button(self.p_window, text="刷新串口", command=self.win_fun_reset_serial)
        button.place(x=x_, y=y_)
        # button.pack()

    def win_view_button_clean_serial(self, x_=200, y_=200):
        button = tk.Button(self.p_window, text="清除串口", command=self.win_fun_reset_text_serial)
        button.place(x=x_, y=y_)
        # button.pack()


    def win_view_text_serial(self, x_=20, y_=10):
        # 创建文本框
        self.text_box_serial_display = tk.Text(self.p_window)  # 创建文本框，指定宽和高
        self.text_box_serial_display.pack()  # 将文本框添加到窗口
        self.text_box_serial_display.place(x=x_, y=y_, width=600, height=400)

    def create_window_handle(self):
        print("create thread")
        self.p_window.title("win")
        self.p_window.geometry("840x700+300+300")
        self.p_window.resizable(False, False)

        self.win_view_dropdown_serial(x_=90, y_=10)  # 显示下拉框选择串口
        self.win_view_button_reset_serial(x_=10, y_=12)  #显示按钮 用于刷新串口
        self.win_view_text_serial(x_=220, y_=12)  # 显示串口接收文本框
        self.win_view_button_clean_serial(x_=10, y_=60)  # 显示清除串口按钮


        self.p_window.protocol("WM_DELETE_WINDOW", self.close_window)  # 接收到关闭点击操作的语句
        self.p_window.mainloop()  # 必须一直更新窗口，不然会未响应，如果要自行更新，可以用window.update()
        print("close window")

    def init_window(self):
        # 创建新线程
        # _thread.start_new_thread(self.create_window_handle, ("Thread-window", ))
        pass

