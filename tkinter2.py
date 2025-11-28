
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('loop')

lables=['what is your name :','what is your age :','what is emile :','what is your country :','what is religen :']
for i in range(len(lables)):
    cur_label='lable' + str(i)
    cur_label = ttk.Label(win, text=lables[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)

# create entery box
name_var = tk.StringVar()
user_info={
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'emile':tk.StringVar(),
    'country':tk.StringVar(),
    'religen':tk.StringVar()
}
for i in user_info:
    cur_enterbor="entery" +i
    cur_entrybox = ttk.Entry(win, width=18, textvariable=user_info[i])
    cur_entrybox.grid(column=1,row=counter)
    counter+=1








win.mainloop()