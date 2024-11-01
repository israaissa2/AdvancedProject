from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.auth import SafeJWTAuthentication
from rentitout.serilaizers.profile_serializer import ProfileSerializer


class ProfileController(ViewSet):

    authentication_classes = (SafeJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        return Response(data={'data': ProfileSerializer(request.user).data}, status=200)