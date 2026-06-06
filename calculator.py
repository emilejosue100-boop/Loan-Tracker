# this file will help handle calculations about my clients

# depending on the interest rate this function returns the total amount to repay and the the monthly amount to pay based on the loan amount, whether the client is a member of the cooperative, and the repayment period.
def calculate_interest(loan_amount,is_member,repayment_period):
    if is_member:
        # if the client is a member of the cooperative, they get a lower interest rate of 5%. If they are not a member, they get a higher interest rate of 10%. The function then calculates the total amount to repay by adding the interest to the original loan amount, and divides it by the repayment period to get the monthly payment amount.
        interest_rate=0.05
    else:
        # if the client is not a member of the cooperative, they get a higher interest rate of 10%. The function then calculates the total amount to repay by adding the interest to the original loan amount, and divides it by the repayment period to get the monthly payment amount.
        interest_rate=0.1
    total_amount_to_repay=loan_amount+(loan_amount*interest_rate)
    monthly_payment=total_amount_to_repay/repayment_period
    return total_amount_to_repay, monthly_payment

# the second function calculates the amount expected at that paricular time based on the monthly payment and the number of months the client has been active
def calculate_expected_amount(monthly_payment,month_active):
    expected_amount_paid_by_now=monthly_payment*month_active
    return expected_amount_paid_by_now

# the function determines the risk level of the client
def get_risk_status(amount_paid,expected_amount_paid_by_now):
    # if the amount paid is at least 90% of the expected amount, the client is on track
    if amount_paid>=expected_amount_paid_by_now*0.9:
        return "On Track"
    # if the amount paid is between 60% and 90% of the expected amount, the client is at risk
    elif amount_paid>=expected_amount_paid_by_now*0.6:
        return "At Risk"
    # if the amount paid is less than 60% of the expected amount, the client is in critical status
    else:
        return "Critical"

