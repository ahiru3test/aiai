import tkinter as tk

root=tk.Tk()
root.title("Entry")
root.geometry("200x150")

#Entry
#Entry
editbox = tk.Entry(width=20)
editbox.insert(tk.END, "名前の入力")
editbox.pack()

root.mainloop()
