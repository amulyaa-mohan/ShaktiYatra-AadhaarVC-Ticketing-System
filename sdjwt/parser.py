def parse_sdjwt(compact: str):
  
    first_sep = compact.find("~")
    if first_sep == -1:
        raise ValueError("Invalid SD-JWT format: no disclosures found")

    jwt_part = compact[:first_sep]
    disclosures_part = compact[first_sep + 1 :]

    disclosures = disclosures_part.split("~")
    return jwt_part, disclosures
