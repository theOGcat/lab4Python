#LorryWei
#104952078

#lab5
#Example Display the equivalent amount of Metric length converting from U.S Customary System length
#in miles,yards,feet.



#PsuedoCode Begin:
#
#Obtain the # of miles,yards,feet,inches by the user
#After the numbers of miles, yards, feet, and inches are entered, the length should be converted entirely to inches
#and then divided by 39.37 to obtain the value in meters. The int function should be used to break the total number of meters
#into a whole number of kilometers and meters. The number of centimeters should be displayed to on decimal place.
#

#
#PsuedoCode End.


#prompt the input required by the user and store in the different int variable
temp = input("Enter number of miles: ")
numMiles = int(temp)
temp = input("Enter number of yards: ")
numYards = int(temp)
temp = input("Enter number of feet:  ")
numFeet = int(temp)
temp = input("Enter number of inches: ")
numInches = int(temp)
#initialize all the variables
totalm = int(0)
totalkm = int(0)
#convert the total inches to total centimeters.
totalInches = 63360 * numMiles + 36 * numYards + 12 * numFeet + numInches
totalcm = round((totalInches /39.37 * 100),1)
#divided the total cm to km and m respectively.
if totalcm >= 100000 :
    totalkm = totalcm // 100000
    totalcm = totalcm % 100000
if totalcm >= 100:
    totalm = totalcm // 100
    totalcm = totalcm % 100

#print all the results.
#Using string formatter to format the output exactly one digits for centimeters.
print("Metric length:")
print("     %d kilometers"%totalkm)
print("     %d meters"%totalm)
print("     %0.1f centimeters"%totalcm)
