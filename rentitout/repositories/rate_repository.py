from rentitout.model.rate import ItemRate


class RateRepository:

    @staticmethod
    def get_item_ratings(item_id):
        return ItemRate.objects.filter(item_id=item_id).all()

    @staticmethod
    def add_item_rating(item_id, description, value, user_id):
        item_rate = ItemRate(
            item_id=item_id,
            description=description,
            value=value,
            user_id=user_id
        )
        item_rate.save()
        return item_rate

    @staticmethod
    def update_rating(rating_id, description, value, user_id):
        item_rate = ItemRate.objects.get(id=rating_id, user_id=user_id)
        item_rate.value = value
        item_rate.description = description
        item_rate.save()
        return item_rate

    @staticmethod
    def delete_rating(rating_id, user_id):
        item_rate = ItemRate.objects.get(id=rating_id, user_id=user_id)
        item_rate.delete()
        return item_rate
