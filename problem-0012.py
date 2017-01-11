

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

# An alternative way of producting the triangle numbers is:
# a(n) = (n(n+1))/2 = (n**2 + n)/2

# Generating and then factorising all the triangle numbers is slow
# But we can exploit the fact that 'n' and 'n+1' are coprime, and if we factorise 'n' and 'n+1'

# If we have a number represented num = product( p(k) ** z(k) for k from 1..inf)... where p(k) is the kth prime,
# and z(k) is the exponent for the kth prime, then we can work out the number of factors the number has as
#   n_factors = product(1 + z(k) for k from 1..inf)

# And since 'n' and 'n+1' are coprime, they don't share a factor, so we can just product the n_factors for each
# (That is, 'n(n+1)'



from utils.generators import primes_by_mod, IteratorMemoiser
from utils.math import factorise_by_trial_division, product



memo={}
primes = IteratorMemoiser(primes_by_mod(None))

n = 1
max_nfactors = 0
max_n = 0
while True:
    triangle_number = (n * (n+1)) // 2

    factorisation_n = factorise_by_trial_division(n, iter(primes), memo)
    factorisation_n_plus_1 = factorise_by_trial_division(n + 1, iter(primes), memo)

    # compute the prime factorisation of the triangle number
    factorisation_triangle_number = factorisation_n + factorisation_n_plus_1
    assert factorisation_triangle_number[2] > 0     # n(n+1) should always be even
    factorisation_triangle_number[2] -= 1           # divide by 2

    nfactors = product([1 + x for x in factorisation_triangle_number.values()])

    if nfactors >= 500:
        break

    if nfactors > max_nfactors:
        max_nfactors = nfactors
        max_n = n

    if n % 1000 == 0:
        print(max_n, max_nfactors)

        max_n = 0
        max_nfactors = 0
    n += 1

print(triangle_number, n, nfactors)

