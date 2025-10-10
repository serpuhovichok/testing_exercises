from functions.level_1.three_url_builder import build_url
from typing import Mapping
import pytest


@pytest.mark.parametrize(
    'host_name, relative_url, get_params, result',
    [
        ('ya.ru', 'search', None, 'ya.ru/search'),
        ('ya.ru', 'search', {1: 'a', 2: 'b'}, 'ya.ru/search?1=a&2=b'),
        ('ya.ru', 'search', {3: 'c'}, 'ya.ru/search?3=c'),
    ]
)
def test_build_url(host_name: str, relative_url: str, get_params: Mapping[str, str], result: str):
    assert build_url(host_name=host_name, relative_url=relative_url, get_params=get_params) == result
