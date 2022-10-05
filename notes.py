###10/3/2022


#Dictionaries 



# info = {
# "Patient 0" : ["Ethan"]
# }
# info["Patient 1"] = ["Sarah"]

# print(info)

#=====================================================

# name = input("name: ")
# lastname = input("last name: ")
# age = input("age: ")


# info = {
# name : [name,lastname,age]

# }

# print("Hi! your name is " ,info[name][0])


#=======================================================
# import statistics
# players = {}


# for i in range(0,5):
#     player = input("Please enter a soccer player: ")
#     goals = int(input("Please enter how many goals they scored: "))
    
#     players[i] = [player, goals]


# def averagegoals():
    
#     data = []
#     for i in range (0,5):
#         data.append(players[i][1])
#     average = statistics.mean(data)
#     return average

#=======================================================




# dictionary = {
# "hello" : [1,2,3],
# "goodbye" : [1,2],
# "hi" : [1,2,3],
# "die" : [1,2,3] 
# }



# def check(dict,key):
#     keycheck = key
    
#     for i in (dict):
#         if keycheck == i:
#             return True
        
#     return False

# print(check(dictionary,"hello"))


#=======================================================


# info1= {
#     "data" : [1,2,3,4,5]
# }

# info2= {
#     "data" : [6,7,8,9,10]
# }

# def adding(dict1,dict2):
    
#     results = []
#     for key in dict1:
#         for key2 in dict2:
#             if key == key2:
#                 for i in range(5):
#                     results.append(dict1[key][i]+dict2[key2][i])
    
#     print(results)

# adding(info1,info2)

#=======================================================
#=======================================================
#=======================================================
#=======================================================

#10/5
import random
from re import L


# list = ["2","3","4","5"]

# def strtoint(data):
#     list = []
#     for number in data:
#         if number.isdigit:
#             list.append(int(number)+5)
#     return list
# data =strtoint(list)

# with open("results.txt","w") as f:
#     for number in data:
#         f.write(str(number)+ "\n")

#=======================================================


def randomnums():
    list = []

    for i in range (100):
        list.append(random.randint(0,100))

    return list


randomList = randomnums()

with open("results.txt","w") as f:
      for number in randomList:
         f.write(str(number)+ "\n")

def listSorter(list):
    temp = {}
    num = 0

    for i in range(len(list)+1):
        for x in list:
            if i == x:
                num+=1
        temp[i]=num
        num = 0
    return temp


dictionary = listSorter(randomList)


with open("final.txt","w") as f:

    for key in dictionary:
        
        f.write(str(key)+" : " + str(dictionary[key])+"\n")
    


#=======================================================


# for number in data:
#     if str(number) in temp: