

def openFile(file):
    temp = open(file,"r")
    data = temp.read().splitlines() 
    return data
def readNums(data):
    list = []
    for i in data:
        if i.isdigit():
            list.append(int(i))
    return list
def findMax(index, current_max, data):
   

    maxxy = data[index]

    if maxxy >= current_max:
        current_max = maxxy
    
    if index >= len(data) - 1:
        return current_max

    else:
        return findMax(index+1,current_max,data)
def findMin(index, current_min, data):
    minny = data[index]

    if minny <= current_min:
        current_min = minny
    
    if index >= len(data) - 1:
        return current_min

    else:
        return findMin(index+1,current_min,data)
def extrema(data,calcMin=True, calcMax=True):


    if calcMin == True and calcMax == True:
        return findMin(0,100000,data),findMax(0,0,data)
    elif calcMin == False and calcMax == False:
        return ("nothing was done")
        
    elif calcMin == False:
        return findMax(0,0,data)
    elif calcMax == False:
        return findMin(0,0,data)

nums = readNums(openFile("8randomValues.txt")) 


print(findMin(0,10000,nums))
print(findMax(0,0,nums))
print(extrema(nums))