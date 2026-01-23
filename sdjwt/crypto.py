import hashlib
import base64

def b64url_decode(data: str) -> bytes:

    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)

def sha256_b64url(data: bytes) -> str:

    digest = hashlib.sha256(data).digest()
    return base64.urlsafe_b64encode(digest).decode("utf-8").rstrip("=")
