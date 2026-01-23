import base64
import json


def encode_zip(zip_bytes: bytes) -> str:
    payload = {
        "type": "sd-jwt-vp",
        "encoding": "base64",
        "payload": base64.urlsafe_b64encode(zip_bytes).decode()
    }
    return json.dumps(payload)

def decode_zip(payload_str: str) -> bytes:
    data = json.loads(payload_str)
    if data["type"] != "sd-jwt-vp":
        raise ValueError("Invalid QR payload type")
    return base64.urlsafe_b64decode(data["payload"])
