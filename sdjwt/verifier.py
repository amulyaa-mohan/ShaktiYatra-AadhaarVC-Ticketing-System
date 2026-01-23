import io
import json
import zipfile

from sdjwt.parser import parse_sdjwt
from sdjwt.disclosure import decode_disclosure
from sdjwt.crypto import sha256_b64url, b64url_decode


def verify_sdjwt_zip(zip_bytes: bytes) -> dict:
    

    zip_file = zipfile.ZipFile(io.BytesIO(zip_bytes))

    if "sdjwt.txt" not in zip_file.namelist():
        raise ValueError("sdjwt.txt not found in ZIP")

    sdjwt_compact = zip_file.read("sdjwt.txt").decode("utf-8")

    jwt_part, disclosures = parse_sdjwt(sdjwt_compact)

    print("Total disclosures found:", len(disclosures))

    try:
        header_b64, payload_b64, _signature = jwt_part.split(".")
    except ValueError:
        raise ValueError("Invalid JWT format")

    payload = json.loads(b64url_decode(payload_b64))

    sd_hashes = payload.get("_sd")
    if not sd_hashes:
        raise ValueError("No _sd hashes found in JWT payload")

    verified_claims = {}

    for disclosure in disclosures:
        computed_hash = sha256_b64url(
            disclosure.encode("utf-8")
        )

        salt, claim_name, claim_value = decode_disclosure(disclosure)

        print("Claim:", claim_name)
        print("Computed hash:", computed_hash)
        print("Valid:", computed_hash in sd_hashes)
        print("-" * 40)

        if computed_hash in sd_hashes:
            verified_claims[claim_name] = claim_value

    return verified_claims
