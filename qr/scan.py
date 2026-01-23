import cv2
import json
from pathlib import Path
from sdjwt.verifier import verify_sdjwt_zip

QR_IMAGE = Path("output/sdjwt_qr.png")
SDJWT_ZIP = Path("input/sdjwt.zip")  
OUTPUT_JSON = Path("output/extracted_claims.json")

def main():
    img = cv2.imread(str(QR_IMAGE))
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)

    qr_data = json.loads(data)

    if qr_data["ref"] != "LOCAL_SDJWT_001":
        raise ValueError("Unexpected QR type")

    zip_bytes = SDJWT_ZIP.read_bytes()

    claims = verify_sdjwt_zip(zip_bytes)
    OUTPUT_JSON.write_text(json.dumps(claims, indent=2))

    print("Extracted claims written to", OUTPUT_JSON)

if __name__ == "__main__":
    main()
