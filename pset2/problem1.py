def debt(balance, aninterest, mpayment):
    for i in range(1, 13):
        min_payment = balance * mpayment
        unp_balance = balance - min_payment
        interest = (aninterest / 12.0) * unp_balance
        balance = unp_balance + interest
    return round(balance, 2)

print('Remaining balance: ' + str(debt(balance, annualInterestRate, monthlyPaymentRate)))    