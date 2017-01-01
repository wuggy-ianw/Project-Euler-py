

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

from utils.generators import primes_by_mod, last, head

print(last(head(10001, primes_by_mod())))

