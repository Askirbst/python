def has_duplicates(lis):
    for i in range(len(lis) - 1):
        if lis[i] in lis[i + 1:]:
            print(lis[i])
            return True
    
    return False

fruit = ['apple', 'orange', 'pear', 'grape', 'pear', 'banana', 'banana', 'pear']
#print(has_duplicates(fruit))


def dict_duplicates(lis):
    fruit_dict = {}
    for i in lis:
        fruit_dict[i] = fruit_dict.get(i, 0) + 1

    for key in fruit_dict:
        if fruit_dict[key] > 1:
            return True

print(dict_duplicates(fruit))