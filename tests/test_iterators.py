import unittest
from exercises.iterators import Cubes, Primes, Fibonacci, Alphabet, Permutations, LookAndSay


class IteratorTests(unittest.TestCase):

    def test_cubes(self):
        c = iter(Cubes())
        for i in range(1, 1001):
            value = next(c)
            self.assertEqual(c, i ** 3)

    def test_primes(self):
        from primes import primes
        p = iter(Primes())
        for prime in primes:
            self.assertEqual(p, prime)
