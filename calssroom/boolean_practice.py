# day_of_week = input("What day of the week is it today? ").lower

# print(f"==================\n{day_of_week}")
# if day_of_week == "monday":
#     print("you are right")
# elif day_of_week == "sunday":
#     print("bad")
# else:
#     print("good")

# print ("always")

#======Membership Testing with in=========

frinds=["rolf", "bob", "jen"]
#? print("en" in frinds)

movies={"dog", "cat", "ron"}

# user_movie = input("Enter a movie you have watched recently: ").lower()

# if user_movie in movies:
#     print("your movie is good")
# else:
#     ("you are stupid")
    
secrat_num = 5
user_input_option=("y", "Y")

user_input = input("Enter Y if you would like to play: ")
if user_input in user_input_option:
    geussed_number= int(input("geuss a number "))
    if geussed_number == secrat_num:
        print("you are right")

    
    else:
        print("you are worng")
else:
    print("you are lame")









# user_movie=input("enter a movie: ").lower()
# if user_movie in movies:
#     print("your movie is a movie")
# else:
#     print("stupid fuck")


#print("rix2" in "matrix")



