import turtle
import math

bob = turtle.Turtle()

size = 100
numOfTris = input("Give value of n to draw an n-sided polygon: ")
isnumber = False

def check(num):
    while not num.isnumeric():
        num = input("Please enter a whole number: ")
    
    return num
        
numOfTris = int(check(numOfTris))

angle_C = 360 / numOfTris
angle_AB = (180 - angle_C) / 2 
side_a = size 

def findLengthC(side_a, angle_C):
    return int(math.sqrt((side_a**2 + side_a**2 - (2 * side_a * side_a * math.cos(math.radians(angle_C))))))

side_c = findLengthC(side_a, angle_C)

def triangle(t):
    t.fd(side_a)
    t.lt(180 - angle_AB)
    t.fd(side_c)
    t.lt(180 - angle_AB)
    t.fd(side_a)
    t.lt(180)

def turtlePie(t):
    for i in range(numOfTris):
        triangle(t)

turtlePie(bob)

turtle.mainloop()