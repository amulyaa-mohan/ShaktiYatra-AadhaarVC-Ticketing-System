import io, zipfile, json, base64, hashlib

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
    valid_hashes = payload_json["_sd"]

    claims = {}

    for disclosure in disclosures:
        decoded = json.loads(b64url_decode(disclosure))
        canon = json.dumps(decoded, separators=(",", ":")).encode()
        if sha256_b64url(canon) in valid_hashes:
            _, name, value = decoded
            claims[name] = value

    return claims
