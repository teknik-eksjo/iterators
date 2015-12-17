import unittest
from exercises.generators import cubes, primes, fibonacci, alphabet, permutations, look_and_say
import json


class CubesGeneratorTests(unittest.TestCase):

    def test_is_generator(self):
        gen = cubes()
        self.assertIn('__init__', dir(gen))
        self.assertIn('__next__', dir(gen))

    def test_cubes(self):
        c = iter(cubes())
        for i in range(1, 1001):
            value = next(c)
            self.assertEqual(c, i ** 3)


class PrimesGeneratorTests(unittest.TestCase):

    def test_is_generator(self):
        gen = primes()
        self.assertIn('__init__', dir(gen))
        self.assertIn('__next__', dir(gen))

    def test_primes(self):
        with open('tests/data_primes.json') as file:
            data = json.load(file)

        p = iter(primes())
        for prime in data:
            self.assertEqual(next(p), prime)


class FibanacciGeneratorTests(unittest.TestCase):

    def test_is_generator(self):
        gen = fibonacci()
        self.assertIn('__init__', dir(gen))
        self.assertIn('__next__', dir(gen))

    def test_fibonacci(self):
        with open('tests/data_fibonacci.json') as file:
            data = json.load(file)

        f = iter(fibonacci())
        for fibonacci in data:
            self.assertEqual(next(f), fibonacci)


class AlphabetGeneratorTests(unittest.TestCase):

    def test_is_generator(self):
        gen = alphabet()
        self.assertIn('__init__', dir(gen))
        self.assertIn('__next__', dir(gen))

    def test_alphabet(self):
        data = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het',
                'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem', 'Nun', 'Samekh', 'Ayin',
                'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']

        a = iter(alphabet())
        for alpha in data:
            self.assertEqual(next(a), alpha)
        self.assertRaises(StopIteration, next, a)


class PermutationsGeneratorTests(unittest.TestCase):

    def test_is_generator(self):
        gen = permutations()
        self.assertIn('__init__', dir(gen))
        self.assertIn('__next__', dir(gen))

    def test_permutations(self):
        data = ['abc', 'acb', 'bac', 'cab', 'cba', 'bca']
        result = []
        p = iter(Permutations())
        for i in data:
            result.append(next(p))
        self.assertCountEqual(result, data)
        self.assertRaises(StopIteration, next, p)


class LookAndSayGeneratorTests(unittest.TestCase):

    def test_is_generator(self):
        gen = look_and_say()
        self.assertIn('__init__', dir(gen))
        self.assertIn('__next__', dir(gen))

    def test_lookandsay(self):
        with open('tests/data_lookandsay.json') as file:
            data = json.load(file)

        l = iter(LookAndSay())
        for value in data:
            self.assertEqual(next(l), value)
