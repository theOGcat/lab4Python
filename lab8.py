#LorryWei
#104952078

#lab8
#Example program that converts the speeds 60 kph through 130 kph(in 10 kph increments) to mph 
#



#PsuedoCode Begin:
#
#write a loop that starting with the variable 60 kph
#convert the current kph variable to mph unit using the formula give
#output the mph unit and increment the kph by 10
#loop end
#
#PsuedoCode End.

kph = 60
mph = 0
print("KPH      MPH")
print("------------")

while (kph <= 130):
    mph = kph* 0.6214
    print(kph,"     ",round(mph,1))
    kph+=10