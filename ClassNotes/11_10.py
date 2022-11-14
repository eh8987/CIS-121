


class Company:
    def __init__(self,name,year):
        self.name = name
        self.year = year




class Car:

    def __init__(self,wheels,company,color,miles,status,speed):
        
        self.wheels = wheels
        self.company = company
        self.color = color
        self.miles = miles
        self.status = status
        self.speed = speed



    def accelerate(self,amount):
        self.status = "Moving"
        self.speed += amount
        self.updateMiles(amount)
        

    def stop(self):
        self.speed = 0 
        self.status = "Stopped"

    def decrease(self):
        self.speed -= 20

        if self.speed < 0:
            self.speed = 0

        self.status = "Slowing Down"
        
    def updateMiles(self,amount):
        self.miles += amount
        
    def displayMiles(self):
        print(f"Your current miles are: {self.miles}")


def speedster():


    import random


    testCar = Car(4,"Fast asf car builders","pink",100000000,"Stopped",0)
    count = 0

    while True:


        count += 1

        accel = random.randint(0,30)


        testCar.accelerate(accel)

        if testCar.speed > 60:
            return count
            



print(f"Your car hit 60mph in {speedster()} seconds!")
