from machine import RTC,Pin,PWM
import utime

def drive_motor()
    rtc = RTC()
    time = rtc.now()
    if time[3] > 7 and time[3] < 17:
        Angle = ((time[3]*60+time[4])-7*60)*150/600#10 hrs a day
        DutyNow = 1000*((Angle-90)/180 * 2+0.5)/20
        Pwm.duty(DutyNow)
        Pwm.init()
        utime.sleep_ms(500)
        Pwr.on()
        utime.sleep_ms(2000)
        Pwr.off()
        utime.sleep_ms(500)
        Pwm.deinit()

def pulse_sleep(second):#do something every 20sec to prevent BatteryPack stop power supply
    i=0
    while i<second/20:
        machine.lightsleep(20000000)#10sec
        i=i+1



Pwr=Pin(4,Pin.OUT)#power Motor
Pwr.off()
Pwm=PWM(Pin(5))#Motor PWM
Pwm.freq(50)
Pwm.duty(75)
Pwm.deinit()
while 1:
    drive_motor()
    pulse_sleep(1800)#drive motor every 0.5 hour
    


    
