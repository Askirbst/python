def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x != y:
            return False
    return True

t1 = ('a', 'b', 'c')
t2 = ('a', 'b', 'c')

print(has_match(t1, t2))