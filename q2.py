#LorryWei
#104952078

#Assignment1 Question2
#Example Display the equivalent amount of centimeters convert from distance in feet.



#PsuedoCode Begin:
#
#Obtain the # of feet by the user
#Convert value returned by the input() function from a string into an integer using the int() function
#Now convert this value into centimeters - this can be done by converting the foot to inches, and then convert inches to centimeters
#print out a message telling the user what the feet are in centimeters.

#
#PsuedoCode End.


#prompt the input required by the user and store in the cents int variable
temp = input("Please enter the # of feet to be converted: ")
valuefeet = int(temp)

#Using multiplying the kilometre to convert
valuecm = valuefeet * 12 * 2.54
#print all the results.
#Using string formatter to format the output exactly three digits.
valuecm = round(valuecm,3)
print("The equivalent centimeters is:","%.2f"%valuecm)
