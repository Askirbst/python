dict_main = {}
word_list = []


def make_word_list():
    fin = open("C:/GitHub/python/thinkPython/words.txt")
    for line in fin:
        word_list.append(line[:-1])
    word_list.sort(key=len)


drop_letter_cache = {}
def drop_letter(s, sublist):
    if len(s) <= 0:
        return sublist
    
    if s in drop_letter_cache:
        for word in drop_letter_cache[s]:
            sublist.append(word)
        return sublist
    
    str_t = list(s)
    for n in range(len(str_t)):
        char = str_t.pop(n)
        new_s = ''.join(str_t)
        if new_s in word_list:
            sublist.append(new_s)
            res = drop_letter(new_s, sublist)
            drop_letter_cache.setdefault(s, [])
            if res != None:
                for word in res:
                    drop_letter_cache[s].append(word)
                return res
            else:
                return []
        else:
            str_t.insert(n, char)


def create_dict(file):
    with open(file_path, 'a') as file:
        for word in word_list:
            t = []
            t = drop_letter(word, t)
            if t != None and len(t) == len(word):
                file.write(f"{word}: {t}\n")
                file.flush()
    return


make_word_list()
file_path = 'C:/GitHub/python/thinkPython/Chapter_12/output.txt'
create_dict(file_path)