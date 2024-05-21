import turtle
import math

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polyline_Rt(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)

def polygon(t, length, n):
    angle = 360 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)

def arc_Rt(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline_Rt(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

def draw_a(t, length, angle):
    t.width(4)
    t.lt(angle)
    polyline(t, 2, length, (180 + angle))
    t.rt(angle)
    t.fd(25)
    t.lt(angle)
    t.fd(25)


#draw_a(bob, 50, 60)

def draw_b(t, length):
    t.width(4)
    t.rt(90)
    t.fd(length)
    t.lt(90)
    for i in range(2):
        arc(t, length / 4, 180)
        t.lt(180)


#draw_b(bob, 100)

def draw_c(t, length):
    t.rt(135)
    arc_Rt(t, length / 2, 270)

draw_c(bob, 100)

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