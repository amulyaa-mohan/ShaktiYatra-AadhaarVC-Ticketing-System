import jwt
from config import PLATFORM_PUBLIC_KEY

def verify_ticket(token: str) -> dict:
    return jwt.decode(
        token,
        PLATFORM_PUBLIC_KEY.read_text(),
        algorithms=["RS256"]
    )
