from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token


class CustomJwtSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        token: Token = super().get_token(user)
        #TODO: Add converting date to string token["date_joined"] = user.date_joined
        token["username"] = user.username

        return token
