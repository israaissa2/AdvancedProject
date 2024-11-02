from rest_framework import serializers

from rentitout.model.rate import ItemRate


class ItemRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemRate
        fields = [
            'id', 'description', 'value'
        ]