#LorryWei
#104952078

#Assignment3 Question3
#In Windsor Land, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140
#meters travelled. Write a function that takes the distance travelled (in kilometers) as its only
#parameter and returns the total fare as its only result. Write a program that demonstrates the
#function.



#PsuedoCode Begin:
#
#prompt the user to enter the distance travelled
#define function that calculate the fare based on the distance travelled
#base fee is $4, total fare is the base fare plus the rate mutiply by the meter divided by 140
#
#PsuedoCode End.

dist = int(input("Enter number of Km travelled: "))
def calculateFare(dist):
    basefee = 4
    rate = 0.25
    distMeter = dist*1000
    totalfee = basefee + rate*(distMeter/140)
    print("Your fare is : " + str(round(totalfee,2)) + " dollars")
    return(totalfee)
calculateFare(dist)