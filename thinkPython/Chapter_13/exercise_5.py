from fractions import Fraction
import random

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

t = ['a', 'b', 'c' ,'c', 'b', 'b']
d = histogram(t)

# Add the values of each key and get the probabilty each key will be called
def choose_from_hist(dict : dict):
    total_val = 0
    probability_dict = {}
    for key in dict:
        total_val += dict[key]
    for key, val in dict.items():
        probability_dict[key] = str(Fraction(val/total_val).limit_denominator())
    
    choice = random.choice(t)

    return f'{choice} with probability {probability_dict[choice]}'

print(choose_from_hist(d))