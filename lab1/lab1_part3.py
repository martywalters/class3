#Intermediate Python Programming - Lab1 "Part 3" Sean Walters

#python script to calculate compounded interest for given principal
#amount using a given interest rate and duration.

#boolean to test control testing user input
valid_principal = True
valid_apr = True
valid_term = True
# Get user input

principal = float(input("Enter the principal amount (ex: 1000.00): "))
if principal <1 or principal > 1000000:
    print(f'Error principal {principal:.2f} not between 1 and 1,000,000')
    valid_principal = False
    
apr = float(input("Enter interest rate percentage (ex: 4.5): "))
if apr < 0 or apr > 100:
    valid_apr = False
    print(f'Error APR {apr:.2f} not between 0 and 100')
     
term = int(input("Enter term in years (ex: 10): "))
if term < 1 or term > 30:
    valid_term = False
    print(f'Error term {term:.2f} not between 1 and 30')

#verify that user data entry is valid
#if valid data calculate.
if valid_principal and valid_apr and valid_term:
    # Calculate compounded interest
    #final_balance = calculate_compounded_interest(principal, apr, term)
    
    # Convert annual interest rate to decimal
    rate = apr / 100.0

    # Initialize the balance
    balance = principal

    # Calculate compounded interest for each year
    print(f"{'Year':<4}{'Interest':>15}{'Balance':>15}")
    print("=" * 34)
    for year in range(1, term + 1):
        interest = balance * rate
        balance += interest
        print(f"{year:>4}  ${interest:>12,.2f}  ${balance:>12,.2f}")
        
#user input invalid
else:
    print('Invalid data entry. see above for error')

