# list1 = ["I","your","dude"]
# list2 = ["am","boss",'.']

# for i in range(0,3):
#     print (list1[i],list2[i],end=" ")
   

# from subprocess import list2cmdline


# def problem2():

#     list = []
#     list2 = []
#     list3 = []


#     for i in range(0,5):
#         list.append(int(input("Enter a number for list 1: ")))
#     for i in range(0,5):
#         list2.append(int(input("Enter a number for list 2: ")))
#     for i in range(0,5):
#         list3.append(list[i]+list2[i])


#     print (list)
#     print(list2)
#     print (list3)




# problem2()

#x.isdigit() returns a boolean value depending on if the input is a digit or not





family = []
rank = []

for i in range (0,3):
    family.append(input("Please enter a family member: "))



for i in range (0,3):
    rank.append( int(input("What rank is " + family[i] + "?  ")))




print(family[0], rank[0])