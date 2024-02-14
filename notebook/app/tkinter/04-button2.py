import tkinter as tk

root=tk.Tk()
root.title("button")
root.geometry("200x150")
# color=("red","blue","green","yellow")

def button_on():
  label_str.set("ON")

def button_off():
  label_str.set("OFF")

label_str = tk.StringVar()
label_str.set("NON")

tk.Label(textvariable=label_str).pack()

btn_on=tk.Button(text="ON", width=3, command=button_on)
btn_on.pack()

btn_off=tk.Button(text="OFF", width=3, command=button_off)
btn_off.pack()

root.mainloop()
