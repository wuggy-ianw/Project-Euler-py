# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import combinations

def is_palindrome(s):
    midpoint = int((len(s)+1)/2)
    return all(map(lambda x, y: x == y, s[:midpoint+1], s[:-midpoint-1:-1]))

print(max(filter(lambda x: is_palindrome(str(x)), map(lambda x: x[0]*x[1], combinations(range(100, 999), 2)))))
