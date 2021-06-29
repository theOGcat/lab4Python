#LorryWei
#104952078

#Assignment1 Question3
#Example calculation price of loaves of bread entered by the user.



#PsuedoCode Begin:
#
#Obtain the # of Day old bread and fresh loaves by the user
#Convert value returned by the input() function from a string into an integer using the int() function
#Now calculate the total price for each Day old bread and fresh loaves.
#Adding up the Day old bread and fresh loaves to calculate the total price.
#calculate the new total by adding the taxes.
#print out a message telling the user what are the Total price of transaction.

#
#PsuedoCode End.


#prompt the input required by the user and store in the different variables
print("Welcome to Pretend Bakery Windsor, Ontario\n")
temp = input("Please enter the number of fresh loaves you wish to buy:              : ")
valuefr = int(temp)
temp = input ("Please enter the number of old loaves you wish to buy:                : ")
valueold = int(temp)

pricefr = valuefr * 3.49
priceold = valueold *3.49 *0.555

pricetotal = round((pricefr + priceold),2)

valuetax = pricetotal*0.13

totalPrice = pricetotal + valuetax

#print all the results.
#Using string formatter to format the output exactly two digits.



print("\nDiscounted price for old loaves                   : $","%0.2f\n"%priceold)
print("Intermediate total                                : $","%0.2f\n"%pricetotal)
print("HST                                               : $","%0.2f\n"%valuetax)
print("Total Price of transaction                        : $","%0.2f\n"%totalPrice)
print("Thank you for your Business :)")
