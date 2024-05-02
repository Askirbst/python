import turtle
import math

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n):
    angle = 360 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

def draw_a(t, length):
    t.lt(45)
    polyline(t, 1, length, 45)
    t.rt(45)
    polyline(t, 1, length, 45)
    t.pu()
    x, y = t.pos()
    t.goto(x - 2 / 3 * length, y - 2 / 3 * length)
    t.pd()
    t.lt(135)
    t.fd(1/3 * length)

draw_a(bob, 50)
##def draw_b():
##
##def draw_c():
##
##def draw_d():
##
##def draw_e():
##
##def draw_f():
##
##def draw_g():
##
##def draw_h():
##
##def draw_i():
##
##def draw_j():
##
##def draw_k():
##
##def draw_l():
##
##def draw_m():
##
##def draw_n():
##
##def draw_o():
##
##def draw_p():
##
##def draw_q():
##
##def draw_r():
##
##def draw_s():
##
##def draw_t():
##
##def draw_u():
##
##def draw_v():
##
##def draw_w():
##
##def draw_x():
##
##def draw_y():
##
##def draw_z():

turtle.mainloop()