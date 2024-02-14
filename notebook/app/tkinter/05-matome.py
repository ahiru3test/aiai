import tkinter as tk

root=tk.Tk()
root.title("Entry")
root.geometry("200x150")

def bind_entry(event):
    txt = event.widget["text"]
    print(txt)
    label_str.set(txt)
    pass

label_str = tk.StringVar()
label_str.set("Hello Python")

tk.Label(textvariable=label_str).pack()

entry=tk.Entry(text=label_str)
entry.bind("<Entry-1>",)
entry.pack()

root.mainloop()
