def right_justify(s):
    str = s
    strLen = len(str)
    spaces = 70 - strLen
    spaceList = []

    for i in range(spaces):
        spaceList.append(' ')
  
    spaceList.append(str)
    for i in range(spaces + 1):
        print(spaceList[i], end='')

##right_justify('purple')

def do_twice(f, val):
    f(val)
    f(val)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(foo, val):
    do_twice(foo, val)
    do_twice(foo, val)

## do_four(print, 'test')

def horizontal_line():
    print('+', end=' ')
    print('- - - -', end=' ')

def vertical_line():
    print('|         ' * 5)

def column_border(foo):
    foo()
    foo()
    foo()
    foo()
    print('+')

def row_border(foo):
    foo()
    foo()
    foo()
    foo()

def print_row():
    column_border(horizontal_line)
    row_border(vertical_line)

def print_grid(foo):
    foo()
    foo()
    foo()
    foo()
    column_border(horizontal_line)

print_grid(print_row)
