from functions.level_1.five_title import change_copy_item
import pytest


@pytest.mark.parametrize("title, max_len, result", [
    ('title', 10, 'title'),
    ('title', 100, 'Copy of title'),
    ('Copy of abc(123)def', 100, 'Copy of (124)'),
    ('Copy of abc(test)def', 100, 'Copy of abc(test)def (2)'),
])
def test_change_copy_item(title: str, max_len: int, result: str):
    assert change_copy_item(title=title, max_main_item_title_length=max_len) == result

