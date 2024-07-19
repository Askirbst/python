'''

Write a function called middle that takes a list and 
returns a new list that contains all but the first and last elements

'''

def middle(lis):
    new_lis = lis[1:-1]

    return new_lis

just_a_list = [1, 2, 3, 4, 5, 6]
new_just_a_list = middle(just_a_list)
print(new_just_a_list)