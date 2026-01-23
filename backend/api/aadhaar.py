from fastapi import APIRouter, UploadFile, File
from aadhaar_vc.sdjwt import parse_sdjwt_zip
from aadhaar_vc.policy import check_policy

router = APIRouter()

@router.post("/aadhaar/verify")
async def verify_sdjwt(file: UploadFile = File(...)):
    zip_bytes = await file.read()
    claims = parse_sdjwt_zip(zip_bytes)

    return {
        "claims": claims,
        "eligible": check_policy(claims)
    }
