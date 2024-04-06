# Initialize the score
score = 0
# Get user input
password = input("Enter a password: ")    
# Check password length

if len(password) >= 8:
    score += 1
if len(password) > 8:
    score += 1
if len(password) >= 16:
    score += 1


for c in password:
    if c.isupper():
        score += 1
        break
for c in password:
    if c.islower():
        score += 1
        break
for c in password:
    if c.isdigit():
        score += 1
        break
special_symbols = "!@#$%^&*"
for c in password:
    if c in special_symbols:
        score += 1
        break

# Display the result
print(f"Your password score is: {score}")
