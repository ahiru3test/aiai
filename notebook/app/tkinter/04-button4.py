import tkinter as tk

root=tk.Tk()
root.title("button")
root.geometry("200x150")
# color=("red","blue","green","yellow")

def button_on(event):
  txt = event.widget["text"]
  label_str.set(txt)

# def button_off(event):
#   label_str.set("OFF")

label_str = tk.StringVar()
label_str.set("NON")

tk.Label(textvariable=label_str).pack()

btn_on=tk.Button(text="ON", width=3)
btn_on.bind("<Button-1>",button_on)
btn_on.pack()

btn_off=tk.Button(text="OFF", width=3)
btn_off.bind("<Button-1>",button_on)
btn_off.pack()

root.mainloop()
