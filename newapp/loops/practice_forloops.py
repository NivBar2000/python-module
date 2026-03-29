#====ex1=====
# for  i in range (1,6):
#     print(i)

#======ex2====
    
# for  i in range (5,0,-1):
 #   print(i)
 
#====ex3====

# for i in range (1,6):
#     if  i % 2==0:
#         print (i)

#====ex4====

# for  i in range (1,11):
#     print(i)

#=====ex5===

# for i in range (0,21,3):
#     print(i)

#====ex6====

# for hello in range (5):
#  print ("hello")

#====ex7=====

# sum=0
# for i in range (0,101):
#     sum +=i
# print (sum)

#===ex8======

# mylis=["dani", "dona", "coca"]
# print(len(mylis))

#====ex11====

mylis=["danny", "roni", "dan", "Avi", "Alon"]
# for name in mylis:
#     print(name)

#====ex12====

# print(len(mylis))

#=====ex13====
numlis=[43,1,42,5,6,-4,-78,-13,-4]
# print(sum(numlis))

#=====ex14====

# print(max(numlis))

#=====ex15====

# for name in mylis:
#     if name.startswith("A"):
#         print(name)

#=====ex16====

# for num in numlis:
#     if num % 2 == 0:
#         print(num)

#=====ex17====

counter=0
for num in numlis:
    if num > 10:
        counter+=1
#print(counter)

#=====ex18====

# for num in numlis:
#     if num % 2 == 0 and num % 3 == 0:
#         print(num)

#=====ex19====

# for num in numlis:
#     print(num*num)

#======ex20===

last_list=[]

for num in numlis:
    if num > 0:
        last_list.append(num)
#print(last_list)