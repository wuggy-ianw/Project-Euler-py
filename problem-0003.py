# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

from utils.generators import primes_by_mod, last


def prime_factors(k, prime_generator=primes_by_mod):
    primes = prime_generator(sqrt(k))
    for p in primes:
        # divide the prime into k (and get the remainder)
        d, r = divmod(k, p)
        if r==0:
            # p is a factor, but it might divide multiple times...
            while r==0:
                k = d
                d, r = divmod(d, p)
            yield p     # p is a factor of k

        if k == 1:
            return

    assert False, "Ran out of prime factors?!"


print(last(prime_factors(600851475143)))
