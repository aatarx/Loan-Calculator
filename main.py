def calculate_loan(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_months = int(years * 12)  # Convert years to an integer

    # Calculate monthly payment
    monthly_payment_amount = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -total_months)

    # Generate amortization schedule
    remaining_balance = principal
    amortization_schedule = []
    for month in range(1, total_months + 1):
        interest_amount = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment_amount - interest_amount
        remaining_balance -= principal_payment

        amortization_schedule.append({
            "Month": month,
            "Payment": monthly_payment_amount,
            "Principal": principal_payment,
            "Interest": interest_amount,
            "Balance": remaining_balance
        })

    return monthly_payment_amount, amortization_schedule

def print_amortization_schedule(amortization_schedule):
    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format('Month', 'Payment', 'Principal', 'Interest', 'Balance'))
    for payment in amortization_schedule:
        print("{:<10} ${:<14.2f} ${:<14.2f} ${:<14.2f} ${:<14.2f}".format(
            payment['Month'], payment['Payment'], payment['Principal'], payment['Interest'], payment['Balance']))

# User inputs
loan_amount = float(input("Enter the loan amount: "))  # Principal amount
annual_rate = float(input("Enter the annual interest rate: "))  # Annual interest rate
loan_years = int(input("Enter the loan tenure in years: "))  # Loan tenure in years as an integer

monthly_payment, amortization_table = calculate_loan(loan_amount, annual_rate, loan_years)

print(f"\nMonthly Payment: ${monthly_payment:.2f}")
print("\nAmortization Schedule:")
print_amortization_schedule(amortization_table)

