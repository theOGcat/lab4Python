#LorryWei
#104952078

#Assignment3 Question1
#Example of using function randrange(). Simulates roll of two dices.
#The random module function are given below. The random module contains some very useful functions
#one of them is randrange()
#randrange(start,stop)



#PsuedoCode Begin:
#
#import randrange function from random.
#define funtion that print out each dice.
#in the main function. using randrange(1,7) to simulate giving a random number between 1 and 7
#
#PsuedoCode End.

from random import randrange
import random

def numDice(dice):
    if dice==1:
        print('+-------+')
        print('|       |')
        print('|   *   |')
        print('|       |')
        print('+-------+')
    elif dice==2:
        print('+-------+')
        print('|   *   |')
        print('|       |')
        print('|   *   |')
        print('+-------+')
    elif dice==3:
        print('+-------+')
        print('|      *|')
        print('|   *   |')
        print('|*      |')
        print('+-------+')
    elif dice==4:
        print('+-------+')
        print('|*     *|')
        print('|       |')
        print('|*     *|')
        print('+-------+')
    elif dice==5:
        print('+-------+')
        print('|*     *|')
        print('|   *   |')
        print('|*     *|')
        print('+-------+')
    elif dice==6:
        print('+-------+')
        print('| * * * |')
        print('|       |')
        print('| * * * |')
        print('+-------+')


for x in range(0,2):
    dice=random.randrange(1,7)
    numDice(dice)