
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('GUI base project')

# create labels
name_label = ttk.Label(win, text='Enter your name:')
name_label.grid(row=0, column=0, sticky=tk.W)

age_label = ttk.Label(win, text='Enter your age:')
age_label.grid(row=1, column=0, sticky=tk.W)

email_label = ttk.Label(win, text='Enter your email:')
email_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text='Enter your gender:')
gender_label.grid(row=3, column=0, sticky=tk.W)

# create entry boxes
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=18, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=18, textvariable=age_var)
age_entrybox.grid(row=1, column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=18, textvariable=email_var)
email_entrybox.grid(row=2, column=1)

gender_var = tk.StringVar()
gender_entrybox = ttk.Entry(win, width=18, textvariable=gender_var)
gender_entrybox.grid(row=3, column=1)

# create combobox
gender_combobox=ttk.Combobox(win,width=15 ,state='readonly')
gender_combobox['values']=('male','female','other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1) 

# ridio button 
userType=tk.StringVar()
ridiobtn1=ttk.Radiobutton(win,text='student',value='student',variable=userType)
ridiobtn1.grid(row=4,column=0)

ridiobtn2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=userType)
ridiobtn2.grid(row=4,column=1)

# check button
usercheck=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text='if you want to subscribe to our channel',variable=usercheck)
checkbtn.grid(row=5,columnspan=3)





# create a button
def action():
    user_name = name_var.get()
    user_age = age_var.get()
    user_email = email_var.get()
    print(f'{user_name} is {user_age} and has email: {user_email}')
    user_gen=gender_combobox.get()
    user_type=userType.get()
    if usercheck.get() ==0:
        subscribed="no"
    else:
        subscribed="yes"

    print(user_gen , user_type, subscribed)

    with open('file.txt','a') as f:
        f.write(f'{user_name},{user_age},{user_email},{user_gen},{user_type},{subscribed}')
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_entrybox.configure(foreground='Blue')

submit_button = ttk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, column=0)

win.mainloop()
