from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.auth import SafeJWTAuthentication
from rentitout.services.currency_service import CurrencyService


class CurrencyConvertController(ViewSet):

    authentication_classes = (SafeJWTAuthentication,)
    permission_classes = ()

    def list(self, request):
        response = CurrencyService.convert_currency_rates(
            base_currency=request.query_params.get('from'),
            to_currency=request.query_params.get('to'),
            amount=request.query_params.get('amount')
        )
        return Response(data={'data': response}, status=200)
