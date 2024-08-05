t = ['a', 'b', 'c', 'd', 'e', 'f']
x = '1'
print(t)

t.append(x)
print(t)

t = t + [x]
print(t)

t += [x]
print(t)

del t[6:]
print(t)

#WRONG this adds a list containing x to the end of list t
t.append([x])
print(t)

#WRONG append() returns None
#t = t.append(x)
#print(t)

#WRONG creates a new list by adding a list containing x to the end of list t but no new variable was created to get the value returned 
t + [x]
print(t)

#WRONG can only concatenate list (not "str") to list
#t = t + x
#print(t)

t = [3, 1, 2]
t2 = t[:]
t2.sort()
print(t)
print(t2)