# generators for common things
from collections import deque
import numpy as np

def fib(a, b, limit):
    """
    Iteratively produce the Fibonacci sequence starting with first two number.

    :param a: The first number of the sequence.
    :param b: The second number of the sequence.
    :param limit: Stop once we've generated all the terms of the sequence less than this limit.
    :return:
    """
    while a<limit:
        yield a
        a,b = b, a+b



def primes_by_mod(limit=1000000):
    """
    Produce primes by checking all previously known primes by modulus. This is quite slow, but
    is rather simple.

    :param limit: Stop once we've generated all the primes less than this limit. None means no limit
                  and would make an infinite iterator. The default is 1 million.
    :return: primes in order
    """
    if (limit is None or 2 < limit):
        yield 2

    h=set()
    k = 3
    while limit is None or k < limit:
        if all(map(lambda x: k % x != 0, h)):
            h.add(k)
            yield k
        k += 2


def primes_by_seive(limit=1000000):
    """
    Produce primes by running a primitive seive (of Eratosthenes)
    :param limit: top once we've generated all the primes less than this limit. There MUST be a limit
                  since it bounds the seive. The default is 1 million.
    :return: primes in order
    """
    # treat 2 as a special case
    sieve = np.zeros(limit, dtype=bool)  # defaults to False, meaning 'not a multiple'

    if 2<limit:
        sieve[2*2::2] = True
        yield 2

    k = 3
    while k<limit:
        if sieve[k] == False:
            # this value is prime, fill in all it's multiples
            sieve[2*k::k] = True
            yield k
        k += 2


def last(iter):
    """
    Get the last value produced by an iterator. May run forever if the iterator doesn't terminate!
    """
    x = None
    for x in iter:
        pass
    return x

def first(iter):
    """
    Get the first value produced by an iterator.
    """
    x = None
    for x in iter:
        return x
    return x


def head(n, iter):
    """
    Get the first 'n' items from an iterator (as an iterator)
    """
    for i, k in zip(range(n), iter):
        yield k

def tail(n, iter):
    """
    Get the last 'n' items from an iterator (as an iterator). May run forever if the iterator doesn't terminate!
    """
    yield from deque(iter, n)

