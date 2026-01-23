from fastapi import APIRouter
from ticketing.ticket import build_ticket
from ticketing.signer import sign_ticket
from ticketing.qr import generate_qr
from utils import now
from config import TICKET_EXPIRY_SECONDS

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
