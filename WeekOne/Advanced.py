'''5. Complex Conditions and Variables:'''

## Write a program that calculates the area of a triangle given its three sides using Heron's formula.

import math

def getLengths():

    len_arr = []
    
    for i in range(3):

        digit = input("Enter a whole number: ")

        while not digit.isnumeric():
            digit = input("Try Again: ")

        len_arr.append(int(digit))
    
    return len_arr

def calculateArea():

    triangle_sides = getLengths()

    a = triangle_sides[0]
    b = triangle_sides[1]
    c = triangle_sides[2]

    s = (a + b + c) / 2

    area = math.sqrt(s* (s - a) * (s - b) * (s - c))

    return area

areaOfTri = calculateArea()

print("The area of the triangle is: ", areaOfTri)

## Write a program that simulates a simple calculator, allowing the user to perform addition, subtraction, multiplication, and division operations on two numbers.

addition = ['+', 'add', 'addition', 'plus', 'sum']
subtraction = ['-', 'sub', 'subtraction', 'subtract', 'difference']
multiplication = ['*', 'x', 'X', 'multiply', 'multiplication']
division = ['/', 'division', 'divide']
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

operation = input("Choose operation (addition, subtraction, multiplication, or division): ")

if operation in addition:
    print(num1 + num2)
if operation in subtraction:
    print(num1 - num2)
if operation in multiplication:
    print(num1 * num2)
if operation in division:
    print(num1 / num2)