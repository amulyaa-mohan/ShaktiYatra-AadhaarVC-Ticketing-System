import json
from sdjwt.crypto import b64url_decode


def decode_disclosure(disclosure: str):
  
    decoded = b64url_decode(disclosure)
    salt, name, value = json.loads(decoded.decode("utf-8"))
    return salt, name, value
