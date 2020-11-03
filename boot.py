import ntptime
from machine import RTC
def sync_ntp():   
    ntptime.NTP_DELTA = 3155644800   # 可选 UTC+8偏移时间（秒），不设置就是UTC0
    ntptime.host = 'ntp1.aliyun.com'  # 可选，ntp服务器，默认是"pool.ntp.org"
    ntptime.settime()   # 修改设备时间,到这就已经设置好了

def connect_and_sync():
    import network
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('719', '')
        while not sta_if.isconnected():
            pass
    sync_ntp()
    sta_if.active(False)


rtc = RTC()
time = rtc.datetime()
if(time[0]<2020):
    print('Time is outdated, Updating...')
    connect_and_sync()


