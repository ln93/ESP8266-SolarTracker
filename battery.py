def get_battery():#使用14500磷酸铁锂电池,浮充于开发板3.3V上,设工作范围为2.9-3.3V
    from machine import ADC
    adc=ADC(0)
    percent=100*(3.3*adc.read()/1024-2.9)/0.4
    if percent>100:
        percent=100
    elif percent<0:
        percent=0
    return percent
