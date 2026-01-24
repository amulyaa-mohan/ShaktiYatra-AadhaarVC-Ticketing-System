'''from fastapi import FastAPI
from backend.api import aadhaar, ticket, gate

app = FastAPI(title="Aadhaar VC Ticketing Platform")

app.include_router(aadhaar.router, prefix="/aadhaar")
app.include_router(ticket.router, prefix="/ticket")
app.include_router(gate.router, prefix="/gate")

@app.get("/")
def health():
    return {"status": "running"}
'''
from fastapi import FastAPI

from backend.api import aadhaar, ticket, gate

app = FastAPI(title="Aadhaar VC Ticketing Platform")

app.include_router(aadhaar.router, prefix="/aadhaar", tags=["Aadhaar"])
app.include_router(ticket.router, prefix="/ticket", tags=["Ticket"])
app.include_router(gate.router, prefix="/gate", tags=["Gate"])

@app.get("/")
def health():
    return {"status": "running"}
