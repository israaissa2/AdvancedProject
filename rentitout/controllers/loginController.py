from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.helpers.token_helper import TokenHelper
from rentitout.models import User
from rentitout.serilaizers.user_serializer import UserSerializer


class LoginController(ViewSet):
    permission_classes = ()
    authentication_classes = (TokenAuthentication,)

    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            raise exceptions.AuthenticationFailed('username and password required')
        user = User.objects.filter(email=email).first()
        if not user:
            raise exceptions.AuthenticationFailed('user not found')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('wrong password')

        serialized_user = UserSerializer(user).data

        access_token = TokenHelper.generate_access_token(user)
        refresh_token = TokenHelper.generate_refresh_token(user)

        response = Response()
        response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
        response.data = {
            'access_token': access_token,
            'user': serialized_user,
        }

        return response
