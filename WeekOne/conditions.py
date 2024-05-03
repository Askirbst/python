'''2. Conditions:'''

## Write a program to check if a given number is even or odd.

num = int(input("Enter number: "))

if num % 2 == 0:
    print(num, 'is even')
else:
    print(num, 'is odd')

## Write a program to find the largest among three numbers.

num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
num3 = int(input("3nd number: "))

def isLargest(num1, num2, num3):
    arr = [num1, num2, num3]
    temp = 0
    for i in range(2):
        for j in range(2):
            if arr[j + 1] > arr[i]:
                temp = arr[i]
                arr[i] = arr[j + 1]
                arr[j + 1] = temp

    return arr
arr = isLargest(num1, num2, num3)

print(arr[0])