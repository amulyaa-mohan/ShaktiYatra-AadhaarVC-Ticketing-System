'''from fastapi import APIRouter
from backend.ticketing.ticket import build_ticket
from backend.ticketing.signer import sign_ticket
from backend.ticketing.qr import generate_qr
from backend.utils import now
from backend.config import TICKET_EXPIRY_SECONDS

router = APIRouter()

@router.post("/ticket/issue")
def issue_ticket(eligible: bool):
    ticket = build_ticket(
        policy_result=eligible,
        issued_at=now(),
        exp=now() + TICKET_EXPIRY_SECONDS
    )
    token = sign_ticket(ticket)
    generate_qr(token, "output/generated_qr.png")
    return {"ticket_token": token}
'''
from fastapi import APIRouter

router = APIRouter()

@router.post("/issue")
def issue_ticket():
    return {"ticket": "dummy"}
