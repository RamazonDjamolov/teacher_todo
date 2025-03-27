from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import LoginSerializers


class LoginAPIView(APIView):
    def post(self, request):
        serializers = LoginSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data.get('user')
        login(request, user)
        return Response(data={"message": "successfully"})
