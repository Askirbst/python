def has_duplicates(lis):
    length = len(lis) - 1
    for i in range(length):
        j = i + 1
        while j <= length:
            if lis[i] == lis[j]:
                return True
            j += 1
    return False

fruit = ['apple', 'banana', 'orange', 'potato', 'orange']

print(has_duplicates(fruit))