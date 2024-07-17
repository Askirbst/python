def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1    
    return -1

def count(word, letter):
    count = 0
    for char in word:
        if letter == char:
            count += 1

#print(find('earth', 'r', 1))

word = 'earth'
#print(word.center(9, "-"))

banana = 'banana'
#print(banana.count('a', 1))

word1 = 'racecar'
#print(word1 in word1[::-1])

def any_lowercase(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
        
#print(any_lowercase('PICKLE'))

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#print(any_lowercase4('PICKLe'))

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5('pick.le'))