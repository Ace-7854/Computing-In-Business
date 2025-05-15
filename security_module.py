import re

def sanitize_input(user_input: str) -> str:
    """
    Removes potentially harmful characters and SQL keywords from input.
    This is NOT a substitute for parameterized queries!
    """
    # Remove common SQL injection characters
    blacklist_chars = r"[\'\";#--]"
    cleaned = re.sub(blacklist_chars, "", user_input)

    # Remove SQL keywords (case-insensitive)
    sql_keywords = [
        "SELECT", "INSERT", "UPDATE", "DELETE", "DROP", "UNION",
        "ALTER", "CREATE", "REPLACE", "WHERE", "FROM", "OR", "AND"
    ]
    for keyword in sql_keywords:
        pattern = re.compile(rf"\b{keyword}\b", re.IGNORECASE)
        cleaned = pattern.sub("", cleaned)

    return cleaned.strip()
