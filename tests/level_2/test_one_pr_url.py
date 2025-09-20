from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__success():
    data = 'https://github.com/serpuhovichok/typing_challenges/pull/2'

    result = is_github_pull_request_url(data)

    assert result is True


def test__is_github_pull_request_url__other_seven_parts():
    data = 'https://github.com/serpuhovichok/'

    result = is_github_pull_request_url(data)

    assert result is False


def test__is_github_pull_request_url__not_github_url():
    data = 'https://gitlab.com/serpuhovichok/typing_challenges/pull/2'

    result = is_github_pull_request_url(data)

    assert result is False


def test__is_github_pull_request_url__not_pull_request():
    data = 'https://github.com/serpuhovichok/typing_challenges/push/2'

    result = is_github_pull_request_url(data)

    assert result is False

