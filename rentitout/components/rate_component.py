from rentitout.repositories.rate_repository import RateRepository


class RateComponent:
    @staticmethod
    def get_item_ratings(item_id):
        return RateRepository.get_item_ratings(item_id=item_id)

    @staticmethod
    def add_item_rating(item_id, user_id, description, value):
        return RateRepository.add_item_rating(
            item_id=item_id,
            user_id=user_id,
            description=description,
            value=value
        )

    @staticmethod
    def remove_item_rating(rating_id, user_id):
        RateRepository.delete_rating(rating_id=rating_id, user_id=user_id)

    @staticmethod
    def update_rating(rating_id, user_id, description, value):
        return RateRepository.update_rating(
            user_id=user_id,
            rating_id=rating_id,
            description=description,
            value=value
        )
