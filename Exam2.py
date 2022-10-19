#Ethan Haugen
#Exam 2
#10/19/2022


#Question 1


list = 2,154,152,3,2,5,3

def oddeven(list):
    
    temp = {}   

    odd=[]      #For adding to temp
    even=[]



    for i in list:    #runs through the list and decides if it can be divided by two or not
        if i%2==0:
            even.append(i)  #adds to list
        else:
            odd.append(i)

    temp["even"] = even    #adds those lists to a dictionary
    temp["odd"] = odd

    return temp

def printfile(data):

    

    with open("Results.txt","w") as f:    #opens a new file and writes the information 
        f.write(
            "Even : " + str(data["even"])  + "\n"
            "Odd : " + str(data["odd"])


        )

printfile(oddeven(list))


#Question 2

import random

def listgen():      
    list1 = []            

    for i in range (200):                      #picks two-hundred random numbers and puts it into a list
        list1.append(random.randint(0,100))

    return list1


def counter(list1,list2): 
   
    temp = {}   
   
    for x in list1:    #goes through all the numbers in list 1
        if x in temp:           # checks if that number is already there, if it is it will add to the existing one
                                
            temp[x] += 1
        else:                   # if not, it will great a new one
            temp[x] = 1
    for y in list2:
        if y in temp:
            temp[y] += 1
        else:
            temp[y] = 1
    
    with open("RESULTS4.TXT","w") as f:   # writes the results on a file
        f.write(str(temp))


counter(listgen(),listgen()) 


#question 3


def findAverage():
                                                #This took so long :(
    file =  open("steps.txt","r")           #opens file and turns it into something I can use
    data = file.read().splitlines()



    janDays = 31                     #idk how many days are in each month so i made it changable 
    febDays = 28
    marchDays = 31
    aprilDays = 30
    mayDays = 30
    juneDays = 31
    julyDays = 30
    augDays = 31
    sepDays = 31
    octDays = 31
    novDays = 30
    decDays = 31



    janTotal = 0                    
    jan = 0

    for i in range (0,janDays):
        janTotal += int(data[i])   #adds all values from 0 to how ever many days are in january 
        jan = janTotal/janDays    #finds average
        

    for i in range (0,janDays):
        data.pop(i)                       #deletes those values already used

    febTotal = 0
    feb = 0

    for i in range (0,febDays):
        febTotal += int(data[i])
        feb = febTotal/febDays
        

    for i in range (0,febDays):
        data.pop(i)

    marchTotal = 0
    march = 0

    for i in range (0,marchDays):
        marchTotal += int(data[i])
        march = marchTotal/marchDays
        
    for i in range (0,marchDays):
        data.pop(i)

    aprilTotal = 0
    april = 0

    for i in range (0,aprilDays):
        aprilTotal += int(data[i])
        april = aprilTotal/aprilDays
        
    for i in range (0,aprilDays):
        data.pop(i)

    mayTotal = 0
    may = 0

    for i in range (0,mayDays):
        mayTotal += int(data[i])
        may = mayTotal/mayDays
        

    for i in range (0,mayDays):
        data.pop(i)
    juneTotal = 0
    june = 0

    for i in range (0,juneDays):
        juneTotal += int(data[i])
        june = juneTotal/juneDays
        

    for i in range (0,juneDays):
        data.pop(i)
    julyTotal = 0
    july = 0

    for i in range (0,julyDays):
        julyTotal += int(data[i])
        july = julyTotal/julyDays
    for i in range (0,julyDays):
        data.pop(i)

    augTotal = 0
    aug = 0

    for i in range (0,augDays):
        augTotal += int(data[i])
        aug = augTotal/augDays
    for i in range (0,augDays):
        data.pop(i)

    sepTotal = 0
    sep = 0

    for i in range (0,sepDays):
        sepTotal += int(data[i])
        sep = sepTotal/sepDays
    for i in range (0,sepDays):
        data.pop(i)

    octTotal = 0
    octo = 0

    for i in range (0,octDays):
        octTotal += int(data[i])
        octo = octTotal/octDays
    for i in range (0,octDays):
        data.pop(i)
        
    novTotal = 0
    nov = 0

    for i in range (0,novDays):
        novTotal += int(data[i])
        nov = novTotal/novDays
    for i in range (0,novDays):
        data.pop(i)
    decTotal = 0
    dec = 0

    for i in range (0,decDays):
        decTotal += int(data[i])
        dec = decTotal/decDays


 # prints everything
    with open("month.txt","w") as f:
        f.write(
            "Month     | " + "Average Steps" + "\n"
            "=======================" + "\n"
            "January   | " + str(round(jan,2)) + "\n"
            "Febuary   | " + str(round(feb,2)) + "\n"
            "March     | " + str(round(march,2)) + "\n"
            "April     | " + str(round(april,2)) + "\n"
            "May       | " + str(round(may,2)) + "\n"
            "June      | " + str(round(june,2)) + "\n"
            "July      | " + str(round(july,2)) + "\n"
            "August    | " + str(round(aug,2)) + "\n"
            "September | " + str(round(sep,2)) + "\n"
            "October   | " + str(round(octo,2)) + "\n"
            "November  | " + str(round(nov,2)) + "\n"
            "December  | " + str(round(dec,2)) + "\n"






        )

findAverage()