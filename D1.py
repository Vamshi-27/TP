# Design 1

from turtle import *
import colorsys

speed(0)
bgcolor('black')
n = 0
for i in range(10):
    for j in range(14):
        c=colorsys.hsv_to_rgb(n,1,1)
        color(c)
        n += 0.005
        rt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6,90)
        rt(90)
    circle(40,20)
done()