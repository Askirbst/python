def is_abcedarian(string):
    length = len(string)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            #print(f"String1: {string[i]}\nString2: {string[j + i + 1]}")
            if ord(string[i]) > ord(string[j + i + 1]):
                return False
    return True

try_this = input("Enter word to check if it is abcedarian\n")
print(is_abcedarian(try_this))