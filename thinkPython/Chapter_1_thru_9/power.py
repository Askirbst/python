def is_power(a, b):
    while a > b:
        if not is_power(a / b, b):
            return False
        else:
            return True
        
    if a % b == 0:
        return True
    else:
        return False
        
print(is_power(177148, 3))