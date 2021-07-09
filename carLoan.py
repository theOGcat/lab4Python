#LorryWei
#104952078

#Assignment2 Question1
#Example Display the result of calculated Monthly payment of Car Loan.
#monthly payment is given by
#monthly payment = i/1-(1+i)^-12n * A



#PsuedoCode Begin:
#
#Obtain the # of loan by the User.
#Obtain the # of interest rate% by Users
#Obtain the # of Years by Users.
#Calcualte the # of Monthly payment by given formula.
#
#PsuedoCode End.

loanAmount = int(input("Enter amount of loan : "))
interestRate = float(input("Enter interest rate (%): " ))
numYear = int(input("Enter number of years: "))

monthlyPay = 0
i = interestRate/1200
monthlyPay = (i*loanAmount)/(1-(1+i)**(-12*numYear))
print("Monthly payment: $","%.2f"%monthlyPay)
