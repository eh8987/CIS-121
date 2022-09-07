#getting an input and turning it into a float
#income = float(input("Please enter your income: "))


#checks to see if u rich
#if income > 450000:
   # print("Damn u rich")
#else:
   # print("You got it")







#lets me use a random number
import random

#sets the random number
answer = random.randint(1,10) 
#This is the variable to determine if you ran out of turns.
limit = 0

#while loop to check if you have a turn left or not.
while limit < 3:

    #gets input from user

    guess = int(input("Enter a guess 1-10: "))

    #checks to see fi you won or not
    if answer == guess:
        print("you win")
        limit = 5
    else:
        print("Wrong!")
        limit += 1




