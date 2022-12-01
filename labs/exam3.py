#Ethan Haugen
#11/22/2022
#Exam 3


#I worked with Apu




#Question 1




class Vehicle:       #First parent class


    #Creates variables

 
    def __init__(self,numPassengers,manufacturer,numWheels):
        self.numPassengers = numPassengers
        self.manufacturer = manufacturer
        self.numWheels = numWheels


    

#Next two classes are child classes to Vehicle

class Automobile(Vehicle): 

    def __init__(self,numPassengers,manufacturer,numWheels,mpg,model,numDoors):
        super().__init__(numPassengers,manufacturer,numWheels) #gives the needed variables to vehicle
        self.mpg = mpg
        self.model = model
        self.numDoors = numDoors


class TwoWheeler(Vehicle):

    def __init__(self,numPassengers,manufacturer,numWheels,model,weight):
        super().__init__(numPassengers,manufacturer,numWheels) #gives the needed variables to vehicle
        self.model = model
        self.weight = weight


#Next two classes are child classes to Vehicle

class Sedan(Automobile):

    def __init__(self,numPassengers,manufacturer,numWheels,mpg,model,numDoors,type,numCylinders,horsepower):
        super().__init__(numPassengers,manufacturer,numWheels,mpg,model,numDoors) #gives the needed variables to Automobile
        self.type = type
        self.numCylinders = numCylinders
        self.horsepower = horsepower


class Truck(Automobile):

    def __init__(self,numPassengers,manufacturer,numWheels,mpg,model,numDoors,type,numAxels,maxTowPayload):
        super().__init__(numPassengers,manufacturer,numWheels,mpg,model,numDoors) #gives the needed variables to Automobile
        self.type = type
        self.type = type
        self.numAxels = numAxels
        self.maxTowPayload = maxTowPayload


#Next two classes are child classes to TwoWheeler

class Motorcycle(TwoWheeler):

    def __init__(self,numPassengers,manufacturer,numWheels,model,weight,type,mpg,horsepower):
        super().__init__(numPassengers,manufacturer,numWheels,model,weight)  #gives the needed variables to TwoWheeler
        self.type = type
        self.mpg = mpg
        self.horsepower = horsepower


class Bicycle(TwoWheeler):

    def __init__(self,numPassengers,manufacturer,numWheels,model,weight,hasGears,hasSuspension,wheelSize):
        super().__init__(numPassengers,manufacturer,numWheels,model,weight)  #gives the needed variables to TwoWheeler
        self.hasGears = hasGears
        self.hasSuspension = hasSuspension
        self.wheelSize = wheelSize






#Question 2


#from the diagram in question one, I can see that there is a parent class with two children
#And both of those child classes are parent classes to two more classes.
#None of these classes have any methods.




#Question 3

class Customer:

    #sets variables
    def __init__(self,spending):
        self.spending = spending
        
    def discount(self):   #This is ran when a discount is activated
        print("====================================================")
        print(f"Thanks for your purchase, your total is ${self.cost}")
        print("You received a $10 dollar discount on your puchase")
        print(f"You your purchases comes to: ${self.cost - 10}")
        print("====================================================")



    def makePurchase(self,cost):
        self.cost = cost       
        self.spending += cost  #adds cost of purchase to total spending

        if self.spending >= 100:     #checks to see if spending is over $100 and gives discount if so.
            self.discount()    
        else:      #if otherwise it prints the orginal cost
            print("====================================================")
            print(f"Thanks for your purchase, your total is ${cost}")
            print("====================================================")

#Using the class in an example

Ethan = Customer(90)   #Creates a customer with $90 in spending already
Ethan.makePurchase(9)   #Makes a purchase for $9, this doesn't give a discount

Ethan.makePurchase(15)  #Makes another purchase that gives a discount 