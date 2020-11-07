# ESP8266-SolarTracker

![Use ESP8266 to drive solar panel to solar.](https://github.com/ln93/ESP8266-SolarTracker/blob/main/example.jpg)

这是一个用小太阳能板对充电宝进行充电的项目。

现有的DIY太阳能板追踪器大多用光敏电阻之类的方案，制作过程看上去较为复杂，而且在太阳底下工作不太靠谱。因此我决定写一个自己的方案。

我对PCB设计和打板不太在行，因此该方案主要使用成品模块进行链接。

我的太阳能板较大，9g舵机难以在断电的情况下支持太阳能板的角度，因此只做了一个自由度。

该方案使用ESP8266联网获取时间，根据时间计算太阳方位，最终驱动舵机指向太阳，同时驱动oled显示当前时间。

基于micropython。

## 硬件描述

### 材料：

[NodeMCU开发板x1](https://detail.tmall.com/item.htm?spm=a1z0d.6639537.1997196601.22.3d487484JcBHzd&id=535588732894)

[180度SG90舵机和云台](https://item.taobao.com/item.htm?spm=a230r.1.14.82.49532d31qkZ2OA&id=612463363006&ns=1&abbucket=3#detail)
（我拆掉了上面的俯仰舵机和支架，然后用502把太阳能板黏在方位舵机支架上。你们大概会比我更有经验吧）

跳线，硬纸板若干

紫米10号充电宝x1（或者其他支持边冲边用，且具有小电流模式的充电宝。）

[5W太阳能电池板（共享单车拆机型号，带稳压USB）x1](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.23692e8dV7nGi3&id=611377225857&_u=1ujvcorba8b)

7针SPI SSD1306 OLED屏幕x1（满大街都是，9.9包邮）

14500磷酸铁锂电池x1或耐压值不小于4V的超级电容(>0.5F)x1或USB充电器x1或全新的碱性电池x2（满大街都是，9.9包邮）。不建议使用两节镍氢电池（虽然确实能启动，但大概会过充）。

除充电宝外，花费一百块钱左右。

亦可以使用单gpio的8266-01开发板，不使用oled屏幕，直接对舵机供电并控制。这大概可以额外节约十几至二十元。

### 设计理念

太阳能板固定仰角，由一个舵机控制方位。全套设备底座朝南放置，对充电宝进行供电。

ESP8266控制舵机PWM（GPIO12）和SSD1306 OLED屏幕（SPI1），ADC连在V3.3上作电量检测之用（仅限NODEMCU开发板）。电源来自一节直连V3.3的磷酸铁锂电池（亦可USB直连太阳能板，此时建议V3.3挂一个超级电容满足瞬时功耗）。

上电后，ESP8266将执行boot.py，在屏幕上显示当前状态，同时自动尝试连接ssid为SolarHost的无密码wifi，以联机计算太阳时。对于没有屏幕的套件而言，8266还将闪烁指示灯并创建热点“Req_AP_SolarHost”提示用户。获得所需信息后，指示灯常亮三秒后熄灭，随后关闭网络以节能。

之后，8266将执行main.py，在7-17时，ESP8266将每120秒根据时间计算当前太阳方位，控制继电器对舵机上电，并产生pwm波，操作太阳能板指向太阳。在夜间，8266将控制太阳能板归位,降低屏幕亮度，并停止几乎所有活动。

在白昼时，ESP8266大多数时间处于轻度睡眠状态，但每隔3小时将尝试联网同步时间————如此高的频率是因为8266的RTC太糟糕了，一个小时能差五分钟。在8266尝试联网时，屏幕将显示天线图标。

受限于8266的ADC性能，当电池组电压下降到3V时，8266才能检测到电压下降。这已经是一个很低的值了，因此目前当检测到电压下降时，系统将直接关闭屏幕，仅保留舵机控制功能。换而言之，插电才能亮屏。


### 性能与功耗

我使用一块5W太阳能板，一天大约可以为充电宝充入5000-8000mah电量，略超一天三次手动掰太阳能板的充电能力。

夜晚即使保持8266和舵机上电，10000mah充电宝也没有显示掉电。估计夜晚待机消耗小于100mah。但使用oled屏会额外耗电。

在使用一节400mah的磷酸铁锂电池供电的情况下，包括屏幕和舵机在内的系统可以安全度过整个晚上。

## TODO

使用3.3v电压浮充磷酸铁锂效率极低。或许应该考虑别的方案。

