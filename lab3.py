#LorryWei
#104952078

#
#Example Display the denominations of the coins that should be used to give that
#amount of change to the shopper.



#PsuedoCode Begin:
#
#Obtain the # of Cents by the user
#Convert toonies loonies quarters... to Cents
#Divide the total cents to each unit from top-down, if divisible, calculate the remainder.
#if not divisible, skip the unit and continue.
#Display the result.

#
#PsuedoCode End.


#prompt the input required by the user and store in the cents int variable
temp = input("Number of cents: ")
cents = int(temp)
#initialize all variable to 0
t = int(0)
l = int(0)
q = int(0)
d = int(0)
n = int(0)
p = int(0)
#using floor dividing and remainder calculation to calculate all the change.
if cents >= 200:
    t = cents // 200
    cents = cents % 200
if cents >= 100:
    l = cents // 100
    cents = cents % 100
if cents >= 25:
    q = cents // 25
    cents = cents % 25
if cents >= 10:
    d = cents // 10
    cents = cents % 10
if cents >= 5:
    n = cents // 5
    cents = cents % 5
if cents >= 1:
    p = cents // 1
    cents = cents % 1
#print all the results.
print(t,"tonnies\n")
print(l,"loonies\n")
print(q,"quarters\n")
print(d,"dimes\n")
print(n,"nickels\n")
print(p,"pennies\n")
    
