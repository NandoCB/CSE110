print('Qualifying for a Loan')

print('Ingrese una calificación del 1 al 10 en lo siguiente:')

large_loan = int(input('How large is the loan? '))

credit_history = int(input('How good is your credit history? '))

income = int(input('How high is your income? '))

down_payment = int(input('How large is your down payment? '))

approved_credit = False


if large_loan >= 5:
    if credit_history >= 7 and income >= 7:
        approved_credit = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            approved_credit = True
        else:
            approved_credit = False
    else:
        approved_credit = False
else:
    if large_loan < 4:
        approved_credit = False
    else:
        if income >=7 or down_payment >= 7:
            approved_credit = True
        elif  income >= 4 and down_payment >= 4:
            approved_credit = True
        else:
            approved_credit = False





if approved_credit:
    print('su credito fue aprobado')

else:
    print('Su credito no a sido aprobado')