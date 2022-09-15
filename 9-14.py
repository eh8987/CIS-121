
iterations = float(input("Enter the number of iterations: "))
y = 1
x = 3
count = 1
while count < iterations:
    count += 1
   
    fraction = 1/-x
    y += fraction

#This gets the demoninator of the fraction and swaps from positive to negative
    if x < 0:
        x = (abs(x)+2)
    else:
        x = -1*(abs(x)+2)
    
    
pi = 4*y
print(pi)
