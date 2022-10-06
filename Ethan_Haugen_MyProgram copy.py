import Ethan_Haugen_Stats




file = open("500DayFruitData (1).txt",'r')


#Getting the lines and separtings them by /n
data = file.read().splitlines()
#gets rid of first line
data.pop(0)


#lists to put data into 
apple_tracker = []



#finds apples and puts it into the list.
for item in data:
    temp = (item.split())
    if temp[1] == "apple":
        apple_tracker.append(int(temp[2]))







#grabs output from the functions from the stats file
applemean = round( Ethan_Haugen_Stats.mean(apple_tracker),2)
applemedian = round(Ethan_Haugen_Stats.median(apple_tracker),2)
applemode = round(Ethan_Haugen_Stats.mode(apple_tracker),2)










#displays results on a different file
with open("Ethan_Haugen_Output.txt",'w') as f:
    f.write(
        


        "APPLES" + "\n" +
        "===================" + "\n"
        " " +"\n"+


        "The mean number of apples is "+ str(applemean) +"\n"+ 
        "The median number of apples is " + str(applemedian) +"\n"
        "The mode number of apples is " + str(applemode) +"\n"
    )

    
    
    