from pycbrf.toolbox import ExchangeRates
import datetime


def get_currency():
    today = datetime.date.today()
    rates = ExchangeRates(today)
    result = f'Курс Доллара на сегодня: {rates["USD"].value} \n' \
             f'Курс Евро на сегодня: {rates["EUR"].value}'
    return result

