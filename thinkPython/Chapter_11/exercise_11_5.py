import math

def build_list(file):
    t = []
    for line in file:
        t.append(line.splitlines())
    return t


def in_bisect(t, value):
    length = len(t)
    if length <= 1:
        return False
    
    length = math.ceil(len(t) / 2)
    word = (t[length - 1])[0]
    if value == word:
        return True
    elif value > word:
        return in_bisect(t[length:], value)
    else:
        return in_bisect(t[0:length], value)


def rotate_word(s, n):
    word = s.lower()
    cypher = ''
    i = 0
    for c in word:
        if c in (' ', "'", '.', ',', '!', '-') or c.isnumeric():
            c2 = c
        elif (ord(c) + n) > 122:
            c2 = chr((ord(c) + n) - 26)
        elif (ord(c) + n) < 97:
            c2 = chr((ord(c) + n) + 26)
        else:
            c2 = chr(ord(c) + n)
        cypher += c2
        i += 1
    return cypher


def rotate_pairs(n):
    d = {}

    with open("C:/GitHub/python/thinkPython/Chapter_11/words.txt") as file:
        t = build_list(file)

    for s in t:
        word_rotated = rotate_word(s[0], n)
        if in_bisect(t, word_rotated):
            if d.setdefault(s[0], [word_rotated]) != [word_rotated]:
                print("found word")
                d[s[0]].append(word_rotated)
    
    return d

rot_pair_dict = rotate_pairs(7)
print(rot_pair_dict)