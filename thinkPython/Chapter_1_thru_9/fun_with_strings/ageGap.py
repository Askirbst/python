def check_age(gap, times_palindromic):
    age_gap = gap
    son = 0
    count = 0
    
    while son < 100:
        mother = son + age_gap

        if count == times_palindromic:
            return son
        
        if str(son).zfill(2)[-2] == str(mother).zfill(2)[-1] and str(son).zfill(2)[-1] == str(mother).zfill(2)[-2]:
            count += 1
        
        son += 1
        
    return -1


def age_gap(times_palindromic):
    age_gap = 5
    while age_gap < 50:
        son_age = check_age(age_gap, times_palindromic)

        if son_age != -1:
            print(f"Times Palindromic: {times_palindromic}\nSon's age: {son_age}, Age gap: {age_gap}")

        age_gap += 1

def check_age_palindrome():
    i = 1
    while i <= 8:
        age_gap(i)
        i += 1

check_age_palindrome()