def calculate_compounded_interest(principal, apr, term):
    # Convert annual interest rate to decimal
    rate = apr / 100.0
    
    # Initialize the balance
    balance = principal
    
    # Print table header

    
    # Calculate compounded interest for each year
    print(f"{'Year':<4}{'Interest':>15}{'Balance':>15}")
    print("=" * 34)
    for year in range(1, term + 1):
        interest = balance * rate
        balance += interest

        print(f"{year:>4}  ${interest:>12,.2f}  ${balance:>12,.2f}")
    
    return balance

# Get user input
principal = float(input("Enter the principal amount: "))
if principal <1 or principal > 1000000:
    print('error principal')
apr = float(input("Enter the annual interest rate (%): "))
if apr < 0 or apr > 100:
    print('error apr')
term = int(input("Enter the term (in years): "))
if term < 1 or term > 30:
    print('error term')

# Calculate compounded interest
final_balance = calculate_compounded_interest(principal, apr, term)

#print(f"\nFinal balance after {term} years: ${final_balance:.2f}")
