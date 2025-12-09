from tkinter import *
'''root = Tk()
root.title('Number Pad')
root.geometry('250x300')

frame = Frame(master=root, height=200, width=360, bg='#d0efff')
nums = [[9,8,7], [6,5,4], [3,2,1], ['#',0,'*']]
for i in range(4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i,column=j)
        label = Label(master=frame, text=nums[i][j],bg='#d0efff')
        label.pack(padx=3, pady=3)
root.mainloop()'''
root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg='#3895D3')
frame.place(x=20, y=0)

# Labels
lbl1 = Label(frame, text='Full Name', bg='#3895D3', fg='white', width=12)
lbl1.place(x=20, y=20)

lbl2 = Label(frame, text='Email ID', bg='#3895D3', fg='white', width=12)
lbl2.place(x=20, y=80)

lbl3 = Label(frame, text='Password', bg='#3895D3', fg='white', width=12)
lbl3.place(x=20, y=140)

# Entry fields
name_entry = Entry(frame)
name_entry.place(x=150, y=20)

email_entry = Entry(frame)
email_entry.place(x=150, y=80)

pass_entry = Entry(frame, show='*')
pass_entry.place(x=150, y=140)

# Textbox for output
textbox = Text(root, bg='#BEBEBE', fg='black', width=40, height=5)
textbox.place(x=20, y=250)

# Button action
def display():
    name = name_entry.get()
    msg = f"Hey {name}\nCongratulations on your new account!\n"
    textbox.insert(END, msg)

btn = Button(root, text='Create Account', command=display, bg='red')
btn.place(x=130, y=210)

root.mainloop()
