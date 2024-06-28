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

