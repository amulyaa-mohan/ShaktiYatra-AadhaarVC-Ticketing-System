def check_policy(claims: dict) -> bool:

    gender = claims.get("gender", "")
    address = claims.get("address", "")

    if not isinstance(gender, str):
        return False

    if gender.lower() != "female":
        return False

    # Convert address to string safely
    address_str = ""

    if isinstance(address, str):
        address_str = address
    elif isinstance(address, dict):
        address_str = " ".join(str(v) for v in address.values())

    return "karnataka" in address_str.lower()
