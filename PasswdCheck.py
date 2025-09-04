import re

def check_strength(password):
    """Check password strength based on length and character variety."""
    length = len(password)
    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_digit = re.search(r"[0-9]", password)
    has_special = re.search(r"[^a-zA-Z0-9]", password)

    score = sum([bool(has_lower), bool(has_upper), bool(has_digit), bool(has_special)])

    if length < 8 or score < 2:
        return "Weak"
    elif length >= 8 and score >= 2 and score < 4:
        return "Medium"
    elif length >= 12 and score == 4:
        return "Strong"
    else:
        return "Medium"


def expand_details(name, dob, phone, pet, hobbies):
    """Expand personal details into multiple possible weak patterns."""
    details = []

    # Name: split into words
    if name:
        details.extend(name.split())

    # DOB: try year, MMDD, etc.
    if dob:
        details.append(dob)
        if len(dob) == 8:  # e.g. DDMMYYYY
            details.append(dob[-4:])   # year
            details.append(dob[:2])    # day
            details.append(dob[2:4])   # month
            details.append(dob[:4])    # DDMM
        elif len(dob) == 4:  # just year
            details.append(dob)

    # Phone: include last 4 digits
    if phone:
        details.append(phone)
        if len(phone) >= 4:
            details.append(phone[-4:])

    # Pet name
    if pet:
        details.append(pet)

    # Hobbies
    if hobbies:
        details.extend(hobbies)

    return [d.strip().lower() for d in details if d.strip()]


def check_social_engineering(password, details):
    """Check if password contains any detail or partial match."""
    password_lower = password.lower()
    for detail in details:
        if detail and detail in password_lower:
            return True, detail
    return False, None


def threat_vectors(strength, social_eng):
    """Return likely threat vectors based on analysis."""
    vectors = []
    if strength == "Weak":
        vectors.append("Brute-force, Dictionary Attacks")
    if social_eng:
        vectors.append("Social Engineering Attacks")
    if strength == "Strong" and not social_eng:
        vectors.append("Lower Risk (still rotate passwords regularly)")
    return vectors


def main():
    print("\n🔐 Password & Social Engineering Risk Analyzer 🔐\n")

    # Collect personal details
    name = input("Enter your full name: ").strip()
    dob = input("Enter your date of birth (YYYY or DDMMYYYY): ").strip()
    phone = input("Enter your phone number: ").strip()
    pet = input("Enter your pet's name: ").strip()
    hobbies = input("Enter your hobbies/favorites (comma-separated): ").strip().split(",")

    # Expand details into common weak patterns
    details = expand_details(name, dob, phone, pet, hobbies)

    # Get password to test
    password = input("\nEnter the password you want to test: ").strip()

    # Strength check
    strength = check_strength(password)

    # Social engineering check
    social_risk, detail = check_social_engineering(password, details)

    # Threat vectors
    vectors = threat_vectors(strength, social_risk)

    # Results
    print("\n--- Analysis Report ---")
    print(f"Password Strength: {strength}")
    if social_risk:
        print(f"Social Engineering Risk: HIGH – Your password contains personal detail ({detail})")
    else:
        print("Social Engineering Risk: Low – No personal info detected in password")

    if vectors:
        print("Threat Vectors: " + ", ".join(vectors))
    else:
        print("Threat Vectors: None detected")

    # Awareness tip
    if strength == "Weak" or social_risk:
        print("⚠️ Awareness Tip: Avoid using personal info or short/common words in passwords.")
        print("   Try something like: C!rcuit$2024x")
    else:
        print("✅ Good Job: Your password looks strong. Keep rotating it periodically!")

    # Example passwords
    print("\n--- Example Passwords ---")
    print("Weak   : password123")
    print("Medium : Cricket@2022")
    print("Strong : J9!rT&7bQ*5p\n")


if __name__ == "__main__":
    main()
