
class Employee:

    def __init__(self,wage,hours,position,name):
        self.wage = wage
        self.hours = hours
        self.position = position
        self.name = name

    


    def changeWage(self,newWage):
        self.wage = newWage

    def changeHours(self,newHours):
        self.hours = newHours

    def changePosition(self,newPosition):
        self.position = newPosition




    def salary(self):
        salary = (self.hours * self.hours) * 52
        return salary



            
    def __str__(self):
       
        print(
            "============= Employee Info ==============" + "\n"
            "------------------------------------------"  + "\n"
            
            "Name                : " + str(self.name) + "\n"
            "------------------------------------------"  + "\n"
            "Hourly Pay          : " + str(self.wage) + "\n"
            "------------------------------------------"  + "\n"
            "Hours Worked Weekly : " + str(self.hours) + "\n"
            "------------------------------------------"  + "\n"
            "Position            : " + str(self.position) + "\n"
            "------------------------------------------"  + "\n"
            "Salary              : " + str(self.salary()) + "\n"
            "------------------------------------------"  + "\n"
            "------------------------------------------"  + "\n"
            "------------------------------------------"  + "\n"

    
        )
        
        return ""