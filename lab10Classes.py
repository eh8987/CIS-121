
#I couldn't do it, this is what I had.


class Die:
    


    def __init__(self,num_of_dice,sides):
        self.num_of_sides = sides
        self.face_up_value = 1
        self.num_of_dice = num_of_dice
    def roll(self):
        import random
        self.face_up_value = random.randint(1,(self.num_of_sides + 1))
        
        

    def getValue(self):
        return self.face_up_value

    def __add__(self):

        return 
    
    def __gt__():
        return

    def __str__(self):
        print("The current value of the dice is: " + str(self.face_up_value))
        return ""





class Player():
    def __init__(self,name,):
    
        dice06 = Die(6,1)
        dice10 = Die(10,1)
        self.name = name
        self.die06 = dice06.roll()
        self.die10 = dice10.roll()

    def rollDice(self):
        
        self.die06.roll()
        self.die10.roll()
        return 

    def getDiceValue(self):

        
        return

    def __str__():
        return



class HighTwoGame():

    def playOneGame():
        return
    
    def playManyGame():
        return

    def __str__():
        return

