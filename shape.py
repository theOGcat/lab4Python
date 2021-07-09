#LorryWei
#104952078

#Assignment2 Question2
#Example Display the determines the name of a shape from its number of sides.
#The program should support shapes with anywhere from 3 up to (and including) 10 sides
#If a number of sides outside of this range is entered then the program should display an appropriate error message.



#PsuedoCode Begin:
#
#Obtain the number of sides by Users
#Using def than if and elif to achieve the if statement
#
#PsuedoCode End.

numSide = int(input("Enter the number of sides: "))
def num_to_string(numSide):
    numSides = {
        3: "That's a triangle",
        4: "That's a quadrilateral",
        5: "That's a pentagon",
        6: "That's a hexagon",
        7: "That's a heptagon",
        8: "That's octagon",
        9: "That's a nonagon",
        10: "That's a decagon",
    }
    return numSides.get(numSide,"That number of sides is not supported by this program")
print (num_to_string(numSide))
