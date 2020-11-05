import ntptime
from machine import RTC,Pin
import network
import utime

def sync_ntp():  
    import ujson,urequests
    js=urequests.get("http://ip-api.com/json")
    parsed = ujson.loads(js.text)
    #lon=parsed["lon"]
    lon=120#北京时间
    print('Your lon is:'+str(lon))
    ntptime.NTP_DELTA = 3155673600-int(lon*86400/360)   # 可选 UTC+8偏移时间（秒），不设置就是UTC0
    ntptime.host = 'ntp1.aliyun.com'  # 可选，ntp服务器，默认是"pool.ntp.org"
    ntptime.settime()   # 修改设备时间,到这就已经设置好了
    rtc = RTC()
    print('Local time(DST):')
    print(rtc.datetime())


def connect_and_sync():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)
    ap_if.config(essid='Req_AP_SolarHost', channel=1)
    sta_if = network.WLAN(network.STA_IF)
    p2 = Pin(2, Pin.OUT)   
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('SolarHost', '')
        while not sta_if.isconnected():         
            p2.value(0)
            utime.sleep_ms(200)
            p2.value(1)
            utime.sleep_ms(200)
            pass
    sync_ntp()
    sta_if.active(False)
    ap_if.active(False)
    p2.value(0)
    utime.sleep_ms(3000)
    p2.value(1)

rtc = RTC()
time = rtc.datetime()
if(time[0]<2020):
    print('Time is outdated, Updating...')
    connect_and_sync()
print('Local time(DST):')
print(rtc.datetime())






