import pytest
from exercises.generators import cubes, primes, fibonacci, alphabet, permutations, look_and_say
import json


def test_generator_is_iterable():
    gen = cubes()
    assert '__init__' in dir(gen)
    assert '__next__' in dir(gen)


def test_cubes():
    c = iter(cubes())
    for i in range(1, 1001):
        value = next(c)
        assert c == i ** 3


def test_primes_is_iterable():
    gen = primes()
    assert '__init__' in dir(gen)
    assert '__next__' in dir(gen)


def test_primes():
    with open('tests/data_primes.json') as file:
        data = json.load(file)

    p = iter(primes())
    for prime in data:
        assert next(p) == prime


def test_fibonacci_is_iterable():
    gen = fibonacci()
    assert '__init__' in dir(gen)
    assert '__next__' in dir(gen)


def test_fibonacci(self):
    with open('tests/data_fibonacci.json') as file:
        data = json.load(file)

    f = iter(fibonacci())
    for fibonacci in data:
        assert next(f) == fibonacci


def test_alphabet_is_iterable():
    gen = alphabet()
    assert '__init__' in dir(gen)
    assert '__next__' in dir(gen)


def test_alphabet():
    data = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het',
            'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem', 'Nun', 'Samekh', 'Ayin',
            'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']

    a = iter(alphabet())
    for alpha in data:
        assert next(a) == alpha
    with pytest.raises(StopIteration):
        next(a)


def test_is_generator_iterable():
    gen = permutations()
    assert '__init__' in dir(gen)
    assert '__next__' in dir(gen)


def test_permutations():
    data = ['abc', 'acb', 'bac', 'cab', 'cba', 'bca']
    result = []
    p = iter(Permutations())
    for i in data:
        result.append(next(p))
    assert len(result) == len(data)
    with pytest.raises(StopIteration):
        next(p)


def test_look_and_say_is_iterable():
    gen = look_and_say()
    assert '__init__' in dir(gen)
    assert '__next__' in dir(gen)


def test_look_and_say():
    with open('tests/data_lookandsay.json') as file:
        data = json.load(file)

    l = iter(LookAndSay())
    for value in data:
        assert next(l) == value
