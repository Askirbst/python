import time
import math
import turtle

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)

#countdown(3)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n - 1)

#print_n('Hello', 2)

def print_x():
    print("It works")

def do_n(func, n):
    if n <= 0:
        return
    func()
    do_n(func, n - 1)

#do_n(print_x, 3)

def timestamp(time):
    totalMinutes = time / 60
    totalHours = totalMinutes / 60
    totalDays = totalHours / 24
    daysRemain = totalDays % 365.25
    hoursRemain = totalHours % 24
    minutesRemain = totalMinutes % 60
    print(f"days:{math.floor(daysRemain)}\n{math.floor(hoursRemain)}:{math.floor(minutesRemain)}")

epoch = time.time()
#timestamp(epoch)

def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print("Holy smokes! Fermat was wrong!")
    else:
        print("No, that doesn't work")

#numA = int(input("Enter a number: "))
#numB = int(input("Enter a number: "))
#numC = int(input("Enter a number: "))
#numN = int(input("Enter a number: "))

#check_fermat(numA, numB, numC, numN)

def is_triangle(a, b, c):
    if a > b + c:
        print("It's NOT a triangle")
    elif b > a + c:
        print("It's NOT a triangle")
    elif c > a + b:
        print("It's NOT a triangle")
    else:
        print("It's a triangle!")

#sideA = int(input("Enter length of side A: "))
#sideB = int(input("Enter length of side B: "))
#sideC = int(input("Enter length of side C: "))

#is_triangle(sideA, sideB, sideC)

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)

#recurse(3, 0)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(angle * 2)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)

bob = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(1200, 800)
#draw(bob, 10, 8)

koch_length = 100

def koch(t, length):
    if length < 3:
        t.fd(length)
        return
    
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)
    t.rt(120)
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)

#bob.pu()
#bob.bk(600)
#bob.rt(90)
#bob.fd(300)
#bob.lt(90)
#bob.pd()

koch(bob, koch_length)
bob.rt(120)
koch(bob, koch_length)
bob.rt(120)
koch(bob, koch_length)

