def make_list():
    fin = open("F:/Programming/Git_Python/python/thinkPython/words.txt")
    t = []
    for line in fin:
        t.append(line[:-1])
    return t


def fill_dict():
    d = {}
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n' , 'p' , 'r', 's', 't', 'v', 'w']
    for i in range(len(consonants)):
        for j in range(i + 1, len(consonants)):
            d.setdefault((consonants[i], consonants[j]), [])
    return d


def swap_letters(p, s):
    i = s.index(p[0])
    j = s.index(p[1])

    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return ''.join(s_list)


def metathesis_pairs(d, t):
    counter = 0
    for word in t:
        for key in d:
            if key[0] in word and key[1] in word:
                new_word = swap_letters(key, word)
                if new_word in t:
                    d[key].append((word, new_word))
                    counter += 1
                    print(f"New word found\n{counter}")
    return d

t = make_list()
d = fill_dict()

new_d = metathesis_pairs(d, t)
print(new_d)