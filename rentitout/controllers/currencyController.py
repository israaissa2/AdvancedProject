from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.auth import SafeJWTAuthentication
from rentitout.services.currency_service import CurrencyService


class CurrencyController(ViewSet):

    authentication_classes = (SafeJWTAuthentication,)
    permission_classes = ()

    def list(self, request):
        response = CurrencyService.get_currency_rates()
        return Response(data={'data': response}, status=200)
