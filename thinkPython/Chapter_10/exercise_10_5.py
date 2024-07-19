def is_sorted(lis):
    j = 1
    length = len(lis) - 1
    for i in range(length):
        if lis[i] > lis[j]:
            return False
        j += 1
    return True

t = ['a', 'b', 'z', 'd', 'e', 'f']

print(is_sorted(t))