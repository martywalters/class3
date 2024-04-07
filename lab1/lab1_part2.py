#Intermediate Python Programming - Lab1 "Part 2" Sean Walters
#Python script that grades the strength of a password

# Initialize the score
score = 0
# Get user input
password = input("Enter a password: ")

# Check password length  1 point
if len(password) >= 8:
    score += 1
    
#loops for checking
#loop looking for UPPER CASE letter,  find then break   
for c in password:
    if c.isupper():
        score += 1
        break
#loop looking for LOWER CASE letter,  find then break 
for c in password:
    if c.islower():
        score += 1
        break
#loop looking for DIGIT,  find then break
for c in password:
    if c.isdigit():
        score += 1
        break
#loop looking for SYMBOL, find then break
special_symbols = "!@#$%^&*"
for c in password:
    if c in special_symbols:
        score += 1
        break
#extra credit
#password length greater then 8 one bonus point,
#password length greater then or equal 16  one bonus point
if len(password) > 8:
    score += 1
if len(password) >= 16:
    score += 1

# Display the result
print(f"Your password score is: {score}")
