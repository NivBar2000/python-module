def age_user():
   user_age_year= int(input ("what is your age? "))
   user_age_sec=user_age_year*365*24*60*60
   print(f"you age in sec si {user_age_sec}")

def add_number(x,y):
    s=x+y
    print()



def first_last_name(name, last_name):
    print(name, last_name)


def divide(x,y):
    if (x==0):
        print("you fool")
    elif (y==0):
        print("you fool")
    else:
        print(x/y)





#====================Lab 3.6.1=================

def yourlist(*args):
    print(args)
    total=(sum(args))
    counter=0
    for i in args:
        counter+=1
    print(f"you'v enterd {counter} numbers")  
    print(f"the sum of your numbers is {total} and the avarage of your number is {total/counter}")   #סכום מספרים, כמות וומוצע

    
#? yourlist(6,5,77)

#======ex2=========                       מספר קטן ביותר וגדול ביותר          

def who_is_who(*mytuple):
    print(f"the smellst number is {min(mytuple)}")
    print(f"the bigest number is {max(mytuple)}")
#? who_is_who(66,5,3)


#=======ex3========                        רק מספרים זוגיים בסדר עולה 

def only_pairs(*mytuple):
    mylist=list(mytuple)
    pair_list=[]
    for i in mylist:
        if (i%2)==0:
            pair_list.append(i)
    print(pair_list)
    print(sorted(pair_list))
#? only_pairs(2,5,6,3,1,8,66,44,2,33)
 
#=========ex4=======                         עם זוגי תחזיר זוגי ואם אי זוגי תחזיר בהתאם 

def is_even(x):
    if (x%2)==0:
        print("even")
    else:
        print("odd")

#? is_even(7)
 
#========ex5=======                            תדפיס רק ציונים מעל 60

def only_above_60(greadlist):
    for i in greadlist:
        if i >= 60:
            print(i)
#? only_above_60([60,77,97,45,76])
   
#=========ex6======                           בודקת אם הרשימה ריקה, אם ךלא ריקה תדפיס ממוצע 

def is_empty(rendom_list):
    counter=0
    print(rendom_list)
    if not rendom_list:
        print("none")
    else:
        for i in rendom_list:
            counter+=1
    print(f"the avrege is {(sum(rendom_list))/counter}")
#? is_empty([2,5,2,1])

#=========ex7=======                         מדפיסה רק מספרים מעל 10

def the_min_is10(yourlist):
    the_above10=[]
    for i in yourlist:
        if i > 10:
            the_above10.append(i)
    print(the_above10)
  
some_list=[45,8,6,55,34]  
#? the_min_is10(some_list)            
    
#=========ex8========                       מקבלת ערך בוליאני ובהתאם אליו הופכת את הרשימה

def stupid_fun(user_list,reverse=False):
    if reverse == True:
        user_list.reverse()
        print(user_list)
    else:
        print(user_list)
ls=[3,1,24,5,7]
#? stupid_fun(ls)

#=========ex9========                        מקבלת אין סוף מספרים ומדפיסה את הגדול ביותר

def th_bigest(*args):
    print(max(args))

#? th_bigest(1,5,23,4)
    
#=========ex10======                           מקבלת מספרים ומדפיסה רק זוגיים 

def only_pairs(*mytuple):
    pair_list=[]
    for i in mytuple:
        if (i%2)==0:
            pair_list.append(i)
    print(pair_list)
#? only_pairs(1,4,6,2,4,1,3,8)

#==========ex11======                          מקבלת שם ושם משפחה ומדפיסה בפורמט מסודר

def name_lastname(name, age):
    print(name, age)
#? name_lastname(age=14, name="tomer")

#==========ex12======                            מקבל רשימה ומוציא מינימום מקסימום וסכום

def  all_kind_of(user_list):
    print(min(user_list))
    print(max(user_list))
    print(sum(user_list))
#? all_kind_of([2,5,1,6,8,3])

#=========ex13=======                           פונקציה בתוך פונקציה שמחשבת סכום

def does_nothing(x,y):
    def total(a,b):
        num_sum=(a+b)
        print(num_sum)
    total(x,y)
#? does_nothing(5,6)     
 
#=========ex14=======                           לוקח משתנה מבחוץ ועושה לו מניפולציה, נידרש גלובל

number1=6

def outsid():
    def inside():
        global number1
        number1+=7
        print(number1)
    inside()
#? outsid()

#==========ex15======                          לוקח משתנה מתוך הפונקציה החיצונית שימוש בנון לוקאל

def outsid2():
    number2=6
    
    def inside():
        nonlocal number2
        number2+=3
        print(number2)
    inside()
#? outsid2()


#==========ex16======                          פונקציה שמקבלת רשימה ופונקציה ומפעילה אתהפונקציה על כל איבר ברשימה

somone_list=[1,2,3]

def addone(x):
    x+=1
    return x
    
def real_thing(list, func):
    new_list=[]
    for i in list: 
            new_list.append(func(i))
    print(new_list)
            
#? real_thing(somone_list, addone)

#===========ex17=======                     פונקציה מקבלת מספר ופונקציה ומבצעת אותה עליו

def num_andfun(x, fun):
    print(fun(x))
#? num_andfun(5,addone)
    
#===========ex18=======                     מקבל ערך בוליאני, רשימה, נותן רשימה עם ערכים שעוברים את הרף ואם הערך אמת הופך את הרשימה

def real_thing2(list, reverse=False):
    new_list=[]
    for i in list:
        if i > 10:
            new_list.append(i)
    if reverse == True:
        new_list.reverse()
        print(new_list)
    else:
        print(new_list)

shit=[5,1,88,6,324]
#? real_thing2(shit,)
   
    
#============ex19========                     מקבל כמות לא מוגבלת של מספרים נותן סכום, מנימום ומקסימום 

def we_allmost_there(*my_new_tuple):
    print(my_new_tuple)
    print(max(my_new_tuple))
    print(min(my_new_tuple))
    print(sum(my_new_tuple))
    
#? we_allmost_there(1,54,465,6,32,5,65,34)

#============ex20========

the_last_ls=[4,15,2,1,6]

def tuple_of_even(ls):
    evens=[]
    non_evens=[]
    for i in ls:
        if i%2==0:
            evens.append(i)
        else:
            non_evens.append(i)
    
    evens=tuple(evens)
    non_evens=tuple(non_evens)
    
    print(f"evens are{evens} non-evens are {non_evens}")
tuple_of_even(the_last_ls)