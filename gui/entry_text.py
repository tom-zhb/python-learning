import tkinter as tk

window=tk.Tk()
window.title("entry_text")
window.geometry("200x200")
e=tk.Entry(window,show='*')
e.pack()

t=tk.Text(window,height=2)
t.pack()

def insert_point():
    var=e.get()
    t.insert("insert", var)

def insert_end():
    var=e.get()
    t.insert(1.1,var)

b1=tk.Button(window, text="insert point", width=15,height=2,command=insert_point)
b1.pack()

b2=tk.Button(window, text="insert_point", width=15, height=2,command=insert_end)
b2.pack

var=tk.StringVar()
l=tk.Label(window, textvariable=var,bg='green',)
window.mainloop()