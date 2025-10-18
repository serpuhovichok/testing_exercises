from functions.level_2.three_first import first
import pytest


@pytest.mark.parametrize("data, result",
                         [([1, 2, 3], 1)]
                         )
def test__first__returns_first_when_items_not_empty(data, result):
    assert first(data) == result


def test__first__items_empty__raise_error_when_default_not_set():
    with pytest.raises(AttributeError):
        result = first([])


@pytest.mark.parametrize("default_value", [None, 15])
def test__first__return_default_value_when_items_empty(default_value):
    assert first(items=[], default=default_value) == default_value
