import pytest
from exercises.iterators import Cubes, Primes, Fibonacci, Alphabet, Permutations, LookAndSay
import json


def test_cubes_is_iterator():
    assert '__init__' in dir(Cubes)
    iterator = iter(Cubes())
    assert '__next__' in dir(iterator)


def test_cubes():
    c = iter(Cubes())
    for i in range(1, 1001):
        assert next(c) == i ** 3


def test_primes_is_iterator():
    assert '__init__' in dir(Primes)
    iterator = iter(Primes())
    assert '__next__' in dir(iterator)


def test_primes():
    with open('tests/data_primes.json') as file:
        data = json.load(file)

    p = iter(Primes())
    for prime in data:
        assert next(p) == prime


def test_fibonnaci_is_iterator(self):
    assert '__init__' in dir(Fibonacci)
    iterator = iter(Fibonacci())
    assert '__next__' in dir(iterator)

def test_fibonacci(self):
    with open('tests/data_fibonacci.json') as file:
        data = json.load(file)

    f = iter(Fibonacci())
    for fibonacci in data:
        assert next(f) == fibonacci


def test_alphabet_is_iterator(self):
    assert '__init__' in dir(Alphabet)
    iterator = iter(Alphabet())
    assert '__next__' in dir(iterator)


def test_alphabet(self):
    data = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het',
            'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem', 'Nun', 'Samekh', 'Ayin',
            'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']

    a = iter(Alphabet())
    for alpha in data:
        assert next(a) == alpha
    with pytest.raises(StopIteration):
        next(a)


def test_permutations_is_iterator(self):
    assert '__init__' in dir(Permutations)
    iterator = iter(Permutations())
    assert '__next__' in dir(iterator)


def test_permutations(self):
    data = ['abc', 'acb', 'bac', 'cab', 'cba', 'bca']
    result = []

    p = iter(Permutations())
    for i in data:
        result.append(next(p))

    assert len(result) == len(data)
    with pytest.raises(StopIteration):
        next(p)


def test_look_and_say_is_iterator():
    assert '__init__' in dir(LookAndSay)
    iterator = iter(LookAndSay())
    assert '__next__' in dir(iterator)


def test_look_and_say():
    with open('tests/data_lookandsay.json') as file:
        data = json.load(file)

    l = iter(LookAndSay())
    for value in data:
        assert next(l) == value
