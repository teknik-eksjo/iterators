import pytest
from exercises.iterators import Cubes, Primes, Fibonacci, Alphabet, Permutations, LookAndSay
import json


@pytest.mark.skip('Not implemented yet.')
def test_cubes_is_iterator():
    assert '__init__' in dir(Cubes)
    iterator = iter(Cubes())
    assert '__next__' in dir(iterator)


@pytest.mark.skip('Not implemented yet.')
def test_cubes():
    c = iter(Cubes())
    for i in range(1, 1001):
        assert next(c) == i ** 3


@pytest.mark.skip('Not implemented yet.')
def test_primes_is_iterator():
    assert '__init__' in dir(Primes)
    iterator = iter(Primes())
    assert '__next__' in dir(iterator)


@pytest.mark.skip('Not implemented yet.')
def test_primes():
    with open('tests/data_primes.json') as file:
        data = json.load(file)

    p = iter(Primes())
    for prime in data:
        assert next(p) == prime


@pytest.mark.skip('Not implemented yet.')
def test_fibonnaci_is_iterator():
    assert '__init__' in dir(Fibonacci)
    iterator = iter(Fibonacci())
    assert '__next__' in dir(iterator)


@pytest.mark.skip('Not implemented yet.')
def test_fibonacci():
    with open('tests/data_fibonacci.json') as file:
        data = json.load(file)

    f = iter(Fibonacci())
    for fibonacci in data:
        assert next(f) == fibonacci


@pytest.mark.skip('Not implemented yet.')
def test_alphabet_is_iterator():
    assert '__init__' in dir(Alphabet)
    iterator = iter(Alphabet())
    assert '__next__' in dir(iterator)


@pytest.mark.skip('Not implemented yet.')
def test_alphabet():
    data = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het',
            'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem', 'Nun', 'Samekh', 'Ayin',
            'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']

    a = iter(Alphabet())
    for alpha in data:
        assert next(a) == alpha
    with pytest.raises(StopIteration):
        next(a)


@pytest.mark.skip('Not implemented yet.')
def test_permutations_is_iterator():
    assert '__init__' in dir(Permutations)
    iterator = iter(Permutations())
    assert '__next__' in dir(iterator)


@pytest.mark.skip('Not implemented yet.')
def test_permutations():
    expected_result = ['abc', 'acb', 'bac', 'cab', 'cba', 'bca']
    result = []

    p = iter(Permutations('abc'))
    while True:
        try:
            result.append(next(p))
        except StopIteration:
            break

    # Check length of result
    assert len(result) == len(expected_result)

    # Check that all result values are in expected_result
    for value in result:
        assert value in expected_result
        expected_result.remove(value)


@pytest.mark.skip('Not implemented yet.')
def test_look_and_say_is_iterator():
    assert '__init__' in dir(LookAndSay)
    iterator = iter(LookAndSay())
    assert '__next__' in dir(iterator)


@pytest.mark.skip('Not implemented yet.')
def test_look_and_say():
    with open('tests/data_lookandsay.json') as file:
        data = json.load(file)

    l = iter(LookAndSay())
    for value in data:
        assert next(l) == value
