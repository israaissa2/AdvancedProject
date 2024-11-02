from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.auth import SafeJWTAuthentication
from rentitout.components.item_component import ItemReservationComponent
from rentitout.serilaizers.item_serializer import ItemReservationSerializer


class ItemReservationController(ViewSet):

    authentication_classes = (SafeJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request, items_pk=None):
        item_reservation = ItemReservationComponent.get_reservations(item_id=int(items_pk))

        return Response(data={'data': ItemReservationSerializer(item_reservation, many=True).data}, status=200)

    def create(self, request, items_pk=None):
        item_reservation = ItemReservationComponent.add_reservation(
            item_id=int(items_pk),
            user_id=request.user.id,
            start_time=request.data['start_date_time'],
            end_time=request.data['end_date_time'],
            lat=request.data['lat'],
            lng=request.data['lng'],
            receive_type=request.data['receive_type']
        )
        return Response(data={'data': ItemReservationSerializer(item_reservation, many=False).data}, status=200)

    def update(self, request, items_pk=None, pk=None):
        item_reservation = ItemReservationComponent.update_reservation(
            item_id=int(items_pk),
            user_id=request.user.id,
            item_reservation_id=int(pk),
            start_time=request.data['start_date_time'],
            end_time=request.data['end_date_time'],
            lat=request.data['lat'],
            lng=request.data['lng'],
            receive_type=request.data['receive_type']
        )
        return Response(data={'data': ItemReservationSerializer(item_reservation, many=False).data}, status=200)

    def destroy(self, request, items_pk=None, pk=None):
        ItemReservationComponent.delete_reservation(
            item_id=int(items_pk),
            user_id=request.user.id,
            reservation_id=int(pk)
        )
        return Response(data={'status': 'Deleted Successfully'}, status=200)
