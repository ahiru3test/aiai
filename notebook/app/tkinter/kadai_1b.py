import tkinter as tk
 
root = tk.Tk()
root.title("Entry")
root.geometry("200x150")
 
# def btn_pushed():
#     label_str.set(editbox.get())
# def btn_clr(event):
#     editbox.delete(0, tk.END)
    
label_str = tk.StringVar()
lb = tk.Label(textvariable=label_str, width=20)
lb.pack()
 
editbox = tk.Entry(width = 20)
editbox.pack()
 
# button = tk.Button(text="OK", command=btn_pushed)
button = tk.Button(text="OK", command= lambda : label_str.set(editbox.get()))
button.pack()

clr= tk.Button(text="CLEAR")
# clr.bind("<Button-1>", btn_clr)
# clr.bind("<Button-1>", editbox.delete(0, tk.END)) # bug
clr.bind("<Button-1>", lambda event: editbox.delete(0, tk.END)) 
clr.pack()
 
root.mainloop()