from datetime import datetime, timedelta

# ex1: להציג את התאריך של היום בפורמט YYYY-MM-DD
today = datetime.now()         # 1. קיבלנו את התאריך והשעה הנוכחיים
#print(today.date())            # 2. מציגים רק את התאריך, בלי השעה

#ex2: להציג שעה בלבד

# print(datetime.now().time())

#ex3: להוציא רק את השנה מתוך התאריך הנוכחי

today = datetime.now()
# print(today.year)             

#ex4: לחשב גיל על בסיס שנת לידה.

#birth_year = int(input("Enter birth year: "))  # קלט מהמשתמש
current_year = datetime.now().year             # השנה הנוכחית
#age = current_year - birth_year                # חישוב גיל
# print("Age:", age)

# ex 5: לדעת כמה ימים נשארו עד סוף השנה.

today = datetime.now()
end_of_year = datetime(today.year, 12, 31)  # 31 בדצמבר השנה
delta = end_of_year - today                  # הפרש בין התאריכים
#print("Days left:", delta.days)

#ex6: לתת את היום בשבוע 
today = datetime.now()
#print(today.strftime("%A"))  # מחזיר את שם היום במלל (Monday, Tuesday…)

#ex7 הוספת ימים לתאריך הנוכחי

today = datetime.now()
future_date = today + timedelta(days=10)  # מוסיפים 10 ימים
#print("Future date:", future_date.date())

#ex8 לחשב כמה ימים עברו ביין שני תאריכם 

date1 = datetime(2026, 3, 20)
date2 = datetime(2026, 3, 25)
difference = date2 - date1
#print("Difference:", difference.days, "days")

#ex9: להציג זמן ושעה בפורמט קריא 

now = datetime.now()
formatted = now.strftime("%d/%m/%Y %H:%M")
#print(formatted)

#ex10: בדיקה אם היו שבת או ראשון

today = datetime.now()
weekday = today.weekday()  # Monday=0, Sunday=6
is_weekend = weekday >= 5
#print("Weekend:", is_weekend)

import math

# ex11: שורש ריבועי
#print(math.sqrt(16))

#ex12: חזקה
#print(math.pow(2,3))

#ex13: עיגול למעלה 
#print(math.ceil(4.2))

#ex14:עיגול ללמטה 
#print(math.floor(4.2))

#ex15: ערך מוחלט 
#print(abs(-10))

#ex16: נותן את פאי
#print(math.pi)

#exe17: שטח עיגול
r=5
area = math.pi * math.pow(r,2)
#print(area)

#ex18: מרחק ביין שני מספרים 

x=-5
y=8
#print(abs(x-y))

#ex19=ממוצע

numbers = [5, 7]
average = sum(numbers) / len(numbers)
#print("Average =", average)

#ex20: לחשב כמה שעות עברו מתחילת היום ולהכפיל ב־2.
now = datetime.now()
hours_passed = now.hour + now.minute / 60
result = hours_passed * 2
print("Result =", round(result))