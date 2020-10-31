# ESP8266-SolarTracker
Use ESP8266 to drive solar panel to solar.


这是一个用小太阳能板对充电宝进行充电的项目。

现有的DIY太阳能板追踪器大多用光敏电阻之类的方案，在太阳底下工作不太靠谱。因此我决定写一个自己的方案。

我对PCB设计和打板不太在行，因此该方案主要使用成品模块进行链接。

我的太阳能板较大，9g舵机难以在断电的情况下支持太阳能板的角度，因此只做了一个自由度。

该方案使用ESP8266联网获取时间，根据时间计算太阳方位，最终驱动舵机指向太阳。

基于micropython。

## 硬件描述

### 材料：

[NodeMCU开发板x1](https://detail.tmall.com/item.htm?spm=a1z0d.6639537.1997196601.22.3d487484JcBHzd&id=535588732894)

[5V继电器x1](https://detail.tmall.com/item.htm?id=15909056050&spm=a1z09.2.0.0.23362e8d39jsqp&_u=1ujvcor499d)

[180度SG90舵机和云台](https://item.taobao.com/item.htm?spm=a230r.1.14.82.49532d31qkZ2OA&id=612463363006&ns=1&abbucket=3#detail)

（我拆掉了上面的俯仰舵机和支架，然后用502把太阳能板黏在方位舵机支架上。你们大概会比我更有经验吧）

跳线，硬纸板若干

充电宝x1

[5W太阳能电池板（共享单车拆机型号，带稳压USB）x1](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.23692e8dV7nGi3&id=611377225857&_u=1ujvcorba8b)

除充电宝外，花了一百块钱吧。

### 设计理念

太阳能板固定仰角，由一个舵机控制方位。全套设备底座朝南放置，对充电宝进行供电。

ESP8266控制继电器和舵机PWM。继电器控制舵机供电。两者的电源均来自于充电宝。

上电后，ESP8266将执行boot.py，尝试连接硬编码的wifi地址，并且获得时间。之后关闭网络进入自律模式，

之后，8266将执行main.py，在7-17时，ESP8266将每半小时根据时间计算当前太阳方位，操作太阳能板指向太阳。

在空闲时间，ESP8266大多数时间处于休眠状态，但每20秒将自我唤醒，产生较高的短时间电流，以强迫充电宝不断电。

我使用一块5W太阳能板，一天实测大约可以为充电宝充入5000-7000mah电量。整套系统平均功耗10mw，一昼夜原则上仅消耗60-70mah，可喜可贺。

## TODO

1.加上地磁计，换用360度舵机，从而实现想放哪就放哪，想怎么放就怎么放。

2.可以改用8266的AP模式，令手机连接后发送时间给8266，去除愚蠢的硬编码。
