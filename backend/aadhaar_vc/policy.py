def check_policy(claims: dict) -> bool:
    return (
        claims.get("Gender", "").upper() == "FEMALE"
        and claims.get("State", "").upper() == "KARNATAKA"
    )
