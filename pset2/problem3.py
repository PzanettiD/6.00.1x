def debt(balance, anInterest):
    mInterest = anInterest / 12.0
    lowBound = balance / 12
    upBound = (balance * ((1 + mInterest) ** 12)) / 12.0
    while True:
        min_payment = (lowBound + upBound) / 2
        newBalance = balance
        for i in range(1, 13):
            unp_balance = newBalance - min_payment
            newBalance = unp_balance + (mInterest * (unp_balance))
        if round(newBalance, 2) == 0:
            break
        else:
            if newBalance > 0:
                lowBound = (lowBound + upBound) / 2
            else:
                upBound = (lowBound + upBound) / 2

    return round(min_payment, 2)

print(debt(balance, annualInterestRate))