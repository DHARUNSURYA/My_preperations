def calculate_emi(principal, rate, time):
    r = rate / (12 * 100)  # Monthly interest rate
    t = time * 12  # Total number of months
    emi = (principal * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
    return emi

def main():
    principal = float(input("Enter the principal amount (Loan Amount): "))
    tenure = int(input("Enter the total tenure (in years): "))

    # Input Bank A interest rates
    n1 = int(input("Enter the number of slabs for Bank A: "))
    bank_a_rates = []
    for _ in range(n1):
        time, rate = map(float, input("Enter period and interest rate for Bank A (separated by space): ").split())
        bank_a_rates.append((time, rate))

    # Input Bank B interest rates
    n2 = int(input("Enter the number of slabs for Bank B: "))
    bank_b_rates = []
    for _ in range(n2):
        time, rate = map(float, input("Enter period and interest rate for Bank B (separated by space): ").split())
        bank_b_rates.append((time, rate))

    # Calculate EMI and total interest for Bank A
    total_interest_a = sum((calculate_emi(principal, rate, time) * time) - principal for time, rate in bank_a_rates)

    # Calculate EMI and total interest for Bank B
    total_interest_b = sum((calculate_emi(principal, rate, time) * time) - principal for time, rate in bank_b_rates)

    # Compare total interest and make a decision
    if total_interest_a < total_interest_b:
        print("Choose Bank A")
    else:
        print("Choose Bank B")

if __name__ == "__main__":
    main()
def calculate_emi(principal, rate, time):
    r = rate / (12 * 100)  # Monthly interest rate
    t = time * 12  # Total number of months
    emi = (principal * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
    return emi

def main():
    principal = float(input("Enter the principal amount (Loan Amount): "))
    tenure = int(input("Enter the total tenure (in years): "))

    # Input Bank A interest rates
    n1 = int(input("Enter the number of slabs for Bank A: "))
    bank_a_rates = []
    for _ in range(n1):
        time, rate = map(float, input("Enter period and interest rate for Bank A (separated by space): ").split())
        bank_a_rates.append((time, rate))

    # Input Bank B interest rates
    n2 = int(input("Enter the number of slabs for Bank B: "))
    bank_b_rates = []
    for _ in range(n2):
        time, rate = map(float, input("Enter period and interest rate for Bank B (separated by space): ").split())
        bank_b_rates.append((time, rate))

    # Calculate EMI and total interest for Bank A
    total_interest_a = sum((calculate_emi(principal, rate, time) * time) - principal for time, rate in bank_a_rates)

    # Calculate EMI and total interest for Bank B
    total_interest_b = sum((calculate_emi(principal, rate, time) * time) - principal for time, rate in bank_b_rates)

    # Compare total interest and make a decision
    if total_interest_a < total_interest_b:
        print("Choose Bank A")
    else:
        print("Choose Bank B")

if __name__ == "__main__":
    main()
