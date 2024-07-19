''' 

Write a function called nested_sum that takes a list of lists of integers 
and adds up the elements from all of the nested lists

'''

def nested_sum(lis):
    total = 0
    for t in lis:
        total = total + sum(t)
    return total

list_of_lists = [[1, 2], [3, 4], [5], [6, 7, 8]]

sum_of_lists = nested_sum(list_of_lists)
print(sum_of_lists)
