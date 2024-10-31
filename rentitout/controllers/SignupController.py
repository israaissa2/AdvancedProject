from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.components.auth_component import AuthComponent
from rentitout.models import User
from rentitout.serilaizers.user_serializer import UserSerializer


class SignupController(ViewSet):

    permission_classes = ()
    authentication_classes = ()

    def create(self, request):
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        role = request.data.get('role', 1)
        response = AuthComponent.add_user(
            username=email, password=password, email=email,
            first_name=first_name, last_name=last_name, role=role
        )
        if type(response) == User:
            return Response(data=UserSerializer(response).data, status=200)
        else:
            return Response('unauthorized', status=401)
