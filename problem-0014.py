# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

from utils.generators import first

import operator

def update_collatz_chain(n, chain):
    # if we already know the length for n, just return it
    if n in chain:
        return chain[n]

    # otherwise, set the value in chain based on a recursive call!
    if (n % 2) == 0:
        next_n = n//2
    else:
        next_n = 3*n + 1

    chain[n] = update_collatz_chain(next_n, chain) + 1
    return chain[n]

collatz_chain = { 1: 1 }       # start with the end-state as a chain of length 1
for i in range(1, 1000000):
    update_collatz_chain(i, collatz_chain)

print(first(max(collatz_chain.items(), key=operator.itemgetter(1))))
