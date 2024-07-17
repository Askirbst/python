def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 2:
        return
    elif not is_palindrome(middle(word)):
        return False
    
    if first(word) == last(word):
        return True
    else:
        return False
        
print(is_palindrome("asdfggfdsa"))