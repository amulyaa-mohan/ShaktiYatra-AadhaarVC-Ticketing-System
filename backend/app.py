from fastapi import FastAPI
from api import aadhaar, ticket, gate

app = FastAPI()

app.include_router(aadhaar.router)
app.include_router(ticket.router)
app.include_router(gate.router)
