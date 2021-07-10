#LorryWei
#104952078

#lab7
#Example program that reads integers from the user until a blank line is entered (or ask the user to enter Q to quit)
#x = input("Enter an integer(Q to quit):")
#Once all of the integers have been read your program should display all of the negative numbers, followed by all of the zeros
#followed by all of the positive numbers. Within each group the numbers should be displayed in the same order that they were entered by the user
#



#PsuedoCode Begin:
#
#prompt the users with input of list of integers.
#Using while loop or for loops to loop through all the integers in the list.
#Sort the number from Low to high orders.
#Print all the number on the consonle from Low to high orders.
#
#PsuedoCode End.

numList = []
temp = 0
while (temp != "Q"):
    temp = input("Enter an interger(Q to quit) ")
    if temp == "Q":
        continue
    numList.append(int(temp))

print("\nEntered Numbers: "+ str(numList))
numList.sort()
print("Sorted Numbers: " + str(numList) + " (Low to High)")

