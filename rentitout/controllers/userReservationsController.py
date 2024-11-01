from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.auth import SafeJWTAuthentication
from rentitout.components.item_component import ItemReservationComponent
from rentitout.models import User
from rentitout.serilaizers.item_serializer import ItemReservationSerializer


class UserReservationController(ViewSet):

    authentication_classes = (SafeJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user_reservations = ItemReservationComponent.get_reservation_items(request.user.id)
        return Response(data={'data': ItemReservationSerializer(user_reservations, many=True).data}, status=200)
