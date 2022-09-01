#This gets an input of the age of the user in a float.
age = float(input("Enter your age: ")) 

#This turns the float of the age from the user into a float of the animal age.
dog_age =  age * 7
cat_age = age / 9
horse_age = 3 * (( (age**2-47) / (7) )+ 12) 

##This following section converts the dog, cat, and horse age float into separte years, months, and days.
#Turns the float into the amount of days.
dog_days = dog_age * 360
cat_days = cat_age * 360
horse_days = horse_age * 360

#Finds the biggest number of years those days fit into, and gives a remainder to complete the next step with.
dog_years = int(dog_days / 360)
dog_remainder_of_days = int(dog_days % 360)

cat_years = int(cat_days / 360)
cat_remainder_of_days = int(cat_days % 360)

horse_years = int(horse_days / 360)
horse_remainder_of_days = int(horse_days % 360)

#Finds biggest number of months that fits within the reaminder of the years. It also finds remainder of that.
dog_months = int(dog_remainder_of_days / 30)
dog_days = int(dog_remainder_of_days % 30)

cat_months = int(cat_remainder_of_days / 30)
cat_days = int(cat_remainder_of_days % 30)

horse_months = int(horse_remainder_of_days / 30)
horse_days = int(horse_remainder_of_days % 30)

#Prints results
print("You are", dog_years, "years,", dog_months, "months, and",dog_days, "days old in dog age!")
print("You are", cat_years, "years,", cat_months, "months, and",cat_days, "days old in cat age!")
print("You are", horse_years, "years,", horse_months, "months, and",horse_days, "days old in horse age!")




#Height thingy, idk if I was suppose to add this.
height = age**2

print("Your estimated height is", height)
