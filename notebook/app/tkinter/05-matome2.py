import tkinter as tk

root=tk.Tk()
root.title("Entry")
root.geometry("200x150")

def btn_pushed(event):
    label_str.set(entry.get())

label_str = tk.StringVar()
label_str.set("Hello Python")

tk.Label(textvariable=label_str).pack()

entry=tk.Entry(width=20)
entry.pack()

# button = tk.Button(text="ok", command=btn_pushed)
button = tk.Button(text="ok", command= lambda : label_str.set(entry.get()))
button.pack()

clr=tk.Button(text="CLEAR")
clr.bind("<Button-1>", lambda event: entry.delete(0, tk.END))
clr.pack()

root.mainloop()
