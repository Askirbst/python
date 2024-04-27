def right_justify(s):
    str = s
    strLen = len(str)
    spaces = 70 - strLen
    spaceList = []

    for i in range(spaces):
        spaceList.append(i + 1)
    
    spaceList.append(str)
    print(spaceList)

# right_justify('purple')

def do_twice(f, val):
    f(val)
    f(val)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(foo, val):
    do_twice(foo, val)
    do_twice(foo, val)

do_four(print, 'test')