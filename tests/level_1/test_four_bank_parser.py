import datetime
import decimal
import pytest
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
from functions.level_1.four_bank_parser import extract_amount, extract_card_last_digits
from functions.level_1.four_bank_parser import extract_spend_in, extract_spend_at

TEXT_SMS_MESSAGE = SmsMessage(
    text="10.1 something, 12341234 01.01.01 12:34 four four four authcode ",
    author='Somebody',
    sent_at=datetime.datetime.now()
)
TEST_CARD = BankCard(last_digits='1234', owner='Somebody')
TEST_OTHER_CARD = BankCard(last_digits='4321', owner='Somebody Else')
TEST_EXPENSE = Expense(
    amount=decimal.Decimal('10.1'),
    card=TEST_CARD,
    spent_in='four four four',
    spent_at=datetime.datetime.strptime(f'01.01.01 12:34', '%d.%m.%y %H:%M')
)

@pytest.mark.parametrize("sms, cards, result", [
    (TEXT_SMS_MESSAGE, [TEST_CARD, TEST_OTHER_CARD], TEST_EXPENSE)
])
def test_parse_ineco_expense(sms: SmsMessage, cards: list[BankCard], result: Expense):
    assert parse_ineco_expense(sms=sms, cards=cards) == result


@pytest.mark.parametrize("text, result", [
    ('11.2 22.3, text', decimal.Decimal('11.2')),
    ('11.1 22.2 33.3, text', decimal.Decimal('22.2')),
])
def test_extract_amount(text: str, result: decimal.Decimal):
    assert extract_amount(text) == result


@pytest.mark.parametrize("text, result", [
    ("10.1 something, 12341234 two three four four four authcode ", "1234")
])
def test_extract_card_last_digits(text: str, result: str):
    assert extract_card_last_digits(text) == result


@pytest.mark.parametrize("text, result", [
    ("10.1 something, 12341234 two three four four four authcode ", "four four four")
])
def test_extract_spend_in(text: str, result: str):
    assert extract_spend_in(text) == result


@pytest.mark.parametrize("text, result", [
    (
        "10.1 something, 12341234 01.01.01 12:34 four four four authcode ",
        datetime.datetime.strptime(f'01.01.01 12:34', '%d.%m.%y %H:%M')
    )
])
def test_extract_spend_at(text: str, result: str):
    assert extract_spend_at(text) == result
