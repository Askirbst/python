def function(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

#print(function(2, 1))

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else: 
        return False
    
#print(is_between(2, 3, 1))

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
#print(c(x, y+3, x+y))

# Ackermann Function

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    
print(ack(3, 4))
