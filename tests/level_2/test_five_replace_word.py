from functions.level_2.five_replace_word import replace_word


def test__replace_word__without_matches():
    text = 'Съешь ещё этих мягких французских булок, да выпей же чаю'
    replace_from = 'собака'
    replace_to = 'кошка'

    result = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)

    assert result == text


def test__replace_word__with_matches():
    text = 'The quick brown fox jumps over the lazy dog'
    replace_from = 'dog'
    replace_to = 'cat'

    result = replace_word(text=text, replace_from=replace_from, replace_to=replace_to)

    assert result == 'The quick brown fox jumps over the lazy cat'