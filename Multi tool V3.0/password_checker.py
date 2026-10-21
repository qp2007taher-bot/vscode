"""
Password Strength Checker Module.
"""

def x():
    print("\n\n" + "-" * 45 + "\n\n")
    print("        [1] PASSWORD STRENGTH CHECKER")
    print("\n\n" + "-" * 45 + "\n\n")

    password = input("\n\nEnter a password to analyze: ")

    score = 0
    feedback = []

    # 1. Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")

    # 2. Check for numeric digits
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if has_digit:
        score += 1
    else:
        feedback.append("Password lacks numeric characters (0-9).")

    # 3. Check for special symbols
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_symbol = False
    for char in password:
        if char in symbols:
            has_symbol = True
            break

    if has_symbol:
        score += 1
    else:
        feedback.append("Password lacks special symbols (e.g., @, #, $).")

    # Display evaluation results
    print("\n\n--- Evaluation Summary ---\n\n")

    if score == 3:
        print("Result: STRONG (Passes security standards)\n\n")
    elif score == 2:
        print("Result: MODERATE (Needs improvement)\n\n")
    else:
        print("Result: WEAK (High security risk)\n\n")

    if feedback:
        print("\nRecommendations:\n")
        for note in feedback:
            print(f"  • {note}")
        print("\n")


if __name__ == "__main__":
    x()
