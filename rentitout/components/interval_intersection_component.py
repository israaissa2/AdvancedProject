from datetime import datetime
import pytz
utc=pytz.UTC


class IntervalIntersectionComponent:
    @staticmethod
    def check_reservation_intersection(start_date_time, end_date_time, reservations, reservation_id=None):
        start_dt = datetime.fromisoformat(start_date_time)
        end_dt = datetime.fromisoformat(end_date_time)

        for reservation in reservations:
            if (
                reservation_id is not None and
                reservation_id == reservation.id
            ):
                continue

            if (
                IntervalIntersectionComponent.in_between(
                    reservation.start_date_time, reservation.end_date_time, start_dt
                ) or
                IntervalIntersectionComponent.in_between(
                    reservation.start_date_time, reservation.end_date_time, end_dt
                )
            ):
                return True
        return False

    @staticmethod
    def in_between(reservation_start_date_time, reservation_end_date_time, date_time):
        return reservation_start_date_time <= utc.localize(date_time) <= reservation_end_date_time

