import firebase_admin
import firebase_admin.auth
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from core.models import User


class FirebaseAuthentication(TokenAuthentication):
    model = User

    def authenticate_credentials(self, key):
        try:
            user_token = firebase_admin.auth.verify_id_token(key)
            email = user_token['email']
            uid = user_token["uid"]
        except Exception:
            raise exceptions.AuthenticationFailed('Invalid token.')

        user, created = User.objects.get_or_create(auth_id=uid,
                                                   email=email,
                                                   username=email)

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (user, None)
