from functions.level_1.one_gender import genderalize
import pytest


@pytest.mark.parametrize("verb_male, verb_female, gender, result", [
    ('кот', 'кошка', 'male', 'кот'),
    ('кот', 'кошка', 'female', 'кошка'),
])
def test__genderalize__success(verb_male: str,  verb_female: str, gender: str, result: str):
    assert genderalize(verb_male, verb_female, gender) == result
