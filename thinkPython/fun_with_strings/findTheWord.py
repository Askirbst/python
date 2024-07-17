def find_word(word):
    i = 0
    pairs_count = 0
    length = len(word)

    if length < 6:
        return False
    
    while i < length - 1:
        if pairs_count >= 3:
            return True
        
        if word[i] == word[i + 1]:
            i += 2
            pairs_count += 1
        elif pairs_count < 3:
            i += 1
            pairs_count = 0

        
fin = open("/GitHub/python/thinkPython/strings/words.txt")

if fin:
    for line in fin:
        word = line.strip()
        if find_word(word):
            print(word)