from machine import RTC,Pin,PWM,SPI
import machine
import esp
import utime
from ssd1306 import SSD1306_SPI
import draw
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
        sleep(10,10)
    elif time[4] < 7 and time[4] >= 5:
        if time[5]>58:
            motor_angle(15)#prepare for morning
        sleep(10,10)
    else:
        if time[5]>58:
            motor_angle(90)#if batterypack is down at night, solar panel should be on a neural position
            # and it is convenient for debug
        sleep(10,10)

def roboco_animate(string,line,len,delay):
    for i in range(0,len):
        oled.text(str(string[i]),8*i,line,1)
        utime.sleep_ms(delay)
        oled.show()


Pwm=PWM(Pin(12))#Motor PWM
Pwm.freq(50)
Pwm.duty(75)
Pwm.deinit()

spi=SPI(1)
oled=SSD1306_SPI(128,64,spi,Pin(4),Pin(5),Pin(15))
roboco_animate('Pipboy-V1.1',10,11,80)
utime.sleep_ms(1000)
roboco_animate('Roboco Present',25,14,80)
utime.sleep_ms(1000)
roboco_animate('loading...',40,10,80)
rtc = RTC()
p=rtc.datetime()
import draw
draw.draw_pip(oled)
oled.text(str(p[0]),10,10,1)
oled.text(str(p[1])+'-'+str(p[2]),10,25,1)
oled.text(str(p[4])+':'+str(p[5]),10,40,1)
oled.text('PipBoyV1.1',0,56,1)
oled.show()


loopcnt=1
while 1:
    rtc = RTC()
    time = rtc.datetime()
    draw.clear_left(oled)
    oled.text(str(time[0]),10,10,1)
    oled.text(str(time[1])+'-'+str(time[2]),10,25,1)
    oled.text(str(time[4])+':'+str(time[5]),10,40,1)
    oled.rect(5, 5, 50, 46, 1)
    oled.show()
    drive_motor()
    

    


    
