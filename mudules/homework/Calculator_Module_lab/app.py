from utlis import *
print('''
===========================
welcome to you calculator!!
===========================
        ''')

user_choise=int(input('''
1. for adding
2. for Subtraction
3. for multipy
4. for divide
                      '''))

x=int(input("enter your first number: "))
y=int(input("enter your seconde number: "))
oper(x, y, user_choise)