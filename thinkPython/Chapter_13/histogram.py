import string


def process_file(file_name):
    hist = dict()
    fp = open(file_name, 'r', encoding="utf-8")
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.whitespace + string.punctuation)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

hist = process_file('C:/GitHub/python/thinkPython/Chapter_13/emma.txt')

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)


def most_common(hist):
    t = []
    for key, val in hist.items():
        t.append((val, key))
    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    t = most_common(hist)
    print('The most common words are:')
    for freq, word, in t[:num]:
        print(word, freq, sep='\t')

print_most_common(hist, 5)

def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

words = process_file('C:/GitHub/python/thinkPython/words.txt')
diff = subtract(hist, words)

print("Words in the book that aren't in the word list:")
for word in diff:
    print(word, end=' ')

def set_subtract(d1, d2):
    return set(d1) - set(d2)

set_diff = set_subtract(hist, words)

print("Using 'set' to find the words:")
for word in set_diff:
    print(word, end=' ')

