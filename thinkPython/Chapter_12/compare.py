def compare_tuples(t, v):
    if t < v:
        return True
    else:
        return False
    
t = (0, 5, 1)
v = (0, 5, 2)
print(compare_tuples(t,v))