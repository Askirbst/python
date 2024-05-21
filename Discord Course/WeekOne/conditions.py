'''2. Conditions:'''

# Write a program to check if a given number is even or odd.

num = int(input("Enter number: "))

if num % 2 == 0:    # If when the number provided is divided by 2 and the remainder is 0 we know it must be even
    print(num, 'is even')
else:
    print(num, 'is odd')

# Write a program to find the largest among three numbers.

num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
num3 = int(input("3nd number: "))

def isLargest(num1, num2, num3):    # This function sorts the list of numbers from largest to smallest
    list = [num1, num2, num3]
    temp = 0
    for i in range(2):
        for j in range(2):
            if list[j + 1] > list[i]:
                temp = list[i]       
                list[i] = list[j + 1]
                list[j + 1] = temp

    return list[0]
bigNum = isLargest(num1, num2, num3) # The sorting function is called and the sorted list of numbers is stored in the 'list' list

print(bigNum)    # Then the first element in the list that we now know to be the largest is printed to the terminal