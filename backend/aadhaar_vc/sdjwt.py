import io
import json
import zipfile
import base64

DEMO_DECODE_MODE = True


def b64url_decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def parse_sdjwt_zip(zip_bytes: bytes) -> dict:

    zip_file = zipfile.ZipFile(io.BytesIO(zip_bytes))

    if "sdjwt.txt" not in zip_file.namelist():
        raise ValueError("sdjwt.txt not found in ZIP")

    sdjwt_raw = zip_file.read("sdjwt.txt").decode("utf-8")

    parts = sdjwt_raw.split("~")

    # JWT part is parts[0] → ignored in demo mode
    disclosures = parts[1:]

    claims = {}

    for d in disclosures:
        decoded = json.loads(b64url_decode(d))
        _, claim_name, claim_value = decoded

        claims[claim_name.lower()] = claim_value

    return claims
