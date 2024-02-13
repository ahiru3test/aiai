import tkinter as tk
root = tk.Tk()
# root.title("Label")
root.geometry("200x150")

root.option_add("*font","FixedSys 14")

#Label
tk.Label(text="Hello").pack()
tk.Label(text="Python").pack()

root.mainloop()
