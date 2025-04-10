from datetime import timedelta

import jwt
from decouple import config
from django.utils import timezone

SECRET_KEY = config('SECRET_KEY')


def create_token(user_id):
    payload_access = {
        'user_id': user_id,
        'exp': timezone.now() + timedelta(minutes=5),
        "token_type": "access"
    }

    payload_refresh = {
        'user_id': user_id,
        'exp': timezone.now() + timedelta(days=7),
        "token_type": "refresh"
    }

    access_token = jwt.encode(payload=payload_access, key=SECRET_KEY, algorithm='HS256')
    refresh_token = jwt.encode(payload=payload_refresh, key=SECRET_KEY, algorithm='HS256')

    return {
        "access": access_token,
        "refresh": refresh_token
    }


def verify_token(token, secret=SECRET_KEY, excepted_type='access'):
    try:
        payload = jwt.decode(token, secret, ['HS256'])

        if payload.get('token_type') != excepted_type:
            return None

        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
