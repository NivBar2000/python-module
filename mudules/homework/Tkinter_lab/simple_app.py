import tkinter as tk 

def get_entry():                  #        יצירת פונקציה 
    value=entry.get()             # שמקבלת את מה שנכנס באנטרי 
    print(value)                  #      כקלט ומדפיסה אותו
    
window = tk.Tk()                        #הקמת החלון     
window.geometry('200x150+2600+10')      # ומיקומו


label = tk.Label(window, text="Enter your text here", fg= "blue")     #   כתיבת  
label.pack(pady=10)                                                   #   הליבל 

entry = tk.Entry(window)                   #  הקמת 
entry.pack(pady=10)                        # האנטרי

btn = tk.Button(window, text="submit", command=get_entry)        #    הקמת הכפתור 
btn.pack()                                                       # וקישור פונקצית האנטרי

window.mainloop()
