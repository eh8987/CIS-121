#Ethan Haugen
#Lab 4

#This gets input from the user and sets it to the variable upper.
upper = int(input("Enter an upper bound for a check: "))

#These variables are used for the first loop.
count2 = 0
loop = True

#These variables are used in the second loop.
number= 0
y = 0

#These allow the program to add and keep track of the numbers.
deficient = 0
proper = 0
abundant = 0

#The first loop is used to find every number within the limit the user set.
while loop == True:
    
    #Used to stop the loop.
    count2 += 1

    #Uses the count to pick the number the second loop will use.
    number = count2

    #Resets the count for the next loop.
    count = 0

    while count + 1 < number:
        count+=1
        
        #Finds what is divisible from the number.
        if number % count == 0:
            
            #Adds all of the number that are divisible.
            y += count

    #Checks to see if it is any of these and then adds the point to that variable.
    if y < number:
        deficient += 1
    elif y > number:
        abundant += 1
    else:
        proper += 1
        
    #Resets y
    y = 0

    #Ends loop
    if count2 == upper:
        loop = False



#finished product
print("deficient:", deficient)
print("proper:", proper)
print("abundant:", abundant)
