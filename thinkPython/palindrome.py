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
        
print(is_palindrome("racecar"))