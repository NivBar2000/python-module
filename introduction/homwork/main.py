#======================================
#  My Profile App - Project
#======================================

name = input ("enter your name: ")
age = input ("enter your age: ")
city = input ("enter your city: ")
populer_hobbies=["music", "sports", "gaming", "reading"]
uniq_hobbies=[]

hobbies=(input("enter your hobbies, after each one put ','").split(",")) #פיצול האינפוט אחרי כל פסיק, יזין את המידע ישר כרשימה  

print("=====================Hello!!====================")
print(f"Hello {name} I heard you'r {age} years old from {city} \nyour hobbies are {", ".join(hobbies)}") 

for i in hobbies:
    print(f" your hobbie {i} is poppuler:{i in populer_hobbies}")
    
hobbies=set(hobbies)

for i in hobbies:
    if (i in populer_hobbies) == False:
        print(f"your hobbies {i} is uniq")
        uniq_hobbies.append(i)
        
if "music" in hobbies: 
    print("music is one of your hobbies")
    uniq_hobbies.append(i)
else:
    print("music is not one of your hobbies")
        

print(f"you have {len(hobbies)} hobbies, only {len(uniq_hobbies)} of them are uniq")