from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from marketplace.serializers.custom_jwt_serializer import CustomJwtSerializer


class CustomObtainPairApiView(TokenObtainPairView):
    serializer_class = CustomJwtSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        data = request.data
        serializer = self.serializer_class(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": "OK",
                    "access_token": serializer.validated_data["access"],
                    "refresh_token": serializer.validated_data["refresh"]
                }
            )
        except TokenError as err:
            raise InvalidToken(err.args[0])
