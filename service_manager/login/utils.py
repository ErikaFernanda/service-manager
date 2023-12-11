import time
import uuid

import jwt

from django.conf import settings
from django.http import JsonResponse



def generate_jwt(user,company_id, token_type: str, algorithm: str = "HS256"):
    now = int(time.time())

    if token_type == "access":
        exp = now + (settings.ACCESS_TOKEN_EXPIRATION * 60)
    else:
        exp = now + (settings.REFRESH_TOKEN_EXPIRATION * 60)
    return jwt.encode(
        {
            "token_type": token_type,
            "exp": exp,
            "jti": str(uuid.uuid4()),
            "user_id": user.id,
            "name": user.name,
            "email": user.email,
            "company_id":company_id

          
        },
        settings.SECRET_KEY,
        algorithm=algorithm,
    )


def validate_jwt(token):
    try:
        decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

        return decoded_payload

    except jwt.ExpiredSignatureError:
        return JsonResponse({"error": "Token expirado."}, status=401)

    except jwt.InvalidTokenError:
        return JsonResponse({"error": "Token inválido."}, status=401)