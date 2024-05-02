import turtle
import math

bob = turtle.Turtle()

size = 100
petal_number = 8
petal_angle = int(360 / petal_number)
petal_width = 0

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = (2 * math.pi * r * angle / 360) + petal_width
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = (angle + petal_width)/ n

    polyline(t, n, step_length, step_angle)

def petal(t, n, angle):
    arc(t, n, angle)
    t.lt(180 - petal_angle - petal_width)
    arc(t, n, angle)
    t.lt(180 - angle + petal_angle - petal_width)

def flower(t, n, petals, angle):
    for i in range(petals):
        petal(t, n, angle)

flower(bob, size, petal_number, petal_angle)

turtle.mainloop()
