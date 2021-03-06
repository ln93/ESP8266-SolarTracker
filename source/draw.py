def draw_sun(fb,x,y):
    draw_round(fb,x,y,5)
    fb.line(x-11,y,x-8,y,1)
    fb.line(x+11,y,x+8,y,1)
    fb.line(x,y-11,x,y-8,1)
    fb.line(x,y+11,x,y+8,1)
    fb.line(x-9,y-9,x-6,y-6,1)
    fb.line(x+9,y+9,x+6,y+6,1)
    fb.line(x+9,y-9,x+6,y-6,1)
    fb.line(x-9,y+9,x-6,y+6,1)
def clear_left(fb):
    fb.fill_rect(0,0,55,55,0)

def draw_wifi(fb,isconnecting):
    if isconnecting==True:
        draw_round(fb,66,40,2)
        fb.line(66,43,66,49,1)
        fb.line(62,39,62,41,1)
        fb.line(70,39,70,41,1)
    else:
        fb.fill_rect(62,38,9,12,0)
def draw_round(fb,x,y,r):
    for i in range(x-r-1,x+r+2):
        for j in range(y-r-1,y+r+2):
            if (i-x)*(i-x)+(j-y)*(j-y)>(r-1)*(r-1) and (i-x)*(i-x)+(j-y)*(j-y)<(r+1)*(r):
                fb.pixel(i,j,1)
def draw_pip(fb):
    f=open("pip.txt")
    #用文本文件存储128x64的图片，用字符0/1代表黑白，十分朴实。
    for i in range(0,63):
        for j in range(0,127):
            fb.pixel(j,i,1-int(f.read(1)))
    f.close()
def draw_battery(fb):
    import battery
    percent=battery.get_battery()
    fb.fill_rect(35,55,20,9,0)#clear
    fb.rect(35,55,20,9,1)
    fb.fill_rect(37,57,int(16*percent/100),5,1)
    fb.show()

def draw_solarpanel(fb,angle):
    fb.fill_rect(56,0,21,16,0)#clear
    fb.line(56,15-int(15*(angle/180)),76,int(15*(angle/180)),1)#panel
    draw_round(fb,66,9,2)#axis
    fb.line(56+7,0,56+7,3,1)#light
    fb.line(56+10,0,56+10,3,1)#light
    fb.line(56+13,0,56+13,3,1)#light
    