def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if inverse.setdefault(val, [key]) != [key]:
            inverse[val].append(key)
    return inverse
    

h = histogram("supercalifrageliciousexpialidocious")

print(h)

inverse_h = invert_dict(h)

print(inverse_h)