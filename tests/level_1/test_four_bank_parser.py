import datetime
import decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, parse_ineco_expense
import pytest


@pytest.mark.parametrize("text, amount", [
    ("10.1 something, 12341234 01.01.01 12:34 four four four authcode ", decimal.Decimal('10.1'))
])
def test__parse_ineco_expense__extracts_correct_amount(text, amount):
    result = parse_ineco_expense(
        sms=SmsMessage(
            text=text,
            author='Somebody',
            sent_at=datetime.datetime.now()
        ),
        cards=[
            BankCard(last_digits='1234', owner='Somebody'),
            BankCard(last_digits='4321', owner='Somebody Else')
        ]
    )

    assert result.amount == amount


@pytest.mark.parametrize("amount", [
    '10,1', '20,1'
])
def test__parse_ineco_expense__raise_error_when_amount_has_comma_in_separator(amount):
    with pytest.raises(Exception):
        parse_ineco_expense(
            sms=SmsMessage(
                text=f"{amount} something, 12341234 01.01.01 12:34 four four four authcode ",
                author='Somebody',
                sent_at=datetime.datetime.now()
            ),
            cards=[
                BankCard(last_digits='1234', owner='Somebody'),
                BankCard(last_digits='4321', owner='Somebody Else')
            ]
        )


@pytest.mark.parametrize("text, author, cards, amount, spent_in, spent_at", [
    (
        "10.1 something, 12341234 01.01.01 12:34 four four four authcode ",
        'Somebody',
        [
            BankCard(last_digits='1234', owner='Somebody'),
            BankCard(last_digits='4321', owner='Somebody Else')
        ],
        decimal.Decimal('10.1'),
        'four four four',
        datetime.datetime.strptime(f'01.01.01 12:34', '%d.%m.%y %H:%M')
    ),
])
def test__parse_ineco_expense__success(text, author, cards, amount, spent_in, spent_at):
    result = parse_ineco_expense(
        sms=SmsMessage(
            text=text,
            author=author,
            sent_at=datetime.datetime.now()
        ),
        cards=cards
    )

    assert result.amount == amount
    assert result.card == cards[0]
    assert result.spent_in == spent_in
    assert result.spent_at == spent_at

