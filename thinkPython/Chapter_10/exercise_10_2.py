"""

Write a function called cumsum that takes a list of numbers and returns the cumulative sum; 
that is, a new list where the ith element is the sum of the first i+1 elements from the original list

"""

def cumsum(lis):
    cum_sum = 0
    new_lis = []
    for i in lis:
        cum_sum = cum_sum + i
        new_lis.append(cum_sum)
    return new_lis

list_of_ints = [1, 2, 3, 4, 5, 6]
cum_sum_of_list = cumsum(list_of_ints)
print(cum_sum_of_list)