import datetime
import jwt
from rentitout_conf import settings


class TokenHelper:

    @staticmethod
    def generate_access_token(user):
        access_token_payload = {
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7, minutes=0),
            'iat': datetime.datetime.utcnow(),
        }
        access_token = jwt.encode(
            access_token_payload,
            settings.SECRET_KEY, algorithm='HS256'
        )
        return access_token

    @staticmethod
    def generate_refresh_token(user):
        refresh_token_payload = {
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
            'iat': datetime.datetime.utcnow()
        }
        refresh_token = jwt.encode(
            refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')

        return refresh_token
