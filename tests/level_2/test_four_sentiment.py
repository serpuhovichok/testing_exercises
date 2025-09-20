from functions.level_2.four_sentiment import check_tweet_sentiment


GOOD_WORDS = {'радостный', 'счастливый', 'отличный', 'замечательный', 'прекрасный'}
BAD_WORDS = {'грустный', 'плохой', 'ужасный', 'отвратительный', 'злой'}


def test__check_tweet_sentiment__without_good_and_bad_words():
    text = 'Съешь ещё этих мягких французских булок, да выпей же чаю'

    result = check_tweet_sentiment(text=text, good_words=GOOD_WORDS, bad_words=BAD_WORDS)

    assert result is None


def test__check_tweet_sentiment__with_equal_amount_good_and_bad_words():
    text = 'Настроение у неё было отличное, несмотря на отвратительную погоду'

    result = check_tweet_sentiment(text=text, good_words=GOOD_WORDS, bad_words=BAD_WORDS)

    assert result is None


def test__check_tweet_sentiment__with_more_good_words():
    text = 'Праздник получился просто замечательный, прекрасный и радостный, хотя вначале было немного ужасно'

    result = check_tweet_sentiment(text=text, good_words=GOOD_WORDS, bad_words=BAD_WORDS)

    assert result == 'GOOD'


def test__check_tweet_sentiment__with_more_bad_words():
    text = 'День был ужасный, отвратительный и грустный, хотя начался с отличного настроения'

    result = check_tweet_sentiment(text=text, good_words=GOOD_WORDS, bad_words=BAD_WORDS)

    assert result == 'BAD'

