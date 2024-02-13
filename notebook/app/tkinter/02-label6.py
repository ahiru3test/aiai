import tkinter as tk
root = tk.Tk()
# root.title("Label")
root.geometry("200x150")

lb=tk.Label(text="Python")
lb.pack()
lb.configure(bg="yellow")
lb.configure(fg="blue")
lb.cget("text")

root.mainloop()
