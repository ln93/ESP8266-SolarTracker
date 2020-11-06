import ntptime
from machine import RTC,Pin,SPI
import network
import utime
from ssd1306 import SSD1306_SPI
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
    
def roboco_animate(string,line,len,delay):
    for i in range(0,len):
        oled.text(str(string[i]),8*i,line,1)
        utime.sleep_ms(delay)
        oled.show()

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
        roboco_animate('\'SolarHost\'',40,11,80)
        while not sta_if.isconnected():         
            p2.value(0)
            utime.sleep_ms(200)
            p2.value(1)
            utime.sleep_ms(200)
            pass
    roboco_animate('Connecting',55,10,80)
    sync_ntp()
    sta_if.active(False)
    ap_if.active(False)
    p2.value(0)
    utime.sleep_ms(3000)
    p2.value(1)



spi=SPI(1)
oled=SSD1306_SPI(128,64,spi,Pin(4),Pin(5),Pin(15))
roboco_animate('PipSol-V1.2',10,11,80)
utime.sleep_ms(1000)
roboco_animate('Roboco Present',25,14,80)

rtc = RTC()
time = rtc.datetime()
utime.sleep_ms(1000)
oled.fill(0)
oled.show()
print('Time is outdated, Updating...')
roboco_animate('Sync online',10,11,80)
roboco_animate('Searching...',25,12,80)
connect_and_sync()
print('Local time(DST):')
print(rtc.datetime())






