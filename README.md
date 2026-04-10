# Shakti Yatra – Aadhaar VC Ticketing System

This project is a prototype system that demonstrates how Aadhaar-based identity verification and ticket validation can be implemented in a secure, scalable, and offline-capable transport environment.

It models a real-world architecture where identity, authorization, and verification are handled as separate layers using cryptographic trust principles.

## Project Structure
AadhaarVC/</br>
│</br>
├── frontend/ # Conductor dashboard (OVSE simulation)</br>
├── backend/ # Verification + data handling (Bridge integration)</br>
└── README.md</br>

## Documentation

- Frontend Documentation: [Frontend README](./frontend/README.md)
- Backend Documentation: [Backend README](./backend/README.md)

## System Overview

The system simulates a complete identity-driven ticketing workflow:
UIDAI (Issuer)</br>
↓</br>
Aadhaar App (Holder)</br>
↓</br>
Platform Backend (Verification + Ticket Issuance)</br>
↓</br>
OVSE Device (Conductor / Scanner)</br>
↓</br>
Passenger Access Granted / Denied</br>

## Core Components

### 1. Frontend (OVSE Simulation)
- Conductor dashboard
- QR-based trip generation
- Passenger validation logic
- Real-time counters and history
- Offline-first verification behavior

### 2. Backend (Bridge Integration)
- Handles verification logging
- Stores passenger scan data
- Retrieves historical records
- Uses Cosmitude Bridge for structured data flow

## Key Concepts

### OVSE (Offline Verification Seeking Entities)

OVSE devices are responsible for verifying credentials without requiring real-time access to the issuer.

In this system:
- The conductor dashboard acts as an OVSE simulation
- Validation is performed locally using predefined rules
- Backend is used for logging and auditing, not real-time validation

### Cosmitude Bridge Integration

The backend integrates with **Cosmitude Bridge** to:

- Store verification data in structured form flows  
- Retrieve and process historical records  
- Enable consistent and scalable data handling  

Links:
- Cosmitude Website: https://www.cosmitude.com  
- Cosmitude Bridge: https://bridge.cosmitude.com  

## Features

- Aadhaar-based verification (simulated)
- QR-based ticketing system
- Policy-based eligibility validation
- Offline-capable verification flow
- Real-time scan tracking
- History of latest 25 passenger validations
- Structured backend data storage

## Tech Stack

### Frontend
- React + TypeScript
- Vite
- Tailwind CSS
- shadcn/ui

### Backend
- Node.js / API layer
- Cosmitude Bridge integration
- Base64 encoding/decoding

## Disclaimer

**This project is a prototype implementation.**

- It uses mock data and simulated cryptographic flows
- No real Aadhaar data or UIDAI APIs are used
- Private keys are not included

This system is designed to demonstrate how identity-based verification and validation systems can be built and extended for real-world applications such as:

- Public transport ticketing
- Identity verification systems
- Offline validation environments (OVSE)
- Secure access control systems

## Acknowledgement

Thank you for reviewing this project.  
It represents my exploration of identity systems, security, and scalable architecture for real-world applications.
by **Amulya Mohan**
