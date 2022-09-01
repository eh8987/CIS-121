# this gets a flaot input from the user.
age = float(input("Enter your age: ")) 

# this turns the age from the user into animal age.
dogage =  age * 7
catage = age / 9
horseage = 3 * (( (age**2-47) / (7) )+ 12) 

## this following section converts the dog, cat, and horse age float into separte years months and days
#turns years float into days
dogdays = dogage * 360
catdays = catage * 360
horsedays = horseage * 360

#finds biggest number of years those days fit into and gives a remainder
dogyears = int(dogdays / 360)
dogmonthdays = int(dogdays % 360)

catyears = int(catdays / 360)
catmonthdays = int(catdays % 360)

horseyears = int(horsedays / 360)
horsemonthdays = int(horsedays % 360)

#finds biggest number of months within the reaminder of the years. also finds remainder of that.
dogmonths = int(dogmonthdays / 30)
dogdays = int(dogmonthdays % 30)

catmonths = int(catmonthdays / 30)
catdays = int(catmonthdays % 30)

horsemonths = int(horsemonthdays / 30)
horsedays = int(horsemonthdays % 30)

#prints results
print("You are", dogyears, "years,", dogmonths, "months, and",dogdays, "days old in dog age!")
print("You are", catyears, "years,", catmonths, "months, and",catdays, "days old in cat age!")
print("You are", horseyears, "years,", horsemonths, "months, and",horsedays, "days old in horse age!")


#height thingy
height = age**2

print("Your estimated height is", height)