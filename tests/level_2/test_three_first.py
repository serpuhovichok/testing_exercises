from functions.level_2.three_first import first
import pytest


def test__first__items_not_empty():
    items = [1, 2, 3]

    result = first(items)

    assert result == 1


def test__first__items_empty__default_not_set():
    items = []

    with pytest.raises(AttributeError):
        result = first(items)


def test__first__items_empty__none_default():
    items = []

    result = first(items, None)

    assert result is None


def test__first__items_empty__int_default():
    items = []

    result = first(items, 15)

    assert result == 15