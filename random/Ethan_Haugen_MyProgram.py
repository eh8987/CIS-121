import Ethan_Haugen_Stats




file = open("500DayFruitData (1).txt",'r')

print(file)

#Getting the lines and separtings them by /n
data = file.read().splitlines()
#gets rid of first line
data.pop(0)


#lists to put data into 
apple_tracker = []
banana_tracker = []
strawberry_tracker = []


#finds all the fruits and separtates them into their own lists.
for item in data:
    temp = (item.split())
    if temp[1] == "apple":
        apple_tracker.append(int(temp[2]))

for item in data:
    temp = (item.split())
    if temp[1] == "banana":
        banana_tracker.append(int(temp[2]))


for item in data:
    temp = (item.split())
    if temp[1] == "strawberry":
        strawberry_tracker.append(int(temp[2]))






#grabs output from the functions from the stats file
applemean = round( Ethan_Haugen_Stats.mean(apple_tracker),2)
applemedian = round(Ethan_Haugen_Stats.median(apple_tracker),2)

bananamean = round( Ethan_Haugen_Stats.mean(banana_tracker),2)
bananamedian = round(Ethan_Haugen_Stats.median(banana_tracker),2)

strawberrymean = round( Ethan_Haugen_Stats.mean(strawberry_tracker),2)
strawberrymedian = round(Ethan_Haugen_Stats.median(strawberry_tracker),2)










#displays results on a different file
with open("Ethan_Haugen_Output.txt",'w') as f:
    f.write(
        


        "APPLES" + "\n" +
        "===================" + "\n"
        " " +"\n"+


        "The mean number of apples is "+ str(applemean) +"\n"+ 
        "The median number of apples is " + str(applemedian) +"\n"
        " " +"\n"+


        "BANANAS" + "\n" +
        "===================" + "\n"
        " " +"\n"+


        "The mean number of banana is "+ str(bananamean) +"\n"+ 
        "The median number of banana is " + str(bananamedian) + "\n"
        " " +"\n"+

        "STRAWBERRIES" + "\n" +
        "===================" + "\n"
        " " +"\n"+


        "The mean number of strawberry is "+ str(strawberrymean) +"\n"+
         "The median number of strawberry is " + str(strawberrymedian) 
    
    

    
    
    )
    