import requests

from rentitout.Constants import CurrencyServiceConstants
from rentitout.exceptions import CurrencyServiceInvalid


class CurrencyService:
    @staticmethod
    def get_currency_rates():
        response = requests.get(
            url=CurrencyServiceConstants.BASE_URL + CurrencyServiceConstants.RATES_API +
                '?access_key=' + CurrencyServiceConstants.ACCESS_KEY
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise CurrencyServiceInvalid()

    @staticmethod
    def convert_currency_rates(base_currency, to_currency, amount):
        response = requests.get(
            url=CurrencyServiceConstants.BASE_URL + CurrencyServiceConstants.CONVERT_API +
                '?access_key=' + CurrencyServiceConstants.ACCESS_KEY +
                f'&from={base_currency}&to={to_currency}&amount={amount}'
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise CurrencyServiceInvalid()
