from rest_framework import serializers

from rentitout.model.item import Item, ItemReservation
from rentitout.serilaizers.user_serializer import UserSerializer


class ItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, source='user', read_only=True)

    class Meta:
        model = Item
        fields = [
            'id', 'name', 'description', 'price', 'owner'
        ]


class UserItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'id', 'name', 'description', 'price'
        ]


class ItemReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    item = ItemSerializer(many=False, read_only=True)

    class Meta:
        model = ItemReservation
        fields = [
            'id', 'item', 'start_date_time', 'end_date_time', 'total_price',
            'user'
        ]
