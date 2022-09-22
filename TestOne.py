#Ethan Haugen
#Exam 1
#9/21/2022

#1


#1 a:
#The second line will not work because it is asking for a int but it will get a str. 
#The correct line would look like 
#age = int(input("Please enter your age: "))

#1 b:
#This loop would go forever, and to fix it you would have to add 1 to number everytime it goes through the loop


#1 c:
#This code works

#1 d:
#This code works

#1 e:
#This code will not work because it needs to ask the user for a int instead of a str.
#The correct line would look like
#user_number = int(input("Please enter a number: "))



#2:

#varaibles for the products
milk = int(input("How many gallons of milk would you like?: "))
eggs = int(input("How many eggs would you like?: "))
bacon = int(input("How much bacon would you like?: "))


#calculations for the price
cost = round(((milk*2)+(eggs*1.5)+(bacon*3)),2)
tax = round( cost * .11,2)

total = round(cost + tax,2)

#recipt 
print(milk ,"Milk - $" , milk*2)
print(eggs ,"Eggs - $" , eggs*1.5)
print(bacon ,"Bacon - $" , bacon*3)

print("- - - - - - ")

print("Cost - $" , cost)
print("Tax - $", tax)
print("Total  - $" , total)

print("- - - - - - ")

print("Thank you for shopping at my awesome store")



#3

phone = (input("phone: "))

#I dont even know why this doesn't work
#print( "(" ,phone[0,2] , ")" ,phone[3,5], "-" ,phone[6,9])



#4


#Lets me use the random function
import random



count = 0
loop = True


while loop == True:

    #makes a random number from 1 - 60
    number = random.randint(1,61)
    
    
    #Checks to see if that number is a divisor of 48
    if 48%number == 0:
        count+=1
        
        #Checks if number is greater or equal to 15, if not checks to see if it is even.
        if number >= 15:
            print("I generated the number", number ,"randomly")

        elif number%2==0:
            print(number)
    
    #shuts off once it finds 10 numbers.
    if count == 10:
        loop = False
        
print("-----")


#idk if you wanted actual random number, but here is a for loop as well. It does the same thing
for i in range(1,61):
    
    if 48%i == 0:
        #Checks if number is greater or equal to 15, if not checks to see if it is even.
        if i >= 15:
            print("I generated the number", i ,"randomly")

        elif i%2==0:
            print(i)
    
