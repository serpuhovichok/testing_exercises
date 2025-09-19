import datetime
import decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, parse_ineco_expense
import pytest


def test__parse_ineco_expense__extracts_correct_amount():
    result = parse_ineco_expense(
        sms=SmsMessage(
            text="10.1 something, 12341234 01.01.01 12:34 four four four authcode ",
            author='Somebody',
            sent_at=datetime.datetime.now()
        ),
        cards=[
            BankCard(last_digits='1234', owner='Somebody'),
            BankCard(last_digits='4321', owner='Somebody Else')
        ]
    )

    assert result.amount == decimal.Decimal('10.1')


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


def test__parse_ineco_expense__success():
    result = parse_ineco_expense(
        sms=SmsMessage(
            text="10.1 something, 12341234 01.01.01 12:34 four four four authcode ",
            author='Somebody',
            sent_at=datetime.datetime.now()
        ),
        cards=[
            BankCard(last_digits='1234', owner='Somebody'),
            BankCard(last_digits='4321', owner='Somebody Else')
        ]
    )

    assert result.amount == decimal.Decimal('10.1')
    assert result.card == BankCard(last_digits='1234', owner='Somebody')
    assert result.spent_in == 'four four four'
    assert result.spent_at == datetime.datetime.strptime(f'01.01.01 12:34', '%d.%m.%y %H:%M')

