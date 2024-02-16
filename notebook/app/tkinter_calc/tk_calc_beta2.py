import tkinter as tk
 
class Calc(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
 
        # create 1-9. buttons
        for n, cap in enumerate([7,8,9,4,5,6,1,2,3,0]):
            btn = tk.Button(self,text=str(cap),width=3)
            btn.bind("<Button-1>", self.num_pushed)
            btn.grid(column=n%3, row=n//3)
 
    def num_pushed(self,event):
        """
        0-9. button pushed
        event.widget['txt']で押されたボタンの「数値」を取得して
        算術計算のオペランドを作成する。
        """
        num_str=event.widget['text']
        print(num_str)
 
if __name__ == '__main__':
    root=tk.Tk()
    root.geometry('210x280+100+100')
    root.title("Cal")
    app = Calc(master=root)
    app.mainloop()
