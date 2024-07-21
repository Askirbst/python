import math


'''

First function will build a list of strings from the file words.txt

'''
def build_list_append():
    t = []
    with open("F:/Programming/Git_Python/python/thinkPython/Chapter_10/words.txt") as file:
        for line in file:
            t.append(line.strip())
    return t


'''

These functions check for words that are palindromes as not to include in the final check

'''
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) < 2:
        return True

    if first(word) == last(word):
        return is_palindrome(middle(word))
    else:
        return False


'''

This function uses recursion to do a binary search of the list for the word passed in as value

'''
def in_bisect(t, value):
    is_word = False
    length = len(t)
    if length <= 1:
        return False
    
    length = math.ceil(len(t) / 2)
    word = (t[length - 1])
    if value == word:
        return True
    elif value > word:
        is_word = in_bisect(t[length:], value)
    else:
        is_word = in_bisect(t[0:length], value)

    return is_word


'''

This function prints a new element of a list on a new line

'''
def print_list(lis):
    for element in lis:
        print(element)


'''

This function will reverse the word first before passing it to in_bisect(),
then creates a list of all words that are in a reverse pair with their accompanied pair

'''
def reverse_pair(t):
    reverse_pairs = []
    for word in t:
        if is_palindrome(word) == False:
            if in_bisect(t, word[::-1]):
                reverse_pairs.append(word + ', ' + word[::-1])
    print_list(reverse_pairs)


lis = build_list_append()
reverse_pair(lis)