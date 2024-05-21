'''6. Variables and Conditions:'''

# Write a program that takes a number as input and prints "positive" if it's greater than zero, "negative" if it's less than zero, and "zero" if it's equal to zero.

num = int(input('Enter a whole number: '))

if num > 0:
    print('positive')
elif num < 0:
    print('negative')
elif num == 0:
    print('zero')


# Write a program that takes a year as input and determines if it's a leap year or not. (Any year that is evenly divisible by 4 is a leap year)

year = int(input("Enter a year to check if it's a leap year: "))

if year % 4 == 0:
    print("It's a leap year!")
else:
    print('Not a leap year')

'''7. Strings and Conditions:'''

# Write a program that takes a string input from the user and checks if it contains only digits.

userString = input("Please enter a string: ")

if userString.isnumeric():
    print(userString, 'is only digits.')
else:
    print(userString, 'contains characters other than numerical digits.')

'''8. Variables and Strings:'''

# Write a program that takes a string input from the user and counts the number of words in it.

userString = input("Please enter a string: ")

wordsList = []
notCharList = [' ', '.', ',', '?', '!']
word = ''

for char in userString:
    if char not in notCharList:
        word = word + char
    elif char in notCharList and len(word) != 0:
        wordsList.append(word)
        word = ''       

if word != '':  # Appends the last word in the string to wordsList 
    wordsList.append(word)

wordCount = len(wordsList)

print("The number of words in the string", userString, "is: ", wordCount)

'''9. Conditions and Strings:'''

# Write a program that takes two strings as input and concatenates them only if they have different lengths; otherwise, it returns "Lengths are equal."

str1 = input('Enter a string: ')
str2 = input('Enter another string: ')

if len(str1) != len(str2):
    print(str1 , str2)
else:
    print('Lengths are equal')

'''10. Advanced Conditions and Variables:'''
# Write a program that calculates the BMI (Body Mass Index) given the weight (in kilograms) and height (in meters) of a person.

weight = int(input('Please enter weight in kilograms: '))
height = float(input('Please enter height in meters: '))

bmi  = int(weight / (height ** 2))

print('Your BMI is', bmi)

# Write a program that simulates a simple text-based quiz with multiple-choice questions. The program should ask the user questions, provide options, and give feedback on correctness.
yes = ['y', 'Y', 'yes', 'Yes', 'YES', 'yea', 'yeah', 'Yea', 'Yeah', 'yay', 'YAY', 'Yay']
a = ['a', 'A']
b = ['b', 'B']
c = ['c', 'C']

answer = input("Welcome to your Pop Quiz! Are you ready?\n Y or N: ")

if answer in yes:
    answer = input("Question 1: What symbol do we use when we want to add comments to a python program?\nA.) %\nB.) &\nC.) #\n")
    while (answer not in c) and answer != '#':
        answer = input("Incorrect. Try again: ")
    print("Correct!")
    answer = input("Question 2: Which keyword allows one to load a module in Python?\nA.) load\nB.) import\nC.) include\n")
    while (answer not in b) and answer != 'import':
        answer = input("Incorrect. Try again: ")
    print("Correct")
    answer = input("Question 3: Which function can add elements to the end of a list?\nA.) append()\nB.) insert()\nC.) add()\n")
    while (answer not in a) and answer != 'append' and answer != 'append()':
        answer = input("Incorrect. Try again: ")
    print("Great Job! You passed!")
else:
    print("Come back when you are ready :)")