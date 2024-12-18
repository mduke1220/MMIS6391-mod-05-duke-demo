# functions.py

def calculate_grades(grades):
    """
    Calculate the average of a list of numerical grades and return a letter grade.

    :param grades: List of numerical grades
    :return: Letter grade (A, B, C, D, F)
    """
    if not grades:
        return None

    average = sum(grades) / len(grades)

    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def loan_amortization(loan_amount, interest_rate, loan_term_years):
    """
    Calculate the loan amortization schedule.

    :param loan_amount: The principal amount of the loan
    :param interest_rate: The annual interest rate (percentage)
    :param loan_term_years: The term of the loan in years
    :return: List of dictionaries containing amortization details for each month
    """
    loan_term_months = loan_term_years * 12  # Convert loan term to months
    monthly_interest_rate = interest_rate / 12 / 100  # Calculate monthly interest rate

    # Calculate the monthly payment
    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term_months))
    else:
        monthly_payment = loan_amount / loan_term_months  # Handle no interest case

    # Create a list to store the loan amortization details
    loan_amortization_list = []

    # Loop to calculate the loan amortization details for each month
    for i in range(1, loan_term_months + 1):
        interest_paid = loan_amount * monthly_interest_rate  # Calculate interest paid for the current month
        principal_paid = monthly_payment - interest_paid  # Calculate principal paid
        remaining_balance = loan_amount - principal_paid  # Calculate remaining balance after payment

        # Append the details for the current month
        loan_amortization_list.append({
            'month': i,
            'starting_balance': loan_amount,
            'interest_paid': interest_paid,
            'principal_paid': principal_paid,
            'monthly_payment': monthly_payment,
            'remaining_balance': remaining_balance
        })

        # Update the loan amount for the next month
        loan_amount = remaining_balance

    return loan_amortization_list


# Testing the functions
if __name__ == "__main__":
    # Test calculate_grades function
    grades = [85, 92, 78, 90, 88]
    letter_grade = calculate_grades(grades)
    print(f"Grades: {grades}")
    print(f"Letter Grade: {letter_grade}")

    # Test loan_amortization function
    loan_amount = 10000
    interest_rate = 5
    loan_term_years = 2
    amortization_schedule = loan_amortization(loan_amount, interest_rate, loan_term_years)
    print(f"Loan Amount: {loan_amount}, Interest Rate: {interest_rate}%, Loan Term: {loan_term_years} years")
    for month in amortization_schedule:
        print(month)