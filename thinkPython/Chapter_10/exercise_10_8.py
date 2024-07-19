import random

'''

If there are 23 students in your class, what are the odds that two of you have the same birthday.
Generate 23 random birthdays, then check for matches.
Create a function that takes a number as a parameter and checks if there is a matching birthday from a random list of dates

'''

def make_calender():
    calender = []
    month = ['Jan', 'Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for mon in month:
        for j in range(31):
            if mon == 'Feb' and j == 29:
                break
            elif mon in ['Apr', 'Jun', 'Sep', 'Nov'] and j == 30:
                break
            else:
                calender.append([mon, j + 1])
    return calender


def make_birthday_list():
    class_birthdays = []
    calender = make_calender()
    for i in range(23):
        date = calender[random.randint(0, 365)]
        class_birthdays.append(date)
    return class_birthdays


def check_birthday():
    class_birthdays = make_birthday_list()
    length = len(class_birthdays) - 1
    for i in range(length):
        j = i + 1
        while j <= length:
            if class_birthdays[i] == class_birthdays[j]:
                return True
            j += 1
    return False


def find_probability():
    count = 0
    probability = 0
    while count <= 100:
        if check_birthday():
            probability += 1
        count += 1
    return probability


print(find_probability())