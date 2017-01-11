import unittest

from utils.generators import fib, primes_by_mod, primes_by_seive, numbers_by_prime_factors, head


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

    def test_numbers_by_prime_factors(self):
        expected = [(1, [2], [0]),
                    (2, [2], [1]),
                    (3, [2, 3], [0, 1]),
                    (4, [2], [2]),
                    (5, [2, 3, 5], [0, 0, 1]),
                    (6, [2, 3], [1, 1]),
                    (7, [2, 3, 5, 7], [0, 0, 0, 1]),
                    (8, [2], [3]),
                    (9, [2, 3], [0, 2]),
                    (10, [2, 3, 5], [1, 0, 1]),
                    (11, [2, 3, 5, 7, 11], [0, 0, 0, 0, 1]),
                    (12, [2, 3], [2, 1]),
                    (13, [2, 3, 5, 7, 11, 13], [0, 0, 0, 0, 0, 1]),
                    (14, [2, 3, 5, 7], [1, 0, 0, 1]),
                    (15, [2, 3, 5], [0, 1, 1]),
                    (16, [2], [4]),
                    (17, [2, 3, 5, 7, 11, 13, 17], [0, 0, 0, 0, 0, 0, 1]),
                    (18, [2, 3], [1, 2]),
                    (19, [2, 3, 5, 7, 11, 13, 17, 19], [0, 0, 0, 0, 0, 0, 0, 1])]
        result = list(numbers_by_prime_factors(20))
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
