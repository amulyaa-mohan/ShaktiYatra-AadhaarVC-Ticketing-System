import io
import json
import zipfile
import base64
import hashlib


def b64url_decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def sha256_b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(
        hashlib.sha256(data).digest()
    ).rstrip(b"=").decode()


def canonicalize_disclosure(disclosure: list) -> bytes:
    return json.dumps(
        disclosure,
        separators=(",", ":"),
        ensure_ascii=False
    ).encode("utf-8")


def parse_sdjwt_zip(zip_bytes: bytes) -> dict:
    zip_file = zipfile.ZipFile(io.BytesIO(zip_bytes))

    if "sdjwt.txt" not in zip_file.namelist():
        raise ValueError("sdjwt.txt not found in ZIP")

    sdjwt_raw = zip_file.read("sdjwt.txt").decode("utf-8")

    parts = sdjwt_raw.split("~")
    jwt_part = parts[0]
    disclosures = parts[1:]

    # Decode JWT payload
    _header_b64, payload_b64, _sig = jwt_part.split(".")
    payload = json.loads(b64url_decode(payload_b64))

    sd_hashes = payload.get("_sd", [])
    if not sd_hashes:
        raise ValueError("No _sd hashes found in JWT")

    verified_claims = {}

    for d in disclosures:
        decoded = json.loads(b64url_decode(d))
        salt, claim_name, claim_value = decoded

        canonical = canonicalize_disclosure(decoded)
        computed_hash = sha256_b64url(canonical)

        if computed_hash in sd_hashes:
            verified_claims[claim_name.lower()] = claim_value
    
    print("VERIFIED CLAIMS:", verified_claims)

    return verified_claims
