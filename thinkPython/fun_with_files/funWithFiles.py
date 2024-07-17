#fin = open('words.txt')

def has_no_e(file):
    count = 0
    e_count = 0
    for line in file:
        word = line.strip()
        if 'e' in word:
            print(word)
            e_count += 1
        count += 1
    percentage = e_count / count 
    print(f"Percentage of words that have an e is: {int(percentage * 100)}%")

#has_no_e(fin)

fin = open('words.txt')
count = 0
letters = input("Enter some forbidden letters: ")

def avoid(s, forbidden):
    for i in range(len(forbidden)):
        letter = forbidden[i]
        print(letter)
        if s.find(letter) != -1:
            return False
    return True

for line in fin:
    word = line.strip()
    if avoid(word, letters) == True:
        count += 1
print(count)