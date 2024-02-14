import tkinter as tk

root=tk.Tk()
root.title("placer")
root.geometry("200x150")
color=("red","blue","green","yellow")

# ラベルの作成
for x in range(3):
  label=tk.Label(root,text="Label{}".format(x),bg=color[x])
  #label.pack()
  label.place(relx=0.25*x,rely=0.25*x)

root.mainloop()
