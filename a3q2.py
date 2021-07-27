#LorryWei
#104952078

#Assignment3 Question2
#The above code works and is correct. What would be the output of the code and why
#Please try to trace the program.
#The answer should be uploaded in a pdf file in the correct area on BB

def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
        print("*"*value)
    return y
print(mystery([1,2,3,4,5]))
print(mystery([0,6,2,4]))