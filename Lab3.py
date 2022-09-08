"""
Ethan Haugen
9/8/2022

This program finds out how much the user owes in taxes.
"""
import sys
from traceback import print_stack


taxOwed = 0.0

earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")


#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")




# Your code goes here



#These two sets of if statements first check to see if you are married or single.
if maritalStatus == "m":

    #These if and elif statements check to were your income lands on the chart. It then calculates the amount of taxes you owe.
    if earnedIncome >= 0 and earnedIncome <= 19900:
        taxOwed =  earnedIncome * .10
    elif earnedIncome >= 19901 and earnedIncome <= 81050:
        taxOwed =  earnedIncome * .12
    elif earnedIncome >= 81051 and earnedIncome <= 172750:
        taxOwed =  earnedIncome * .22
    else:
        print("You are too rich for me!")

if maritalStatus == "s":
    
    #These if and elif statements check to were your income lands on the chart. It then calculates the amount of taxes you owe.
    if earnedIncome >= 0 and earnedIncome <= 9950:
        taxOwed =  earnedIncome * .10
    elif earnedIncome >= 9951 and earnedIncome <= 40525:
        taxOwed =  earnedIncome * .12
    elif earnedIncome >= 40526 and earnedIncome <= 86375:
        taxOwed =  earnedIncome * .22
    else:
        print("You are too rich for me!")


#This prints the output of the program and tells the user how  much they owe in taxes for the year.
print ("You have to pay $" ,taxOwed, "in taxs!")
