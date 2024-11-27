
from manage_window import c_window_manage
from manage_commit import c_wired_connect
from manage_gamepad import c_gamepad_manage


gamepad_manage = c_gamepad_manage()
window_manage = c_window_manage()
wired_connect = c_wired_connect()

def close_app():
    gamepad_manage.deinit_gamepad_manage()
    wired_connect.deinit_wired_connect()

if __name__=="__main__":
    wired_connect.init_wired_connect()
    gamepad_manage.init_gamepad_manage()
    window_manage.close_window_register(close_app)
    window_manage.refresh_serial_register(wired_connect.refresh_serial_port)
    window_manage.create_window_handle()
