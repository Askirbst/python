##'''6. Variables and Conditions:'''
##
#### Write a program that takes a number as input and prints "positive" if it's greater than zero, "negative" if it's less than zero, and "zero" if it's equal to zero.
##
##num = int(input('Enter a whole number: '))
##
##if num > 0:
##    print('positive')
##elif num < 0:
##    print('negative')
##elif num == 0:
##    print('zero')
##
##
#### Write a program that takes a year as input and determines if it's a leap year or not. (Any year that is evenly divisible by 4 is a leap year)
##
##year = int(input("Enter a year to check if it's a leap year: "))
##
##if year % 4 == 0:
##    print("It's a leap year!")
##else:
##    print('Not a leap year')
##
##'''7. Strings and Conditions:'''
##
#### Write a program that takes a string input from the user and checks if it contains only digits.
##
##userString = input("Please enter a string: ")
##
##if userString.isnumeric():
##    print(userString, 'is only digits.')
##else:
##    print(userString, 'contains characters other than numerical digits.')

'''8. Variables and Strings:'''

## Write a program that takes a string input from the user and counts the number of words in it.

userString = input("Please enter a string: ")

wordsList = []

word = ''

for char in userString:
    if char != ' ':
        word = word + char
    elif char == ' ' and len(word) != 0:
        wordsList.append(word)
        word = ''       

if word != '':
    wordsList.append(word)

wordCount = len(wordsList)

print("The number of words in the string", userString, "is: ", wordCount)