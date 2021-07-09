#LorryWei
#104952078

#Assignment2 Question3
#Example Display the translation the word into Pig Latin.
#If the word begins with a group of consonants, move them to the end of the word and add ay.
#If the word begins with a vowel, add way to the end of the word. For instance, else vecomes elseway.



#PsuedoCode Begin:
#
#Obtain the String before the translation by users.
#Using if statement to tell if the string starting with a consonants or vowel.
#if it is consonants, move the group of consonants to the end and add ay
#if it is vowel, add way to the end of the word.
#
#PsuedoCode End.

flag = 0
string1 = input("Enter word to translate: ")
str(string1)
for index,element in enumerate(string1):
    if (element == "a" or element == "e" or element == "i" or element == "o" or element == "u" or element == "A" or element == "E" or element == "I" or element == "O" or element == "U") and flag == 0:
        print(string1 + "way")
        break
       
    else:
        flag =1
        index = 0
        if string1[index] == "a" or string1[index] == "e" or string1[index] == "i" or string1[index] == "o" or string1[index] == "u" or string1[index] == "A" or string1[index] == "E" or string1[index] == "I" or string1[index] == "O" or string1[index] == "U":
            print(string1 + "ay")
            break
        else:
            string1 = string1[1:] + string1[0]
            continue
       
    
