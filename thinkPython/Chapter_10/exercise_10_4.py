'''

Write a function called chop that takes a list, 
modifies it by removing the first and last elements,
and returns None

'''

def chop(t):
    del t[0]
    del t[-1]

lis = [1, 2, 3, 4, 5, 6]

chop(lis)

print(lis)