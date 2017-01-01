

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
