def get_battery():
#使用14500磷酸铁锂电池,浮充于开发板3.3V上,设工作范围为2.9-3.3V。
#但在实践中，发现我那块板子的ADC量程并不是0-3.3V，而是0-3V，不知道是不是个体问题，因此代码未做修正。
    from machine import ADC
    adc=ADC(0)
    percent=100*(3.3*adc.read()/1023-2.9)/0.4
    if percent>100:
        percent=100
    elif percent<0:
        percent=0
    return percent
