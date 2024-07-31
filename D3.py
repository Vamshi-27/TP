# Design 3

import turtle
import colorsys

turtle.setup(800, 600)
turtle.speed(0)  
turtle.bgcolor("black")

sides = 6
repetitions = 72
angle = 360 / sides

hue = 0
colors = []

for i in range(repetitions):
    colors.append(colorsys.hsv_to_rgb(hue, 1.0, 1.0))
    hue += 1 / repetitions

for i in range(repetitions):
    turtle.pencolor(colors[i])
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)
    turtle.right(5)

turtle.hideturtle()
turtle.done()
