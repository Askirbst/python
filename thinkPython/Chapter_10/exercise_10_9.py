fin = open('C:/GitHub/python/thinkPython/Chapter_10/words.txt')

def build_list_concat(file):
    t = []
    for line in file:
        t = t + [line.splitlines()]
    print("Done Concatenating")

#build_list_concat(fin)

def build_list_append(file):
    t = []
    for line in file:
        t.append(line.splitlines())
    print("Done Appending")

build_list_append(fin)