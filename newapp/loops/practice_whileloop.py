#=====ex1=====

# i = 1

# while i <= 5:
#     print(i)
#     i += 1
    
#======ex2=====

# i=5

# while i > 0:
#     print(i)
#     i-=1 

#======ex3=====

# i = 1 
# while i < 10 :
#     if (i%2) == 0:
#         print(i)
#     i+=1

#=====ex4=====

# total=0
# i=1
# while i <= 5:
#     total+=i
#     i+=1
# print(total)

#=====ex5======
# i = 10
# while i > 0:
#     if i % 3 ==0:
#         print(i)
#     i=i-1

#=====ex6======

# num = input("enter a num: ")
# i=0
# while i < 5:
#     print(num)
#     i+=1
    
#=====ex7======

# usernume=int(input("enter a number"))
# i=1
# while i <= usernume:
#    print(i)
#    i+=1
    
#====ex8=====

# stop = False
# while stop == False:
#     usernum=int(input("enter a number: "))
#     if usernum == 0:
#         stop=True

#=====ex9=====

# passwd="000"
# while passwd != "1234":
#     passwd=input("enter your paswred")
    
#=====ex10====

# answer=input("chose y/n: ")
# while answer != "n":
#     answer=input("chose y/n: ")
    
#======ex11====

# even=[]
# i=1
# while i < 20:
#     if i % 2 == 0:
#         even.append(i)
#     i+=1
# print(f" there are {len(even)} numbers betwin 1 and 20")
# print(even)

#=====ex12=====

# counter=0
# i=1
# while i < 10:
#     if i % 2 == 1:
#         counter +=1
#         print(i)
#     i+=1
# print(f" there are {counter} numbers betwin 1 and 20")

#=====ex14=======

# user="hello"
# while user != "q":
#     user=input("enter a num or 'q' to exit: ")
#     if user == "q":
#         break
#     else:
#         if int(user) % 2 == 0:
#             print("even number")
#         else:
#             print("not a even number")