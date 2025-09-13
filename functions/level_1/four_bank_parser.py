import datetime
import decimal
from typing import NamedTuple


class BankCard(NamedTuple):
    last_digits: str
    owner: str


class SmsMessage(NamedTuple):
    text: str
    author: str
    sent_at: datetime.datetime


class Expense(NamedTuple):
    amount: decimal.Decimal
    card: BankCard
    spent_in: str
    spent_at: datetime.datetime


def extract_amount(text: str) -> decimal.Decimal:
    result, _ = text.split(', ')
    result = result.split(' ')
    result = result[-2]
    return decimal.Decimal(result)


def extract_card_last_digits(text: str) -> str:
    _, raw_details = text.split(', ')
    raw_details = raw_details.split(' authcode ')[0]
    raw_card, _, _, _ = raw_details.split(' ', maxsplit=3)
    return raw_card[-4:]


def extract_spend_in(text: str) -> str:
    _, raw_details = text.split(', ')
    raw_details = raw_details.split(' authcode ')[0]
    _, _, _, spend_in = raw_details.split(' ', maxsplit=3)
    return spend_in


def extract_spend_at(text: str) -> datetime:
    _, raw_details = text.split(', ')
    raw_details = raw_details.split(' authcode ')[0]
    _, raw_date, raw_time, _ = raw_details.split(' ', maxsplit=3)
    return datetime.datetime.strptime(f'{raw_date} {raw_time}', '%d.%m.%y %H:%M')


def parse_ineco_expense(sms: SmsMessage, cards: list[BankCard]) -> Expense:
    """
        По-хорошему, здесь должна быть проверка на корректность текста в sms.
        Сейчас предполагается, что текст всегда корректный приходит.
    """
    return Expense(
        amount=extract_amount(sms.text),
        card=[c for c in cards if c.last_digits == extract_card_last_digits(sms.text)][0],
        spent_in=extract_spend_in(sms.text),
        spent_at=extract_spend_at(sms.text),
    )


