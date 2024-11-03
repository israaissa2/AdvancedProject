import os

SECONDS_IN_HOUR = 3600
PROFIT_PERCENTAGE = 0.30


class CurrencyServiceConstants:
    BASE_URL = 'https://api.exchangeratesapi.io/v1/'
    RATES_API = 'latest'
    CONVERT_API = 'convert'
    ACCESS_KEY = os.getenv('ACCESS_KEY')