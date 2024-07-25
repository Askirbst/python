def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    
print(ack(3, 4))

cache = {}
def memo_ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return memo_ack(m - 1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = memo_ack(m - 1, memo_ack(m, n - 1))
        return cache[m, n]
        
    
print(memo_ack(3, 4))