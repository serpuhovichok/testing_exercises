from functions.level_2.one_pr_url import is_github_pull_request_url
import pytest

@pytest.mark.parametrize("data, result", [
                            ('https://github.com/serpuhovichok/typing_challenges/pull/2', True)
                         ])
def test__is_github_pull_request_url__return_true_for_correct_url(data, result):
    assert is_github_pull_request_url(data) is result


@pytest.mark.parametrize("data, result", [
                            ('https://github.com/serpuhovichok/', False)
                         ])
def test__is_github_pull_request_url____return_false_for_username_only_url(data, result):
    assert is_github_pull_request_url(data) is result


@pytest.mark.parametrize("data, result", [
                            ('https://gitlab.com/serpuhovichok/typing_challenges/pull/2', False)
                         ])
def test__is_github_pull_request_url__return_false_for_not_github_url(data, result):
    assert is_github_pull_request_url(data) is result


@pytest.mark.parametrize("data, result", [
                            ('https://github.com/serpuhovichok/typing_challenges/push/2', False)
                         ])
def test__is_github_pull_request_url__return_false_for_not_pull_request(data, result):
    assert is_github_pull_request_url(data) is result

