def build_ticket(policy_result: bool, issued_at: int, exp: int):
    return {
        "iss": "AadhaarVC-Ticketing",
        "policy_verified": policy_result,
        "iat": issued_at,
        "exp": exp
    }
