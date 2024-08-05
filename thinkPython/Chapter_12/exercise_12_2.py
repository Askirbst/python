def make_list():
    fin = open("F:/Programming/Git_Python/python/thinkPython/words.txt")
    t = []
    for line in fin:
        t.append(line[:-1])
    return t


def sort_string(s):
    return ''.join(sorted(s))


def print_anagrams(d):
    for key in d:
        if len(d[key]) > 3 and len(d[key][0]) == 8:
            print(d[key])


def find_anagrams(t):
    d = {}
    for word in t:
        key = sort_string(word)
        key = tuple(key)
        d.setdefault(key, []).append(word)
    return d


t = make_list()
anagrams = find_anagrams(t)
#print_anagrams(anagrams)

def sort_anagrams(d):
    t = []
    for key in d:
        if len(d[key]) > 3:
            t.append(tuple(d[key]))
    sorted_t = sorted(t, key=len, reverse=True)

    print(sorted_t)

sort_anagrams(anagrams)