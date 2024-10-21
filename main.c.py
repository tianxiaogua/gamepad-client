import vgamepad as vg
import time

# 创建虚拟 XBox360 游戏手柄
gamepad = vg.VX360Gamepad()

# 按下 A 按钮
gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(0.5)

# 释放 A 按钮
gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(0.5)

# 按下左肩按钮
gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
gamepad.update()
time.sleep(0.5)

# 释放左肩按钮
gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
gamepad.update()
time.sleep(0.5)

# 重置游戏手柄状态
gamepad.reset()
gamepad.update()