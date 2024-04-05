def password_strength(password):
    # Initialize the score
    score = 0
    
    # Check password length
    if len(password) >= 8:
        score += 1
    
    # Check for uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    
    # Check for lowercase letters
    if any(c.islower() for c in password):
        score += 1
    
    # Check for numeric digits
    if any(c.isdigit() for c in password):
        score += 1
    
    # Check for special symbols
    special_symbols = "!@#$%^&*"
    if any(c in special_symbols for c in password):
        score += 1
    
    return score

# Get user input
user_password = input("Enter a password: ")

# Calculate the password strength
strength_score = password_strength(user_password)

# Display the result
print(f"Password strength score: {strength_score}")
