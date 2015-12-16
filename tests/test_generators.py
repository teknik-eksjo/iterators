import unittest
from exercises.generators import cubes, primes, fibonacci, alphabet, permutations, look_and_say
import json


class GeneratorTests(unittest.TestCase):

    def test_cubes(self):
        c = iter(cubes())
        for i in range(1, 1001):
            value = next(c)
            self.assertEqual(c, i ** 3)

    def test_primes(self):
        with open('tests/data_primes.json') as file:
            data = json.load(file)

        p = iter(primes())
        for prime in data:
            self.assertEqual(next(p), prime)

    def test_fibonacci(self):
        with open('tests/data_fibonacci.json') as file:
            data = json.load(file)

        f = iter(fibonacci())
        for fibonacci in data:
            self.assertEqual(next(f), fibonacci)

    def test_alphabet(self):
        data = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het',
                'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem', 'Nun', 'Samekh', 'Ayin',
                'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']

        a = iter(alphabet())
        for alpha in data:
            self.assertEqual(next(a), alpha)
        self.assertRaises(StopIteration, next, a)

    @unittest.expectedFailure
    def test_permutations(self):
        data = ['abc', 'acb', 'bac', 'cab', 'cba', 'bca']
        result = []
        p = iter(Permutations())
        for i in data:
            result.append(next(p))
        self.assertCountEqual(result, data)
        self.assertRaises(StopIteration, next, p)

    @unittest.expectedFailure
    def test_lookandsay(self):
        pass
