def check(number):
    i = 0
    length = len(number)
    while i < length - 1:
        if number[i] != number[length - 1 - i]:
            return False
        else:
            i += 1
    return True

def ododrome(i):
    return (check(str(i)[2:]) and check(str(i + 1)[1:]) and check(str(i + 2)[1:-1]) and check(str(i + 3)))

def print_odometer():
    upper_limit = 999996
    i = 100000
    while i < upper_limit:
        if ododrome(i):
            print(f"{i}, {i + 1}, {i + 2}, {i + 3}")
        i += 1
    
print_odometer()