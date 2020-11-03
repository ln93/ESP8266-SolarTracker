from machine import RTC,Pin,PWM
import machine
import esp
import utime
def drive_motor():
    rtc = RTC()
    time = rtc.datetime()
    if time[4] > 7 and time[4] < 17 and time[6] > 35:
        Angle = ((time[4]*60+time[5])-7*60)*150/600#10 hrs a day
        DutyNow = 1000*((90-Angle)/180 * 2+1.5)/20
        Pwm.duty(int(DutyNow))
        Pwm.init()
        utime.sleep_ms(500)
        Pwr.on()
        utime.sleep_ms(2000)
        Pwr.off()
        utime.sleep_ms(500)
        Pwm.deinit()

Pwr=Pin(4,Pin.OUT)#power Motor
Pwr.off()
Pwm=PWM(Pin(12))#Motor PWM
Pwm.freq(50)
Pwm.duty(75)
Pwm.deinit()
drive_motor()
esp.deepsleep(20000000)
machine.soft_reset()

    


    
