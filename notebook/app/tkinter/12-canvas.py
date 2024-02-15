import os
import tkinter as tk
 
root = tk.Tk()
root.title("Canvas")
 
### キャンバスの作成
c1 = tk.Canvas(width = 300, height = 200)

###画像の貼付
fname = os.path.dirname(__file__) + '/img_05_l.gif'
image_data = tk.PhotoImage(file = fname)
# id4 = c1.create_image(150,100, image=image_data)
id4 = c1.create_image(300, 0, anchor=tk.NE, image=image_data) 

### 四角の描画
id2 = c1.create_rectangle(10,10,140,140, fill='yellow')

### 円の描画
id = c1.create_oval(10,10,140,140)

### 線の描画とその修飾
id3 = c1.create_line(10,140,10,10,140,140,140,10,)
c1.itemconfigure(id3, width=2.0, fill='green')
c1.itemconfigure(id3, smooth=True)

###文字の描画
id5 = c1.create_text(75,75,text= 'Hello Python', font=('FixedSys', 14))

c1.pack()
 
root.mainloop()
