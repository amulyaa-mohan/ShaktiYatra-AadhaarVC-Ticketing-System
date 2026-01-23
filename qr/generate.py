import json
import secrets
import qrcode
from pathlib import Path


OUTPUT_QR = Path("output/sdjwt_request_qr.png")


def generate_sdjwt_request_qr():
    qr_payload = {
        "type": "sd-jwt-request",
        "protocol": "sd-jwt-v1",
        "verifier": "aadhaar-vc-demo",
        "nonce": secrets.token_urlsafe(16),
        "requested_claims": [
            "ResidentName",
        ]
    }

    qr_data = json.dumps(qr_payload, separators=(",", ":"))

    qr = qrcode.QRCode(
        version=None,  # auto
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(OUTPUT_QR)

    print("QR generated:", OUTPUT_QR)
    print("QR payload:", qr_payload)


if __name__ == "__main__":
    generate_sdjwt_request_qr()
