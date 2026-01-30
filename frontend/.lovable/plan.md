

# 🚌 Shakthi Scheme - Bus Ticket Verification System

A responsive web frontend for verifying free bus travel eligibility for women under the Government Shakthi Scheme.

---

## 🎨 Design Approach

**Theme:** Professional blue & white government-style UI
**Language:** English only
**Style:** Clean, mobile-first, accessible design with clear visual indicators (✔️ green / ❌ red)

---

## 📱 Pages & Features

### 1. Conductor Login Page
- Clean login form with Conductor ID and PIN fields
- "Forgot PIN" link (placeholder)
- Government disclaimer at bottom
- Blue header with "Shakthi Scheme" branding

### 2. Conductor Dashboard
After successful login, conductors will see:
- **Bus Selection:** Dropdown to select Bus Number
- **Route Selection:** Dropdown to select Bus Route
- **Generate QR Button:** Creates trip-specific QR code
- **QR Display:** Large, scannable QR code for passengers
- **Live Counters Panel:**
  - Total passengers scanned
  - ✔️ Verified passengers (green)
  - ❌ Not verified (red)
- Logout option

### 3. Passenger Verification Page (No Login Required)
When passenger scans the QR code:
- Government-branded header
- Message: "Verify eligibility using Aadhaar (consent-based)"
- **"Verify using Aadhaar App"** button
- Privacy disclaimer: "Aadhaar verification is consent-based and secure"
- After verification simulation:
  - **Success:** Large green checkmark with "Eligible – Shakthi Scheme Approved"
  - **Failed:** Red cross with "Not Eligible / Verification Failed"
- No Aadhaar numbers or personal data displayed

### 4. Admin Login Page
- Separate login for administrators
- Admin ID and password fields
- Access to analytics dashboard

### 5. Admin Dashboard
Comprehensive analytics view with:
- **Summary Cards:**
  - Total buses active today
  - Total QR scans
  - Total verified passengers
  - Total not verified passengers
- **Date Filter:** Today / Weekly / Monthly toggle
- **Charts:**
  - Bar chart: Bus Number vs Verified/Not Verified counts
  - Bar chart: Route-wise verified passengers
- **Conductor Performance Table:**
  - Conductor ID
  - Bus Number
  - Total scans
  - Verified count
  - Not verified count
- Export functionality (placeholder)

---

## 🔄 User Flows

**Conductor Flow:**
Login → Select Bus & Route → Generate QR → View live scan counters

**Passenger Flow:**
Scan QR → View verification page → Tap "Verify" → See result (✔️ or ❌)

**Admin Flow:**
Login → View dashboard → Filter by date → Analyze charts/tables

---

## 🛠 Technical Approach

- **Routing:** React Router for navigation between all pages
- **State Management:** React Context for auth state & mock data
- **Charts:** Recharts library (already installed) for analytics
- **QR Generation:** QR code library for trip codes
- **Mock Data:** Simulated API responses for conductors, routes, verification
- **Mobile-First:** Tailwind responsive utilities throughout

---

## 📋 Compliance Features

- No Aadhaar data collection or storage
- Clear consent-based verification messaging
- Government-appropriate visual styling
- Accessibility considerations (contrast, touch targets)

