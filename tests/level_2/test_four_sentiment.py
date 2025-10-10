from functions.level_2.four_sentiment import check_tweet_sentiment
import pytest


GOOD_WORDS = {'радостный', 'счастливый', 'отличный', 'замечательный', 'прекрасный'}
BAD_WORDS = {'грустный', 'плохой', 'ужасный', 'отвратительный', 'злой'}


@pytest.mark.parametrize("text, result",
                         [('Съешь ещё этих мягких французских булок, да выпей же чаю', None)]
                         )
def test__check_tweet_sentiment__result_none_without_good_and_bad_words(text, result):
    assert check_tweet_sentiment(text=text, good_words=GOOD_WORDS, bad_words=BAD_WORDS) == result


@pytest.mark.parametrize("text, result",
                         [('Настроение у неё было отличное, несмотря на отвратительную погоду', None)]
                         )
def test__check_tweet_sentiment__result_none_with_equal_amount_good_and_bad_words(text, result):
    assert check_tweet_sentiment(text=text, good_words=GOOD_WORDS, bad_words=BAD_WORDS) == result


@pytest.mark.parametrize("text, result",
                         [
                             (
                                'Праздник получился просто замечательный, прекрасный и радостный, хотя вначале было немного ужасно',
                                'GOOD'
                             )
                         ]
                        )
def test__check_tweet_sentiment__result_good_with_more_good_words(text, result):
    assert check_tweet_sentiment(text=text, good_words=GOOD_WORDS, bad_words=BAD_WORDS) == result


@pytest.mark.parametrize("text, result",
                         [
                             (
                                'День был ужасный, отвратительный и грустный, хотя начался с отличного настроения',
                                'BAD'
                             )
                         ]
                        )
def test__check_tweet_sentiment__result_bad_with_more_bad_words(text, result):
    assert check_tweet_sentiment(text=text, good_words=GOOD_WORDS, bad_words=BAD_WORDS) == result

