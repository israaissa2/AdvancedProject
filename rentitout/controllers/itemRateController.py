from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.auth import SafeJWTAuthentication
from rentitout.components.rate_component import RateComponent
from rentitout.models import User
from rentitout.serilaizers.rate_serializer import ItemRateSerializer


class ItemRateController(ViewSet):

    authentication_classes = (SafeJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request, items_pk=None):
        ratings = RateComponent.get_item_ratings(int(items_pk))
        return Response(data={'data': ItemRateSerializer(ratings, many=True).data}, status=200)

    def create(self, request, items_pk=None):
        rating = RateComponent.add_item_rating(
            item_id=int(items_pk),
            user_id=request.user.id,
            description=request.data['description'],
            value=request.data['value'],
        )
        return Response(data={'data': ItemRateSerializer(rating, many=False).data}, status=200)

    def update(self, request, items_pk=None, pk=None):
        rating = RateComponent.update_rating(
            rating_id=int(pk),
            user_id=request.user.id,
            description=request.data['description'],
            value=request.data['value'],
        )
        return Response(data={'data': ItemRateSerializer(rating, many=False).data}, status=200)

    def destroy(self, request, items_pk=None, pk=None):
        RateComponent.remove_item_rating(
            rating_id=int(pk),
            user_id=request.user.id,
        )
        return Response(data={'status': 'Success'}, status=200)
