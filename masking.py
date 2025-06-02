import re

PII_PATTERNS = {
    "full_name": r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b",
    "email": r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
    "phone_number": r"\b\d{10}\b",
    "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
    "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])/?([0-9]{2}|[0-9]{4})\b"
}

def mask_pii(email_text):
    masked_text = email_text
    entities = []
    offset = 0

    for label, pattern in PII_PATTERNS.items():
        for match in re.finditer(pattern, email_text):
            start, end = match.start(), match.end()
            original = match.group()
            replacement = f"[{label}]"
            masked_text = masked_text[:start+offset] + replacement + masked_text[end+offset:]
            offset += len(replacement) - (end - start)
            entities.append({
                "position": [start, end],
                "classification": label,
                "entity": original
            })

    return masked_text, entities