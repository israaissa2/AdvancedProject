from rentitout.components.interval_intersection_component import IntervalIntersectionComponent
from rentitout.components.price_calculator_component import PriceCalculatorComponent
from rentitout.exceptions import ReservationTimeAlreadyReserved, ItemDoesNotExist
from rentitout.repositories.item_repository import ItemRepository, ItemReservationRepository


class ItemComponent:

    @staticmethod
    def get_user_items(user_id):
        return ItemRepository.get_user_items(user_id)

    @staticmethod
    def get_items(user_id):
        return ItemRepository.get_items(user_id)

    @staticmethod
    def add_item(user_id, item_name, item_description, item_price):
        return ItemRepository.add_item(user_id, item_name, item_price, item_description)

    @staticmethod
    def update_item(user_id, item_id, item_name, item_description, item_price):
        return ItemRepository.update_item(user_id, item_id, item_name, item_price, item_description)

    @staticmethod
    def delete_item(user_id, item_id):
        return ItemRepository.delete_item(user_id, item_id)


class ItemReservationComponent:
    @staticmethod
    def get_reservation_items(user_id):
        return ItemReservationRepository.get_user_reservations(user_id)

    @staticmethod
    def get_reservations(item_id):
        return ItemReservationRepository.get_reservations(item_id)

    @staticmethod
    def add_reservation(item_id, user_id, start_time, end_time):
        item = ItemRepository.get_item_by_id(item_id)
        if IntervalIntersectionComponent.check_reservation_intersection(
            start_date_time=start_time, end_date_time=end_time,
            reservations=ItemReservationRepository.get_reservations(item_id)
        ):
            raise ReservationTimeAlreadyReserved()
        if item:
            return ItemReservationRepository.reserve_item(
                item_id=item_id, user_id=user_id, start_time=start_time, end_time=end_time,
                total_price=PriceCalculatorComponent.calculate_total_price(
                    start_date_time=start_time, end_date_time=end_time, price_per_hour=item.price
                )
            )
        else:
            raise ItemDoesNotExist()

    @staticmethod
    def update_reservation(item_reservation_id, item_id, user_id, start_time, end_time):
        item = ItemRepository.get_item_by_id(item_id)
        if IntervalIntersectionComponent.check_reservation_intersection(
            start_date_time=start_time, end_date_time=end_time,
            reservations=ItemReservationRepository.get_reservations(item_id),
            reservation_id=item_reservation_id
        ):
            raise ReservationTimeAlreadyReserved()
        if item:
            return ItemReservationRepository.update_reservation(
                item_id=item_id, user_id=user_id, start_time=start_time, end_time=end_time,
                item_reservation_id=item_reservation_id, total_price=PriceCalculatorComponent.calculate_total_price(
                    start_date_time=start_time, end_date_time=end_time, price_per_hour=item.price
                )
            )
        else:
            raise ItemDoesNotExist()

    @staticmethod
    def delete_reservation(reservation_id, item_id, user_id):
        return ItemReservationRepository.delete_reservation(
            item_id=item_id, reservation_id=reservation_id, user_id=user_id,
        )
