#............Capston Project 1.......................................

import math  # Importing math module for mathematical operations

def calculate_investment():
    # Asking user for input
    P = float(input("Enter the amount of money you are depositing: "))  # Principal amount
    r = float(input("Enter the interest rate (as a percentage): ")) / 100  # Annual interest rate
    t = int(input("Enter the number of years you plan on investing: "))  # Time period in years
    interest = input("Do you want simple or compound interest? ").lower()  # Interest type

    # Calculating the total amount based on the interest type
    if interest == "simple":
        A = P * (1 + r * t)  # Simple interest formula
    elif interest == "compound":
        A = P * math.pow((1 + r), t)  # Compound interest formula
    else:
        print("Invalid input! Please enter either 'simple' or 'compound'.")
        return

    # Displaying the result
    print(f"Total amount after {t} years: {A}")

def calculate_bond():
    # Asking user for input
    P = float(input("Enter the present value of the house: "))  # Present value of the house
    i = float(input("Enter the interest rate (as a percentage): ")) / 100 / 12  # Monthly interest rate
    n = int(input("Enter the number of months to repay the bond: "))  # Time period in months

    # Calculating the monthly repayment amount
    repayment = (i * P) / (1 - (1 + i) ** (-n))

    # Displaying the result
    print(f"Monthly repayment: {repayment}")

def main():
    # Displaying the menu
    print("Welcome to the finance calculator!")
    print("Menu:")
    print("1. Investment")
    print("2. Bond")

    # Getting user's choice
    choice = input("Enter your choice (1 or 2): ")

    # Processing user's choice
    if choice == "1" or choice.lower() == "investment":
        calculate_investment()  # Calculate investment
    elif choice == "2" or choice.lower() == "bond":
        calculate_bond()  # Calculate bond
    else:
        print("Invalid choice! Please enter either '1' or '2'.")

# Running the main function if the script is executed
if __name__ == "__main__":
    main()