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
# import random
# from re import L


# # list = ["2","3","4","5"]

# # def strtoint(data):
# #     list = []
# #     for number in data:
# #         if number.isdigit:
# #             list.append(int(number)+5)
# #     return list
# # data =strtoint(list)

# # with open("results.txt","w") as f:
# #     for number in data:
# #         f.write(str(number)+ "\n")

# #=======================================================


# def randomnums():
#     list = []

#     for i in range (100):
#         list.append(random.randint(0,100))

#     return list


# randomList = randomnums()

# with open("results.txt","w") as f:
#       for number in randomList:
#          f.write(str(number)+ "\n")

# def listSorter(list):
#     temp = {}
#     num = 0

#     for i in range(len(list)+1):
#         for x in list:
#             if i == x:
#                 num+=1
#         temp[i]=num
#         num = 0
#     return temp


# dictionary = listSorter(randomList)


# with open("final.txt","w") as f:

#     for key in dictionary:
        
#         f.write(str(key)+" : " + str(dictionary[key])+"\n")
    


#=======================================================


# for number in data:
#     if str(number) in temp:




# #=======================================================


# int = 1
# float = 1.53
# Boolean = True
# String = "apu"

# list = [3,56,3,56,6]




# Dictionary = {
# "list1" : [1,23,45,5],
# "list2" : [5,4,3,2,1]

# }


# Dictionary["list3"] = [1,2,23,4,4]

# print(Dictionary)


#=======================================================


# list1 = [1,2,3]
# list2 = ["Number 1","Number 2","Number 3"]

# def listSmasher(list1,list2):
#     dict = {}
#     for i in range (len(list2)):
        
#         dict[list2[i]]=[list1[i]]
        
        
#     return dict
# print(listSmasher(list1,list2))


#=======================================================




# info = {
#     "Num 1" : "12",
#     "Num 2" : "abcs",
#     "Num 3" : "56"

# }




# x = (int(input(": ")))

# for i in (info):
#     if info[i].isdigit():
#         print(info[i])


#=======================================================
# import random


# def problem():
#     temp = {}

#     for i in range(5):
        
#         temp[i]=random.randint(0,100)
#     return temp



# def problem1(info):
#     x = 1
#     y = 0
#     loop = True

    
#     while loop == True:
#         y = random.randint(1,100)

#         for i in info:
#             if info[i]==y:
#                 loop = False
#     print(info)
#     return y
    
# print(problem1(problem()))

#=======================================================
#=======================================================
#=======================================================

#10/12

# import random

# def creatlist(x):
#     temp = []
#     dict = {}
#     for n in range(2):
#         for i in range(x):
#             temp.append(random.randint(0,100))
#         dict[n]=temp
#         temp = []
#     return dict



# print(creatlist(5))

#=======================================================


# def letterfinder(word):
#     a = 0
#     u = 0
#     dict ={}
#     for i in word:
        
#         if i == "a":
#             a +=1
#         if i == "u":
#             u +=1

#     dict["a"] = a
#     dict["u"] = u

#     return dict


# print(letterfinder("apple"))


#=======================================================

# import statistics

# def mile():

#     times = []
#     dictionary = {}
#     for i in range(10):
#         times.append(int(input("Please enter an mile time: ")))

    
#     dictionary["times"] = times
#     dictionary["best"] = max(times)
#     dictionary["worst"] = min(times)
#     dictionary["average"] = statistics.mean(times)

#     return dictionary

# print(mile())

#=======================================================

# list2 = [1,2,3]
# list1= ["num1","num2","num3"]

# def problem3(list1,list2):
    
#     info = {}

#     for i in range(len(list1)):
#         info[list1[i]]=list2[i]

#     for i in range(len(list1)):
#         name ="num" , i +len(list1)
#         info[name]=(list2[i])*5


#     print(info)

# problem3(list1,list2)
