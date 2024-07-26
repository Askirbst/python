from pronounce import read_dictionary

d = read_dictionary()

def find_homophone(d):
    for i in d:
        first_letter_removed = i[1:]
        second_letter_removed = i[0] + i[2:]

        pronunciation_1 = d.get(i, 0)
        pronunciation_2 = d.get(first_letter_removed, 0)
        pronunciation_3 = d.get(second_letter_removed, 0)
        
        if type(pronunciation_1) == type(pronunciation_2) == type(pronunciation_3) == str:
            if pronunciation_1 == pronunciation_2 == pronunciation_3:
                print(i, first_letter_removed, second_letter_removed)

find_homophone(d)