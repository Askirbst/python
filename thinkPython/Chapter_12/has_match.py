def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

t1 = ['a', 'b', 'c', 'd']
t2 = ['a', 'b', 'c', 'd']

print(has_match(t1, t2))