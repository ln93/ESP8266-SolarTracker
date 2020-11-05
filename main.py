from machine import RTC,Pin,PWM
import machine
import esp
import utime

def motor_angle(ang):
    DutyNow = 1000*((90-ang)/180 * 2+1.5)/20
    Pwm.duty(int(DutyNow))
    Pwm.init()
    utime.sleep_ms(500)
    Pwr.on()
    utime.sleep_ms(2000)
    Pwr.off()
    utime.sleep_ms(500)
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
    rtc = RTC()
    time = rtc.datetime()#year,month,day,weekday,hour,minute,sec,msec

    if time[4] >= 7 and time[4] < 17:
        Angle = 15+((time[4]*60+time[5])-7*60)*150/600#very simple, 10 hrs a day,from 15-165 deg
        motor_angle(Angle)
        sleep(120,10)
    elif time[4] < 7 and time[4] >= 5:
        motor_angle(15)#prepare for morning
        sleep(1800,1800)
    else:
        motor_angle(90)#if batterypack is down at night, solar panel should be on a neural position
        # and it is convenient for debug
        sleep(3600,3600)



Pwr=Pin(4,Pin.OUT)#power Motor
Pwr.off()
Pwm=PWM(Pin(12))#Motor PWM
Pwm.freq(50)
Pwm.duty(75)
Pwm.deinit()

loopcnt=1
while 1:
    drive_motor()

    


    
