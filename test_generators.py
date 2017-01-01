import unittest

from utils.generators import fib, primes_by_mod, primes_by_seive, head


class TestGenerators(unittest.TestCase):
    def test_fib(self):
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        result = list(fib(1, 1, limit=100))
        self.assertEqual(expected, result)

    def core_test_primes(self, prime_generator):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] # primes < 100
        result = list(prime_generator(limit=100))
        self.assertEqual(expected, result)

        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]  # first 20 primes
        result = list(head(20,prime_generator()))
        self.assertEqual(expected, result)

    def test_primes_by_mod(self):
        self.core_test_primes(primes_by_mod)

    def test_primes_by_seive(self):
        self.core_test_primes(primes_by_seive)


if __name__ == '__main__':
    unittest.main()
