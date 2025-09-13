from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest

TODAY = datetime.date.today()
TOMORROW = datetime.date.today() + datetime.timedelta(days=1)


@pytest.mark.parametrize("date_str, time_str, given_date", [
    ('', '12:34', TODAY),
    ('tomorrow', '12:34', TOMORROW),
])
def test_compose_datetime_from_today(date_str: str, time_str: str, given_date: datetime.date):
    result = compose_datetime_from(date_str=date_str, time_str=time_str)
    assert result.year == given_date.year
    assert result.month == given_date.month
    assert result.day == given_date.day
    assert result.hour == 12
    assert result.minute == 34
