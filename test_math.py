import unittest

from utils.generators import primes_by_mod
from utils.math import factorise_by_trial_division

class TestUtilsMaths(unittest.TestCase):

    def test_factorise_by_trial_division(self):
        result = [factorise_by_trial_division(i, primes_by_mod()) for i in range(0,13)]
        expected = [ {},        # 0
                     {2: 0},    # 1 is a special case, 2**0
                     {2: 1},    # 2
                     {3: 1},    # 3
                     {2: 2},    # 4
                     {5: 1},    # 5
                     {2: 1, 3: 1},  # 6
                     {7: 1},    # 7
                     {2: 3},    # 8
                     {3: 2},    # 9
                     {2: 1, 5: 1},  # 10
                     {11: 1},   # 11
                     {2: 2, 3: 1}
                ]

        self.assertEqual(result, expected)

    def test_factorise_by_trial_division_with_memoisation(self):
        memo = {}

        result = [factorise_by_trial_division(i, primes_by_mod(), memo) for i in range(0,13)]
        expected = [ {},        # 0
                     {2: 0},    # 1 is a special case, 2**0
                     {2: 1},    # 2
                     {3: 1},    # 3
                     {2: 2},    # 4
                     {5: 1},    # 5
                     {2: 1, 3: 1},  # 6
                     {7: 1},    # 7
                     {2: 3},    # 8
                     {3: 2},    # 9
                     {2: 1, 5: 1},  # 10
                     {11: 1},   # 11
                     {2: 2, 3: 1}
                ]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
