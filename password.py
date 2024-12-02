import re

def check_password_strength(password):
    # Initialize criteria
    length_criteria = len(password) >= 8
    complexity_criteria = (re.search(r'[a-z]', password) and
                           re.search(r'[A-Z]', password) and
                           re.search(r'[0-9]', password) and
                           re.search(r'[@$!%*?&]', password))
    
    # Common passwords list (for uniqueness check)
    common_passwords = {'password', '123456', '123456789', 'qwerty', 'abc123', 'letmein', 'welcome', 'monkey', 'password1', '12345'}
    
    uniqueness_criteria = password not in common_passwords

    # Evaluate password strength
    if not length_criteria:
        return "Weak: Password should be at least 8 characters long."
    elif not complexity_criteria:
        return "Weak: Password should include uppercase, lowercase, digits, and special characters."
    elif not uniqueness_criteria:
        return "Weak: Password is too common, choose a more unique password."
    else:
        return "Strong: Your password is strong!"

# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password to check its strength: ")
    strength_feedback = check_password_strength(user_password)
    print(strength_feedback)
