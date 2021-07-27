#LorryWei
#104952078

#lab9
#Example program that calculate the factorial n! , n! is the product of all positive
#integers less than or equal to n
#for example, 5! = 5*4*3*2*1 = 120
#The value of 0! is 1
#



#PsuedoCode Begin:
#
#using for loops
#for i = 1; i <=n ++1
#factorial *= i
#print out the list that from the factorial
#
#PsuedoCode End.

numList = []
f = 1
n = int(input("Please enter a positive integer between 1 and 20: "))
if (n == 0):
    print("j = ",0,";"," ",0,"! = ",1)  
    numList.append(1)
elif (n > 20 or n < 0):
    print("The number entered is out of range.")
    exit(0)

for j in range(1,n+1):
    f = f*j
    numList.append(f)
    print("j = ",j,";"," ",j,"! = ",f)   
print("factorial_list = ",numList)     
