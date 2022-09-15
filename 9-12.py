number =  int(input("Pick a number 35-100: "))
prints = 0
while prints < number:
    if number > 100:
        number = 100
    prints = prints + 1
   
    if prints % 2 == 0:
        print(prints)
    
    