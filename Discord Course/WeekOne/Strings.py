'''3. Concatenation:'''

# Write a program to concatenate two strings and display the result.

str1 = input("Enter a string: ")
str2 = input("Enter another string: ")

print(str1, str2)

# Write a program that takes a string input from the user and prints it in reverse order.

def reverseString(s):
    reverseStr = ""
    for char in s:
        reverseStr = char + reverseStr    # This function iterates through the string character by character  
                                          # then creates a new string called reverseStr by adding char to the beginning of the new string
    return reverseStr

userString = input("Enter a string to be reversed: ")

reverseStr = reverseString(userString)

print(reverseStr)

'''4. Complex String Operations'''

# Write a program that takes a string input from the user and checks if it is a palindrome (reads the same forwards and backwards).

def reverseString(s):
    reverseStr = ""
    for char in s:
        reverseStr = char + reverseStr  # Similar idea here except we check it against the original string to see if they are equal

    return reverseStr

userString = input("Check if palindrome: ")

reverseStr = reverseString(userString)

if userString == reverseStr:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")

# Write a program that takes a sentence as input and counts the number of vowels in it.

def checkVowels(s):
    count = 0
    for char in s:
        if char in 'aeiouy':
            count = count + 1
    return count

userString = input("Check number of vowels: ")

numOfVowels = checkVowels(userString)

if numOfVowels == 0:
    print("No vowels")
else:
    print("Number of vowels is:", numOfVowels)