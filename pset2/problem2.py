def debt(balance, anInterest):
    mInterest = anInterest / 12.0
    min_payment = 0
    while True:
        newBalance = balance
        for i in range(1, 13):
            unp_balance = newBalance - min_payment
            newBalance = unp_balance + (mInterest * (unp_balance))
        if newBalance <= 0:
            break
        else:
            min_payment += 10

    return min_payment


print('Lowest Payment: ' + str(debt(balance, annualInterestRate)))    