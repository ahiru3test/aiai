import tkinter as tk
root = tk.Tk()
root.title("Label")
root.geometry("200x150")

#Label
# lb=tk.Label(root, text="Python Tkinter", fg="white",bg="blue")
# lb=tk.Label(text="Python Tkinter", fg="white",bg="blue")
lb=tk.Label(text="Python", font=("Helvetica","14","bold"))
lb.pack()

root.mainloop()
