
QuestionType = int(input("For amount of time a trip will take type 1, for amount of speed type 2: "))

if QuestionType == 1:

    distance = float(input("Distance in miles: "))
    speed = float(input("Speed in mph: "))

    time = round(distance / speed,2)

    print("It will take", time ,"hours to get to your location!")
else :
    distance = float(input("Distance in miles: "))
    time = float(input("Time in hours: "))

    speed = round(distance/time,2)

    print("You need to go", speed,"mph to reach your destination in time!")