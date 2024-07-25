def dictionary(f):
    d = dict()
    i = 0
    for line in f:
        d[line.strip()] = i
        i += 1
    return d

fin = open("C:/GitHub/python/thinkPython/Chapter_11/words.txt")
d = dictionary(fin)

def find_word(d, s):
    if s in d:
        print(f"{s} is in the dictionary!")
    else:
        raise LookupError("Word not found")
    
find_word(d, 'apple')