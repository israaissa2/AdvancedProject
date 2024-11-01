

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.auth import SafeJWTAuthentication
from rentitout.components.item_component import ItemComponent
from rentitout.serilaizers.item_serializer import ItemSerializer


class ItemController(ViewSet):

    authentication_classes = (SafeJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        items = ItemComponent.get_items(request.user.id)
        return Response(data={'data': ItemSerializer(items, many=True).data}, status=200)

    def create(self, request):
        item = ItemComponent.add_item(
            user_id=request.user.id,
            item_name=request.data['name'],
            item_description=request.data['description'],
            item_price=request.data['price']
        )
        return Response(data={'data': ItemSerializer(item, many=False).data}, status=200)

    def update(self, request, pk=None):
        item = ItemComponent.update_item(
            user_id=request.user.id,
            item_id=int(pk),
            item_name=request.data['name'],
            item_description=request.data['description'],
            item_price=request.data['price']
        )
        return Response(data={'data': ItemSerializer(item, many=False).data}, status=200)

    def destroy(self, request, pk=None):
        ItemComponent.delete_item(
            user_id=request.user.id,
            item_id=int(pk)
        )
        return Response(data={'status': 'removed Successfully'}, status=200)

