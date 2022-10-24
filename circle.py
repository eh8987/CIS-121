class Circle:
    def __init__(self,radius):
        self.radius = radius


    def area(self):
        area = 3.145*(self.radius**2)
        return area


    def perimiter(self):
        perimiter = 2*3.145*self.radius
        return perimiter

    def __str__(self):


        print(

            "========= Circle Stats ==========" + "\n"
            "Area      : " + str(self.area()) + "\n"
            "Perimiter : " + str(self.perimiter()) + "\n"

        )

        return ""