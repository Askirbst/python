import math
'''
1. Print each element of a list using a while loop
'''
list = ['one', 2, 'three', 4]

index = 0
while index < len(list):
    print(list[index])
    index = index + 1

''' 
2. Get a number from a user, then print numbers from 0-100 while also telling if the number is even or odd. 
If the number is equal to the user's number, then tell the user that this number is equal to what the user gave you instead of telling if it is even or odd.
'''

userInput = int(input("Enter a number: "))

index = 0

def evenOrOdd(num):
    if num == userInput:
        return "equal to user's input" 
    elif num % 2 == 0:
        return 'even'
    else: return 'odd'

while index <= 100:
    print(f"{index} is {evenOrOdd(index)}")
    index = index + 1

for i in range(101):
    if i % 2 == 0:
        print(f"The number {i} is even")
    else:
        print(f"The number {i} is odd")

def largest(num1, num2, num3):
    nums = [num1, num2, num3]
    return max(nums)

print(largest(34, 18, 67))