from machine import RTC,Pin,PWM,SPI
import machine
import esp
import utime
from ssd1306 import SSD1306_SPI
import draw
import battery
def motor_angle(ang):
    DutyNow = 1000*((90-ang)/180 * 2+1.5)/20
    Pwm.duty(int(DutyNow))
    Pwm.init()
    utime.sleep_ms(2000)
    Pwm.deinit()

def sleep(sec,flashsec):
    from machine import Pin
    import utime
    p2 = Pin(2, Pin.OUT)
    while sec>1:
        sec=sec-flashsec
        utime.sleep_ms(flashsec*1000)
        p2.value(0)
        utime.sleep_ms(50)
        p2.value(1) 

def drive_motor():
    if time[4] >= 7 and time[4] < 17:
        Angle = 15+((time[4]*60+time[5])-7*60)*150/600#very simple, 10 hrs a day,from 15-165 deg
        if time[6]>45 and time[5]%2==0:
            motor_angle(Angle)
            oled.invert(True)
            draw.draw_solarpanel(oled,Angle)
        sleep(10,10)
        oled.contrast(100)
    elif time[4] < 7 and time[4] >= 5:
        if time[5]>58:
            motor_angle(15)#prepare for morning
            draw.draw_solarpanel(oled,15)
        sleep(30,30)
    else:
        if time[5]>58:
            motor_angle(90)#if batterypack is down at night, solar panel should be on a neural position
            # and it is convenient for debug
            draw.draw_solarpanel(oled,90)
        oled.contrast(10)
        oled.invert(False)
        sleep(60,60)
def frame():
    if(battery.get_battery()<50):
        oled.poweroff()#when battery low, only control solar panel,don't display
        return
    oled.poweron()
    draw.clear_left(oled)
    oled.text(str(time[0]),14,10,1)
    month=str(time[1])
    day=str(time[2])
    hour=str(time[4])
    minute=str(time[5])
    if(len(month)==1):
        month=' '+month
    if(len(day)==1):
        day='0'+day
    if(len(hour)==1):
        hour=' '+hour
    if(len(minute)==1):
        minute='0'+minute
    oled.text(month+'-'+day,10,25,1)
    oled.text(hour+':'+minute,10,40,1)
    oled.rect(5, 5, 50, 46, 1)
    draw.draw_battery(oled)
    oled.show()
def time_sync():
    import ntptime
    import network
    import utime
    sta_if = network.WLAN(network.STA_IF)
    p2 = Pin(2, Pin.OUT)   
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('SolarHost', '')
        while not sta_if.isconnected():         
            draw.draw_wifi(oled,True)
            oled.show()
            p2.value(0)
            utime.sleep_ms(200)
            p2.value(1)
            utime.sleep_ms(200)
            pass
    sync_ntp()
    sta_if.active(False)
    draw.draw_wifi(oled,False)


Pwm=PWM(Pin(12))#Motor PWM
Pwm.freq(50)
Pwm.duty(75)
Pwm.deinit()

spi=SPI(1)
oled=SSD1306_SPI(128,64,spi,Pin(4),Pin(5),Pin(15))
rtc = RTC()
p=rtc.datetime()
import draw
draw.draw_pip(oled)
oled.text('BAT:',4,56,1)
oled.contrast(10)

loopcnt=1
while 1:
    rtc = RTC()
    time = rtc.datetime()
    frame()
    oled.show()
    loopcnt=loopcnt-1
    if loopcnt<1:
        time_sync()
        loopcnt=1000
    drive_motor()

    

    


    
