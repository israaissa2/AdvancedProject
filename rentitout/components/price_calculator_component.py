import math
from datetime import datetime

from rentitout.Constants import SECONDS_IN_HOUR, PROFIT_PERCENTAGE


class PriceCalculatorComponent:

    @staticmethod
    def calculate_total_seconds(start_date_time, end_date_time):
        start_dt = datetime.fromisoformat(start_date_time)
        end_dt = datetime.fromisoformat(end_date_time)

        time_diff = end_dt - start_dt
        return time_diff.total_seconds()

    @staticmethod
    def calculate_total_price(start_date_time, end_date_time, price_per_hour):
        total_seconds = PriceCalculatorComponent.calculate_total_seconds(start_date_time, end_date_time)
        price = math.ceil(total_seconds / SECONDS_IN_HOUR) * price_per_hour
        return price * (1 + PROFIT_PERCENTAGE)

