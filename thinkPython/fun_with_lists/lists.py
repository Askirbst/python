import random
t = [1, 2, 3, 4, 5, 6]
print(t)
print(t[1:])
print(t[1:1])
print(t[1:2])
t[1:3] = 'a'
print(t)
print(t*2)

g = [3, 5, 9, 1, 18]
g.sort()
print(g)

p = []
for i in range(1000):
    p.append(random.randint(1, 1000))
print(p)
p.sort()
print(p)