import vgamepad as vg
import _thread
import time

class c_gamepad_manage:
    run_status = 0
    def __init__(self):
        self.run_status = 1

    def gamepad_handle(self, threadName):
        print("create thread",threadName)
        # 创建虚拟 XBox360 游戏手柄
        gamepad = vg.VX360Gamepad()
        while self.run_status:
            # 按下左肩按钮
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(0.5)

            # 释放左肩按钮
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(3)
        # 重置游戏手柄状态
        gamepad.reset()
        gamepad.update()
        print("close gamepad")

    def init_gamepad_manage(self):
        # 创建新线程
        _thread.start_new_thread(self.gamepad_handle, ("Thread-gamepad", ))

    def deinit_gamepad_manage(self):
        self.run_status = 0