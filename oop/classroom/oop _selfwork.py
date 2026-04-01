class person:
    def __init__(self, name, age, city, job):
        self.name = name
        self.age =  age
        self.city =  city
        self.job =  job

person1=person("niv", 14, "pt", "pc")
#print(person1.name, person1.age, person1.city, person1.job)

#ex2:

class car:
    def __init__(self, brand, model, year, color):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
        
car1=car("ford", "mustang", 1967, "black")
#print(car1.brand, car1.model, car1.year)

#ex3:

class book:
    def __init__(self, title, author, pages, genre):
        self.title=title
        self.author=author
        self.pages=pages
        self.genre=genre
harry_potter=book("harry_potter", "jk_rolling", 300, "adv")
#print(harry_potter.title, harry_potter.author)

#ex4:

class dog:
    def __init__(self, name, age, breed, weight):
        self.name = name 
        self.age = age
        self.breed = breed
        self.weight = weight

lola = dog ("lola", 14, "maltez", "4 kg")
#print(lola.name, lola.breed)
 
 #ex5
 
class phone:
    def __init__(self, brand, model, price, battery):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery = battery
        
iphone = phone("apple", "16", 1500, "big")
#print(iphone.price)

#ex6:
class student:
    def __init__(self, name, age, grade, school):
        self.name=name
        self.age=age
        self.grade=grade
        self.school=school
        
niv=student("niv", 15, 100, "alomim")
#print(niv.name,niv.grade)
 
#ex7:

class movie:
    def __init__(self, title, year, rating, duration):
        self.title=title
        self.year=year
        self.rating=rating
        self.duration=duration
lion_king=movie("lion_king",1997,"10/10","1:40")
#print(lion_king.duration) 

#ex8
class laptop:
    def __init__(self, brand, ram, storage):
        self.brand=brand
        self.ram=ram
        self.storage=storage
lenovo=laptop("lenovo",16,"1T")
#print(lenovo.ram)     
        