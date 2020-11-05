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
    fb.fill_rect(0,0,64,55,0)

def draw_round(fb,x,y,r):
    for i in range(x-r-1,x+r+2):
        for j in range(y-r-1,y+r+2):
            if (i-x)*(i-x)+(j-y)*(j-y)>(r-1)*(r-1) and (i-x)*(i-x)+(j-y)*(j-y)<(r+1)*(r):
                fb.pixel(i,j,1)
def draw_pip(fb):
    f=open("pip.txt")
    for i in range(0,63):
        for j in range(0,127):
            fb.pixel(j,i,1-int(f.read(1)))
    f.close()
    