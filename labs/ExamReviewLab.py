#Ethan Haugen
#11/17/2022
#Exam Review

#Question 1


#It looks like there's two parents classes, Address being the parent to Person,
#and Person being the parent to both Student and Teacher.
#Address has a handful of variables and methods.
#Person has a few variables.
#Both Student and Teacher have some variables and methods.



#Question 2


#The Address class is a parent class because it is at the top of the chart.
#It is the parent class to Person, indicated by the arrow pointing from Person to Address.

#The Person Class is both a parent class and a child class. 
#As explained before, Person is a child class to Address.
#But now, Person is a parent class to Student and Teacher as well.
#This is indicated with the arrows pointing from Student and Teacher to Person.

#Finally, as explained above, Student and Teacher are the child classes to Person.


#Question 3




class Address:        #First Parent Class

    #Sets Variables

    def __init__(self,street,city,country,zipcode,state):        
        self.street = street
        self.city = city
        self.country = country
        self.zipcode = zipcode
        self.state = state



    #All the methods

    def getAddress(self):
        return self.street , self.city, self.state , self.country , self.zipcode

    def getCity(self):
        return self.city

    def getZipcode(self):
        return self.zipcode

    def getState(self):
        return self.state

    def getCountry(self):
        return self.country


    #Displays Info

    def __str__(self):
        print(

            "=========Home=========" + "\n"
            f"Street: {self.street}" + "\n"
            f"City: {self.city}" + "\n"
            f"State: {self.state}" + "\n"
            f"Country: {self.country}" + "\n"
            f"Zip Code: {self.zipcode}" + "\n"
            "======================" + "\n"
        )

        return ""




class Person(Address): #Parent Class to Student and Teacher, inherits from Address

    #Sets Variables

    def __init__(self,street,city,country,zipcode,state,name,phoneNumber,emailAddress):
        super().__init__(street,city,country,zipcode,state)
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress




    #Displays Info

    def __str__(self):
        print(

            "=========Person=========" + "\n"
            f"Name: {self.name}" + "\n"
            "........................" + "\n"
            f"Street: {self.street}" + "\n"
            f"City: {self.city}" + "\n"
            f"State: {self.state}" + "\n"
            f"Country: {self.country}" + "\n"
            f"Zip Code: {self.zipcode}" + "\n"
            "........................" + "\n"
            f"Phone Number: {self.phoneNumber}" + "\n"
            f"Email Address: {self.emailAddress}" + "\n"
            "========================" + "\n"
        )

        return ""
    

class Student(Person):

    #Sets Variables

    def __init__(self,street,city,country,zipcode,state,name,phoneNumber,emailAddress,studentNumber,gpa):
        super().__init__(street,city,country,zipcode,state,name,phoneNumber,emailAddress)
        self.studentNumber = studentNumber
        self.gpa = gpa

    def getGPA(self):
        return self.gpa

    def getStudentNumber(self):
        return self.studentNumber

    #Displays Info

    def __str__(self):
        print(

            "=========Student=========" + "\n"
            f"Name: {self.name}" + "\n"
            "........................" + "\n"
            f"Street: {self.street}" + "\n"
            f"City: {self.city}" + "\n"
            f"State: {self.state}" + "\n"
            f"Country: {self.country}" + "\n"
            f"Zip Code: {self.zipcode}" + "\n"
            "........................" + "\n"
            f"Phone Number: {self.phoneNumber}" + "\n"
            f"Email Address: {self.emailAddress}" + "\n"
            "........................" + "\n"
            f"Student Number: {self.studentNumber}" + "\n"
            f"GPA: {self.gpa}" + "\n"
            "=========================" + "\n"
        )

        return ""
    
class Teacher(Person):

    #Sets Variables

    def __init__(self,street,city,country,zipcode,state,name,phoneNumber,emailAddress,teacherID,workHours,workRate,yearsOfService):
        super().__init__(street,city,country,zipcode,state,name,phoneNumber,emailAddress)
        self.teacherID = teacherID
        self.workHours = workHours
        self.workRate = workRate
        self.yearsOfService = yearsOfService

    #All the methods

    def getTeacherID(self):
        return self.teacherID

    def getWorkHours(self):
        return self.workHours

    def getWorkRate(self):
        return self.workRate
    
    def getYearsOfService(self):
        return self.yearsOfService

    def calculateYearlySalary(self):
        return self.workHours*self.workRate*52

    #Displays Info

    def __str__(self):
        print(

            "=========Teacher=========" + "\n"
            f"Name: {self.name}" + "\n"
            "........................" + "\n"
            f"Street: {self.street}" + "\n"
            f"City: {self.city}" + "\n"
            f"State: {self.state}" + "\n"
            f"Country: {self.country}" + "\n"
            f"Zip Code: {self.zipcode}" + "\n"
            "........................" + "\n"
            
            f"Phone Number: {self.phoneNumber}" + "\n"
            f"Email Address: {self.emailAddress}" + "\n"
            "........................" + "\n"
            f"Teacher ID: {self.teacherID}" + "\n"
            f"Weekly Work Hours: {self.workHours} Hours" + "\n"
            f"Hourly Pay: ${self.workRate}/Hour" + "\n"
            f"Years of Service: {self.yearsOfService}" + "\n"
            f"Salary: ${self.calculateYearlySalary()}" + "\n"
            "=========================" + "\n"
        )

        return ""

#Main

Home = Address("30th St","Watertown","USA","57201","South Dakota")
Ethan = Person("30th St","Watertown","USA","57201","South Dakota","Ethan Haugen","(123)123-1234","yourmom@gmail.com")
StudentEthan = Student("30th St","Watertown","USA","57201","South Dakota","Ethan Haugen","(123)123-1234","yourmom@gmail.com",123456,4)
TeacherEthan = Teacher("30th St","Watertown","USA","57201","South Dakota","Ethan Haugen","(123)123-1234","yourmom@gmail.com",123456,30,50,100)


print(Home)
print(Ethan)
print(StudentEthan)
print(TeacherEthan)