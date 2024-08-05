def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

num1 = int(input("Enter a number greater than two: "))
num2 = int(input("Enter another number greater than two and less than your previous entry: "))

print(f"The greatest common divisor of {num1} and {num2} is {gcd(num1, num2)}")