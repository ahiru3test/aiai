import tkinter as tk
root = tk.Tk()
# root.title("Label")
root.geometry("200x150")

lab_str=tk.StringVar()
lab_str.set("Hello")
lab=tk.Label(textvariable=lab_str,bg="yellow")
lab.pack()
lab_str.set("Python")

root.mainloop()
