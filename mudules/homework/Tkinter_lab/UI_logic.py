import tkinter as tk

def get_entery_valu():
    value =entry.get() # קבלת המידע מהחלונית והזנה לפונקציה
    #print(value)
    label.config(text=value)
def do_somthing():
    print("i did somthing")
import tkinter as tk

def change_label():
    label.config(text="label changed !!") # קונפיג משנה דברים בחלון בזמן שהוא רץ

root = tk.Tk()       # הקמת החלון עצמו
root.geometry('200x150+2600+10')    # מחליט על גודל ומיקום החלון
label = tk.Label(root, text ="this is a window") # לייבל זה שם המשתנה של הכותרת, לאחר מכן קוראים לפקודת לייבל מתוך ספריית טיקי. בתוך הסוגריים שם החלון ותוכן הטקסט
label.pack() # זאת בעצם הפקודה שיוצרת את המשתנה שיצרנו כלייבל בחלון
btn1 = tk.Button(root, text="good") # בטן 1 שם המשתנה, קורא לפעולת כפתור מתוך הספרייה. בתוך הסוגריים משייך לחלונית בשם רות ומכניס תוכן טקסט
btn2 = tk.Button(root, text='do somthing', command=do_somthing) #קומנד מאפשר לי לשייך פונקציה לכפתור  
btn3 = tk.Button(root, text='change label', command=change_label)  
btn1.pack() # בדיוק כמו מקודם זה הפקודה שמקימה את המשתנה 
btn2.pack() # משתנה נוסף שנקים בחלון 
btn3.pack()
entry = tk.Entry(root, text= "enter your entery") #חלונית להזנת מידע 
entry.pack()
entry_btn = tk.Button(root, text= "submit", command=get_entery_valu)
entry_btn.pack()
root.mainloop() # לולאה שגורמת לחלון להמשיך לרוץ עד שנלחץ על האיקס  
