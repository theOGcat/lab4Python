#LorryWei
#104952078

#lab4
#Example Display the equivalent amount of time in the form D:HH:MM:SS where D,HH
#MM, and SS represent days, hours, minute and second respectively.



#PsuedoCode Begin:
#
#Obtain the # of Cents by the user
#Convert second... to Days,Hours,Minutes, and seconds.
#Divide the total cents to each unit from top-down, if divisible, calculate the remainder.
#if not divisible, skip the unit and continue.
#Display the result.

#
#PsuedoCode End.


#prompt the input required by the user and store in the cents int variable
temp = input("Enter a number of seconds: ")
seconds = int(temp)
#initialize all variable to 0
dt = int(0)
ht = int(0)
mt = int(0)
st = int(0)
#using floor dividing and remainder calculation to calculate all the change.
if seconds >= 86400 :
    dt = seconds // 86400
    seconds = seconds % 86400
if seconds >= 3600:
    ht = seconds // 3600
    seconds = seconds % 3600
if seconds >= 60 :
    mt = seconds // 60
    seconds = seconds % 60
if seconds >= 1:
    st = seconds // 1
    seconds = seconds % 1

#print all the results.
#Using string formatter to format the output exactly two digits.
print("The equivalent duration is ","%02d:"%dt,"%02d:"%ht,"%02d:"%mt,"%02d."%st)



