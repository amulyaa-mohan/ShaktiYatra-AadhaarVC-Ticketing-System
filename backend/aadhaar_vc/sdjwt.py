import io, json, zipfile, base64, hashlib

def b64url_decode(data: str) -> bytes:
    padding = '=' * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)

def sha256_b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(
        hashlib.sha256(data).digest()
    ).rstrip(b"=").decode()

def parse_sdjwt_zip(zip_bytes: bytes) -> dict:
    zf = zipfile.ZipFile(io.BytesIO(zip_bytes))
    token = zf.read("sdjwt.txt").decode()

    jwt_part, *disclosures = token.split("~")
    header, payload, _sig = jwt_part.split(".")

    payload_json = json.loads(b64url_decode(payload))
    hashes = payload_json["_sd"]

    claims = {}

    for d in disclosures:
        raw = json.loads(b64url_decode(d))
        salt, name, value = raw
        canon = json.dumps(raw, separators=(",", ":")).encode()
        if sha256_b64url(canon) in hashes:
            claims[name] = value

    return claims
