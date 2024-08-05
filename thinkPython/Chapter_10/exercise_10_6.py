def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        str_lis1 = list(str1.lower())
        str_lis2 = list(str2.lower())

        str_lis1.sort()
        str_lis2.sort()

        if str_lis1 == str_lis2:
            return True
        else:
            return False
    
a_string = "monument"
b_string = "TNEMUBOM"

print(is_anagram(a_string, b_string))