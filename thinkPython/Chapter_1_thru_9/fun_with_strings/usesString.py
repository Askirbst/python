letters = 'acefhlo'

def uses_only(user_string, letters):
    for letter in user_string:
        if letter not in letters:
            return False
    return True
    
def remove_whitespace(s):
    string_list = s.split()
    new_sentence : str = ""
    for word in string_list:
        new_sentence += word
    return new_sentence

sentence = input("Enter a sentence that only contains: acefhlo\n")

user_string = remove_whitespace(sentence)
print(uses_only(user_string, letters))

def uses_only(user_word, required_letters):
    for letters in required_letters:
        if letters not in user_word:
            return False
    return True

vowels = "aeiouy"
word = remove_whitespace(input("Enter a sentence to check:\n"))
print(uses_only(word, vowels))