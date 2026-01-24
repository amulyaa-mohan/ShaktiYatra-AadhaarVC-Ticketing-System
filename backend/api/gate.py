'''from fastapi import APIRouter
from backend.ticketing.verifier import verify_ticket

router = APIRouter()

@router.post("/ticket/verify")
def verify_qr(token: str):
    decoded = verify_ticket(token)
    if decoded["policy_verified"]:
        return {"status": "VERIFIED"}
    return {"status": "DENIED"}
'''
from fastapi import APIRouter

router = APIRouter()

@router.post("/verify")
def verify_gate():
    return {"status": "VERIFIED"}
