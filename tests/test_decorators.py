import pytest
from exercises.decorators import memoize, rovarsprak
from mock import Mock


@pytest.mark.skip('Not implemented yet.')
def test_memoize_decorator():
    dummy_fn = Mock(name='dummy_fn')
    dummy_fn.return_value = 'spam'

    wrapped = memoize(dummy_fn)

    # Första anrop ger call count == 1
    assert wrapped(3) == 'spam'
    assert dummy_fn.call_count == 1
    # Andra anrop ger inget ytterligare call - cachen användes!
    assert wrapped(3) == 'spam'
    assert dummy_fn.call_count == 1

    # Nästa anrop ger ökning av call count.
    assert wrapped(7) == 'spam'
    assert dummy_fn.call_count == 2


@pytest.mark.skip('Not implemented yet.')
def test_rovarsprak_decorator():
    @rovarsprak
    def test_fun():
        return 'testord'

    assert test_fun() == 'totesostotorordod'
