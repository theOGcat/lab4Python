#LorryWei
#104952078

#Assignment1 Question1
#Example Display the equivalent amount of miles convert from distance in kilometres.



#PsuedoCode Begin:
#
#Obtain the # of kilometres by the user
#Convert value returned by the input() function from a string into an integer using the int() function
#Now convert this value into miles - this can be done by Multiplying the kilometres by 0.6214
#print out a message telling the user what the kilometres are in miles.

#
#PsuedoCode End.


#prompt the input required by the user and store in the valuekilo int variable
temp = input("Please enter the kilometres to be converted. ")
valuekilo = int(temp)

#Using multiplying the kilometre to convert
valuemiles = valuekilo * 0.6214
#print all the results.
#Using string formatter to format the output exactly three digits.
valuemiles = round(valuemiles,3)
print("The equivalent miles is:","%.3f"%valuemiles)
