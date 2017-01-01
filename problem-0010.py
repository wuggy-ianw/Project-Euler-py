# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from utils.generators import primes_by_seive

print(sum(primes_by_seive(2000000)))
