from rentitout.model.item import Item, ItemReservation


class ItemRepository:

    @staticmethod
    def get_user_items(user_id):
        return Item.objects.filter(user_id=user_id).all()

    @staticmethod
    def get_item_by_id(item_id):
        return Item.objects.get(id=item_id)

    @staticmethod
    def get_items(user_id):
        return Item.objects.exclude(user_id=user_id).all()

    @staticmethod
    def add_item(user_id, name, price, description):
        item = Item(user_id=user_id, name=name, price=price, description=description)
        item.save()
        return item

    @staticmethod
    def delete_item(user_id, item_id):
        item = Item.objects.get(pk=item_id, user_id=user_id)
        item.delete()

    @staticmethod
    def update_item(user_id, item_id, name, price, description):
        item = Item.objects.get(pk=item_id, user_id=user_id)
        item.name = name
        item.price = price
        item.description = description
        item.save()
        return item


class ItemReservationRepository:

    @staticmethod
    def get_user_reservations(user_id):
        return ItemReservation.objects.filter(user_id=user_id).all()

    @staticmethod
    def get_reservations(item_id):
        return ItemReservation.objects.filter(item_id=item_id).all()

    @staticmethod
    def reserve_item(user_id, item_id, start_time, end_time, total_price):
        item_reservation = ItemReservation(user_id=user_id, item_id=item_id, start_date_time=start_time, end_date_time=end_time, total_price=total_price)
        item_reservation.save()
        return item_reservation

    @staticmethod
    def update_reservation(user_id, item_id, item_reservation_id, start_time, end_time, total_price):
        item_reservation = ItemReservation.objects.get(item_id=item_id, user_id=user_id, id=item_reservation_id)
        item_reservation.start_date_time = start_time
        item_reservation.end_date_time = end_time
        item_reservation.total_price = total_price
        item_reservation.save()
        return item_reservation

    @staticmethod
    def delete_reservation(user_id, item_id, reservation_id):
        item_reservation = ItemReservation.objects.get(id=reservation_id, user_id=user_id, item_id=item_id)
        item_reservation.delete()
