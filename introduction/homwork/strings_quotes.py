
#=====ex2======

#? print("hello world " )

#======ex3=====

#? print(''' first line
#? sec line
#?  third line''')

#=====ex4======

#? print(42)
#? print(2-7)
#? print(0)

#======ex5=====

#? print(1_000+500)

#======ex6=======

#? print(10+3)
#?print(10-3)
#? print(10*3)
#? print(10//3)
#? print(10/3)

#======ex7=======

#? print( "3.14", "-0.5", "2.0", sep=" , ")

#======ex8=======

#? print(1e-2)
#? print(2.5e2)

#======ex9=======

#? print(10/4)
#? print(10//4)

#======ex10======

#? print(0o10)
#? print(0o755)

#======ex11======

#? print(oct(255))
#? print(oct(8))

#=======ex12=====

#? print(0xFF)
#? print(0x1a)

#========ex13=====

#? print(hex(255))
#? print(hex(16))

#========ex14=====

#? print (True)
#? print (False)

#=======ex15======

#? print(3>2)
#? print(1 == 0 )
#? print(5<=5)

#=======ex16======

#? print(bool(0))
#? print(bool(1))
#? print(bool(""))
#? print(bool("hello"))

#New Tasks – Arithmetic Operators and Order of Operations:

#======ex1========

#? print(20+7)
#? print(20-7)
#? print(-5+3)

#======ex2=======

#? print(6 *7)
#? print(-4*5)

#=======ex3======

#? print(20+7)
#? print(20-7)
#? print(-5*3)

#======ex4======

#? print(17/5)
#? print(17//5)

#======ex5======

#? print(-10//3)
#? print(-10/3)

#=====ex6=======

#? print(17 % 5)
#? print(10 % 3 )
#? print(10 % 2)

#======ex7======

#? print(73//60)
#? print(73 % 60 )

#=======ex8=====

#? print(2 +3 *4 )
#? print((2 +3 ) * 4)

#======ex9======

#? print(10 - 2 * 3) 
#? print((10 - 2) * 3)

#New Tasks – Variables:

#======ex1=======

answer=42
#? print(answer)

#======ex2=======

name="niv"
#? (name)

#======ex3====

x=10
#? print(x)
x=20
#? print(20)

#======ex4=====

a=3
b=5

#? print(a, b)

#=======ex5=====

x=10
y=3

#? print(x-y)
#? print(x+y)

#========ex6=====

result=(100//7)
result2=(100%7)
#? print(f"""{result}
#? {result2}""")

#=======ex7======

n=7
#? print(n)
n=(n+1)
#? print(n)

#=======ex8======

a=2
b=3
c=4
#? print(a*b+c)
#? print(a*(b+c))

#=======ex9======

label="count"
value=5
#? print(label, value, sep=": ")

#======ex10======

price=3.5
quantity=2
#? print(price*quantity)

#======ex11======

original=100
copy=original
#? print(original)
#? print(copy)
original=200
#? print(original)
#? print(copy)

#=====ex12========

msg="Done!"
#? print(msg,msg,msg, sep=" ")


#New Tasks – Shortcut (Compound) Assignment Operators

#=====ex1======

n=10
#? print (n)
n-=3
#? print(n)

#=====ex3=====

count=0
# print(count)
# count+=1
# print(count)
# count+=1
# print(count)
# count+=1
# print(count)


#=====ex10=====
string = "hello"
#? print(string)
string += "!!"
#? print(string)

#New Tasks – Type Casting

#=====ex1========

stringnum=42
#? print(stringnum + 8)
int(stringnum)
#? print(stringnum + 8)

#======ex2=======

num=3.9
#? print(num)
#? print(int(num))

#======ex3=======

stringflouts="3.14"
pureflouts=float(stringflouts)
#? print(pureflouts*2)

#======ex4======

intger=int(5)
#? print(intger)
#? print(float(intger))

#=====ex5=======

intnum=int(100)
#? print(str(intnum))
#? print(str(intnum))
#? print(str(intnum), "items")

#New Task input() 

#=====ex1=======

#? name=(input("what is your name ?"))
#? print(name)

#======ex3=======

#? firstname=input("what is your first name? ")
#? lastname=input("what is your last name? ")
#? print(f"Hello,{firstname} {lastname} nice to meet you")

#======ex4=======

#? x=int(input("enter a number"))
#? print(x+x)

#======ex5========
#? v=int(input("enter two numbers: "))
#? n=int(input())

#? print (n+v)

#New Tasks – String Operations: Concatenation, Repetition, and str

#=====ex1======

firststring="hello"
secondstring="world"
#? print(f"{firststring} {secondstring}")

p="py"
n="thon"
pon=(p+n)
#? print(pon)

#====ex2======

u="Hllo"
u+="!"
u+="World"
#? print(u)

#=====ex3=====

#? print("a"*3)

#=====ex4=====

s="-"
#? print(s*10)

#====ex5======

#? print("="*3 +"HI"+ "="*3 )

#=====ex6=====

var=5
#? print("you have "+str(var)+" item")

#======ex7====

var="-"
num=10
print(var*3,"Count: " +str(num), var*3, sep=" ")