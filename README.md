# ESP8266-SolarTracker
Use ESP8266 to drive solar panel to solar.

使用ESP8266联网获取时间，根据时间计算太阳方位，最终驱动舵机指向太阳。
基于micropython。

## 硬件描述

这是一个用小太阳能板对充电宝进行充电的项目。

太阳能板固定仰角，由一个舵机控制方位。全套设备底座朝南放置，对充电宝进行供电。

ESP8266控制继电器和舵机PWM。继电器控制舵机供电。两者的电源均来自于充电宝。

上电后，ESP8266将执行boot.py，尝试连接硬编码的wifi地址，并且获得时间。之后关闭网络进入自律模式，

之后，8266将执行main.py，在7-17时，ESP8266将每半小时根据时间计算当前太阳方位，操作太阳能板指向太阳。

在空闲时间，ESP8266大多数时间处于休眠状态，但每20秒将自我唤醒，产生较高的短时间电流，以强迫充电宝不断电。

我使用一块6W太阳能板，一天实测大约可以为充电宝充入5000-7000mah电量。整套系统平均功耗10mw，一昼夜原则上仅消耗60-70mah，可喜可贺。

## TODO

外挂MPU6050，换用360度舵机，从而实现想放哪就放哪，想怎么放就怎么放。
