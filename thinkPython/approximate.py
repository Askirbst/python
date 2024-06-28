import math

def estimate_pi():
    epsilon = 1e-15
    one_over_pi = 1 / math.pi
    constant = (2 * math.sqrt(2)) / 9801
    approx = 0
    k = 0
    while abs(approx - one_over_pi) > epsilon:
        numerator = (math.factorial(4 * k)) * (1103 + 26390 * k)
        denominator = (math.factorial(k)**4) * (396**(4 * k))

        approx += constant * (numerator / denominator)

        k += 1
    print(f"The approximate value of pi to the 1e-15 decimal place is {1 / approx}")

estimate_pi()