

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.auth import SafeJWTAuthentication
from rentitout.components.item_component import ItemComponent
from rentitout.serilaizers.item_serializer import UserItemSerializer


class UserItemController(ViewSet):

    authentication_classes = (SafeJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        items = ItemComponent.get_user_items(request.user.id)
        return Response(data={'data': UserItemSerializer(items, many=True).data}, status=200)
