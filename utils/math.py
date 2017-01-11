import collections

def product(l):
    """
    Compute the product of an iterable
    :param l: an iterable
    :return: product of the members of the iterable (or 1 if empty)
    """
    x = 1
    for i in l:
        x *= i
    return x

def gcd(a,b):
    """
    Compute the greatest common divisor of a pair of numbers.

    :param a: integer
    :param b: integer
    :return: the gcd of a and b
    """
    while b:
        a, b = b, a % b
    return a


def lcm(nums):
    """
    Compute the lowest common multiple of a list of numbers

    :param nums: an iterable of integers
    :return: the lcm of nums
    """
    l = next(nums)
    assert l > 0, "Can't generate the lcm of values less than 1"

    for i in nums:
        assert i > 0, "Can't generate the lcm of values less than 1"
        l = (l * i) / gcd(l, i)
    return int(l)     # the division converts this to float, but it will always be an integer


def factorise_by_trial_division(n, primes, memo=None):
    """
    Dumb as rocks prime factoristion. This is very slow.

    :param n: integer to factorise
    :param primes: an iterable of primes, at least up to x
    :return: a dictionary of {p: e} where p are primes that are factors, and e is the exponent for that prime
    """

    result = collections.Counter()
    prime = next(primes)       # start with the first prime
    x = n

    # handle special cases for n
    if n == 0:
        return result

    if n == 1:
        result[prime] = 0
        return result

    try:
        while True:
            if x == 1:              # we've finished factorising
                break

            assert x >= prime

            if memo is not None and x in memo:  # if we've already computed a result
                result += memo[x]
                x = 1
                break

            # try dividing by this prime
            div, rem = divmod(x, prime)

            # if this divides evenly, increment the count for this prime
            if rem == 0:
                result[prime] += 1
                x = div
            else:
                # move onto the next prime
                prime = next(primes)
    except StopIteration:
        assert False, "Ran out of primes?"

    assert x == 1       # ran out of primes?

    if memo is not None:
        memo[n] = result

    return result
