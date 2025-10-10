from functions.level_2.five_replace_word import replace_word
import pytest


@pytest.mark.parametrize("text, replace_from, replace_to, result",
                         [
                             (
                                'Съешь ещё этих мягких французских булок, да выпей же чаю',
                                'собака',
                                'кошка',
                                'Съешь ещё этих мягких французских булок, да выпей же чаю',
                             )
                         ]
                        )
def test__replace_word__without_matches_does_not_change_text(text, replace_from, replace_to, result):
    assert replace_word(text=text, replace_from=replace_from, replace_to=replace_to) == result


@pytest.mark.parametrize("text, replace_from, replace_to, result",
                         [
                             (
                                'The quick brown fox jumps over the lazy dog',
                                'dog',
                                'cat',
                                'The quick brown fox jumps over the lazy cat',
                             )
                         ]
                        )
def test__replace_word__with_matches_replaces_word(text, replace_from, replace_to, result):
    assert replace_word(text=text, replace_from=replace_from, replace_to=replace_to) == result