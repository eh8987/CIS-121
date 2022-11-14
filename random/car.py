class Car:

    def __init__(self,number_of_wheels,engine,model,year):
        self.number_of_wheels = number_of_wheels
        self.engine = engine
        self.model = model
        self.year = year

    
    def __str__(self):
       
        print(
            "============= Car Info ==============" + "\n"
            "------------------------------------------"  + "\n"
            
            "Number of Wheels : " + str(self.number_of_wheels) + "\n"
            "------------------------------------------"  + "\n"
            "Engine           : " + str(self.engine) + "\n"
            "------------------------------------------"  + "\n"
            "Model            : " + str(self.model) + "\n"
            "------------------------------------------"  + "\n"
            "Year             : " + str(self.year) + "\n"
        
    
        )
        

        return " "


    def changeYear(self,new_year):
        self.year = new_year


