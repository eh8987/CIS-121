class Employee:                   


    def __init__(self,ID,name):
        self.ID = ID
        self.name = name

    

class SalaryEmployee(Employee):


    def __init__(self,ID,name,weeklyrate):
        super().__init__(ID,name) #gives the parent class what it needs
        self.weeklyrate = weeklyrate


    def calculate_payroll(self):
        return self.weeklyrate 
        


    
class HourlyEmployee(Employee):

    def __init__(self,ID,name,hourPay,hours):
        super().__init__(ID,name)
        self.hourPay = hourPay
        self.hours = hours


    def calculate_payroll(self):
        return self.hourPay * self.hours

    
    

class CommissionEmployee(SalaryEmployee):
    
    def __init__(self,ID,name,weeklyrate,commission):
        super().__init__(ID,name,weeklyrate)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission


class IPayrollCalculator:
    

   
    def printCommissionInfo(self,commission_employee):
        print("===========Commisison Employee===============")
        print(f"Name: {commission_employee.name}")
        print(f"ID: {commission_employee.ID}")
        print(f"Weekly Rate: {commission_employee.weeklyrate}")
        print(f"Weekly Commission: {commission_employee.commission}")
        print(f"This Weeks Pay: {commission_employee.calculate_payroll()}")
        
        
    def printSalaryInfo(self,salary_employee):
        print("===========Salary Employee===============")
        print(f"Name: {salary_employee.name}")
        print(f"ID: {salary_employee.ID}")
        print(f"Weekly Rate: {salary_employee.weeklyrate}")
        print(f"This Weeks Pay: {salary_employee.calculate_payroll()}")
        
    def printHourlyInfo(self,hourly_employee):
        print("===========Hourly Employee===============")
        print(f"Name: {hourly_employee.name}")
        print(f"ID: {hourly_employee.ID}")
        print(f"Pay Per Hour: {hourly_employee.hourPay}")
        print(f"Hours worked: {hourly_employee.hours}")
        print(f"This Weeks Pay: {hourly_employee.calculate_payroll()}")
        
    
    def run(self):

        




        name = input("Please enter name: ")
        ID = input("please enter ID: ")
        EmployeeType = input("please enter employee type: ")



        if EmployeeType == "Commission":



            weeklyrate = int(input("Please enter weekly rate: "))
            commission = int(input("Please enter commission: "))


            commission_employee = CommissionEmployee(ID,name,weeklyrate,commission)


            self.printCommissionInfo(commission_employee)


        elif EmployeeType == "Salary":



            weeklyrate = int(input("Please enter weekly rate: "))
            


            salary_employee = SalaryEmployee(ID,name,weeklyrate)


            self.printSalaryInfo(salary_employee)

        elif EmployeeType == "Hourly":



            hourPay = int(input("Please enter how much you get paid an hour: "))
            hours = int(input("Please enter your hours worked: "))


            hourly_employee = HourlyEmployee(ID,name,hourPay,hours)


            self.printHourlyInfo(hourly_employee)

    
        else:
            pass