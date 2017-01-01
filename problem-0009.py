# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from itertools import combinations
from utils.generators import first

def pythagorean_triplets(length_limit):
    """
    Produces integer triplets a,b,c such that a < b < c and a**2 + b**2 = c**2. Triplets are generated
    based on Euclid's formula. See https://en.wikipedia.org/wiki/Pythagorean_triple#A_variant

    :param length_limit: the maximum length of a and b to search up to
    :return: iterator of tuples (a,b,c) in some arbitrary order
    """
    for n, m in combinations(range(1, length_limit, 2), 2):
        assert m > n

        a, b, c = m*n, int((m**2 - n**2)/2), int((m**2 + n**2)/2)
        if a > b:   # ensure ordering of a < b < c
            a, b = b, a

        assert a < b < c
        yield a, b, c

a, b, c = first(filter(lambda x: sum(x) == 1000, pythagorean_triplets(1000)))
print(a, b, c, a*b*c)
