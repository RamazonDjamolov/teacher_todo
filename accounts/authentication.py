from rest_framework.authentication import SessionAuthentication, BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication
from accounts.models import User
from accounts.serializers import UserSerializer
from accounts.utils import verify_token


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class JWTAuthentication(BaseAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth_header = get_authorization_header(request).split()

        if not auth_header or auth_header[0].lower() != self.keyword.lower().encode():
            return None
        if not auth_header:
            raise AuthenticationFailed('header xato')
        try:
            key, token = auth_header
            # sasa assas asas
        except ValueError:
            raise AuthenticationFailed('Bearer <token> korinishida ber')

        if key.decode().lower() != 'bearer':
            raise AuthenticationFailed('Bearer <token> korinishida ber')

        payload = verify_token(token.decode())
        if not payload:
            raise AuthenticationFailed('expired data')
        try:
            user = User.objects.get(id=payload.get('user_id'))
        except User.DoesNotExist:
            raise AuthenticationFailed('xato')

        return user, None
