import tkinter as tk

root=tk.Tk()
root.title("packer")
root.geometry("200x150")
color=("red","blue","green","yellow")

# ラベルの作成
for x in range(4):
  label=tk.Label(root,text="Label{}".format(x),bg=color[x])
  #label.pack()
  label.pack(fill="both")

root.mainloop()
