import unittest
from exercises.iterators import Cubes, Primes, Fibonacci, Alphabet, Permutations, LookAndSay
import json


class CubesIteratorTests(unittest.TestCase):

    def test_is_iterator(self):
        self.assertIn('__init__', dir(Cubes))
        iterator = iter(Cubes())
        self.assertIn('__next__', dir(iterator))

    def test_cubes(self):
        c = iter(Cubes())
        for i in range(1, 1001):
            with self.subTest(i = i):
                self.assertEqual(next(c), i ** 3)


class PrimesIteratorTests(unittest.TestCase):

    def test_is_iterator(self):
        self.assertIn('__init__', dir(Primes))
        iterator = iter(Primes())
        self.assertIn('__next__', dir(iterator))

    def test_primes(self):
        with open('tests/data_primes.json') as file:
            data = json.load(file)

        p = iter(Primes())
        for prime in data:
            with self.subTest(prime = prime):
                self.assertEqual(next(p), prime)


class FibonacciIteratorTests(unittest.TestCase):

    def test_is_iterator(self):
        self.assertIn('__init__', dir(Fibonacci))
        iterator = iter(Fibonacci())
        self.assertIn('__next__', dir(iterator))

    def test_fibonacci(self):
        with open('tests/data_fibonacci.json') as file:
            data = json.load(file)

        f = iter(Fibonacci())
        for fibonacci in data:
            with self.subTest(fibonacci = fibonacci):
                self.assertEqual(next(f), fibonacci)


class AlphabetIteratorTests(unittest.TestCase):

    def test_is_iterator(self):
        self.assertIn('__init__', dir(Alphabet))
        iterator = iter(Alphabet())
        self.assertIn('__next__', dir(iterator))

    def test_alphabet(self):
        data = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het',
                'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem', 'Nun', 'Samekh', 'Ayin',
                'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']

        a = iter(Alphabet())
        for alpha in data:
            with self.subTest(alpha = alpha):
                self.assertEqual(next(a), alpha)
        self.assertRaises(StopIteration, next, a)


class PermutationsIteratorTests(unittest.TestCase):

    def test_is_iterator(self):
        self.assertIn('__init__', dir(Permutations))
        iterator = iter(Permutations())
        self.assertIn('__next__', dir(iterator))

    def test_permutations(self):
        data = ['abc', 'acb', 'bac', 'cab', 'cba', 'bca']
        result = []
        p = iter(Permutations())
        for i in data:
            result.append(next(p))
        self.assertCountEqual(result, data)
        self.assertRaises(StopIteration, next, p)


class LookAndSayIteratorTests(unittest.TestCase):

    def test_is_iterator(self):
        self.assertIn('__init__', dir(LookAndSay))
        iterator = iter(LookAndSay())
        self.assertIn('__next__', dir(iterator))

    def test_lookandsay(self):
        with open('tests/data_lookandsay.json') as file:
            data = json.load(file)

        l = iter(LookAndSay())
        for value in data:
            self.assertEqual(next(l), value)
