from math import gcd
from itertools import combinations

def count_pairs_with_gcd_greater_than_1(lst):
    count = 0
    for a, b in combinations(lst, 2):
        if gcd(a, b) > 1:
            count += 1
    return count

lst = [97, 12, 101, 76, 25, 48, 86, 52, 35, 60]
print(count_pairs_with_gcd_greater_than_1(lst))

