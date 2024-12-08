import json
import os

class app_set:
    def __init__(self):
        self.his_serial_rate = 0

        self.his_wifi_password = 0

        self.cfg_setting_path = "settings/settings.json"

        self.settings = 0
        os.makedirs('settings', exist_ok=True)
        self.read_settings_from_json(self.cfg_setting_path)

    # 将设置写入到 JSON 文件
    def write_settings_to_json(self, settings, filename):
        with open(filename, 'w') as f:
            json.dump(settings, f, indent=4)

    # 从 JSON 文件读取设置
    def read_settings_from_json(self, filename):
        with open(filename, 'r') as f:
            self.settings = json.load(f)
            self.his_serial_rate = self.settings["his_serial_rate"]
            print(self.his_serial_rate)
            self.his_wifi_password = self.settings["his_wifi_password"]
            print(self.his_wifi_password)

    def update_setting(self, his_serial_rate=0, his_wifi_password=0):
        self.read_settings_from_json(self.cfg_setting_path)
        if his_serial_rate != 0:
            self.settings["his_serial_rate"] = his_serial_rate
        if his_wifi_password != 0:
            self.settings["his_wifi_password"] = his_wifi_password
        self.write_settings_to_json(self.settings, self.cfg_setting_path)


if __name__ == "__main__":
    cset = app_set()
    cset.update_setting(his_serial_rate=2222)
