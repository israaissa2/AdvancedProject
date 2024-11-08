from rest_framework import serializers

from rentitout.model.report import Report
from rentitout.serilaizers.item_serializer import ItemReservationSerializer


class ReportSerializer(serializers.ModelSerializer):
    reservation = ItemReservationSerializer(read_only=True, many=False)

    class Meta:
        model = Report
        fields = [
            'id', 'description', 'reservation', 'status'
        ]
