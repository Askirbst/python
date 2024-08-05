import math
def mysqrt(a):
    x = a / 2
    epsilon = .0000001
    while True:
        y = (x + (a / x)) / 2
        if abs(y - x) < epsilon:
            return y
        x = y

def test_square_root():
    print("a   mysqrt(a)         math.sqrt(a)      diff\n-   ---------         ------------      ----")
    a = 1
    while a <= 9:
        mysqare = mysqrt(a)
        yoursquare = math.sqrt(a)
        if len(str(mysqare)) < 13:
            print(f"{a}")
        else:
            print(f"{a}   {str(mysqare)[:13]}     {str(yoursquare)[:13]}  {str(abs(mysqare - yoursquare))[:13]}")
        a += 1

test_square_root()