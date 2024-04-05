def calculate_compounded_interest(principal, apr, term):
    # Convert annual interest rate to decimal
    rate = apr / 100.0
    
    # Initialize the balance
    balance = principal
    
    # Print table header
    print(f"{'Year':<10}{'Balance':<15}")
    print("-" * 25)
    
    # Calculate compounded interest for each year
    for year in range(1, term + 1):
        interest = balance * rate
        balance += interest
        print(f"{year:<10}{balance:.2f}")
    
    return balance

# Get user input
principal = float(input("Enter the principal amount: "))
apr = float(input("Enter the annual interest rate (%): "))
term = int(input("Enter the term (in years): "))

# Calculate compounded interest
final_balance = calculate_compounded_interest(principal, apr, term)

print(f"\nFinal balance after {term} years: ${final_balance:.2f}")
