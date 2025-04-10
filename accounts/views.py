from django.contrib.auth import login, logout
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from accounts.serializers import LoginSerializers, UserSerializer, UserCreateSerializers, LoginWithTokenSerializer


class LoginAPIView(APIView):
    def post(self, request):
        serializers = LoginSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data.get('user')
        login(request, user)
        return Response(UserSerializer(user).data)


class LogoutAPIView(APIView):
    def delete(self, request):
        logout(request)
        return Response(data={"message": "logout"})


class SessionAPIView(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return Response(data={"message": "not login"})
        return Response(UserSerializer(request.user).data)


class RegisterAPIView(APIView):
    def post(self, request):
        serializers = UserCreateSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.save()
        return Response(UserSerializer(user).data)


class LoginWithTokenViewSet(GenericViewSet):
    serializer_class = LoginWithTokenSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
