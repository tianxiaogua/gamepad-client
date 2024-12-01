import pywifi


def get_wifi_ssid():
    # 抓取网卡接口
    wifi = pywifi.PyWiFi()

    # 获取无线网卡
    ifaces = wifi.interfaces()[0]

    # 获取无线网卡信息
    profile = ifaces.scan_results()[0]

    return profile.ssid

if __name__=="__main__":
    ssid = get_wifi_ssid()
    print(ssid)