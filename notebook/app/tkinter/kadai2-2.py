import tkinter as tk
import time as tm

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.buff = tk.StringVar()
        self.buff.set('')
        tk.Label(textvariable = self.buff, font=('FixedSys',14,'bold')).pack()

        # # ラベルのインスタンスを作成
        # self.label_str = tk.StringVar()
        # tk.Label(self, textvariable=self.label_str, width=20).pack()
        
        # # 入力ボックスのインスタンスを作成      
        # self.editbox = tk.Entry(self, width = 20)
        # self.editbox.pack()
        
        # # ボタンのインスタンスを作成
        # tk.Button(self,text="OK", command = self.btn_pushed).pack()

    # 時刻の表示
    def show_time(self):
        self.buff.set(tm.strftime('%I:%M:%S'))
        self.after(1000, self.show_time)
        # root.after(1000, show_time)

if (__name__=="__main__"):
    root = tk.Tk()
    root.title("Clock")
    root.geometry("200x100")
    app = App(master = root)
    app.show_time()
    app.mainloop()

# exit()


# root = tk.Tk()
# root.title("デジタル時計")
# root.geometry("200x100")

# buff = tk.StringVar()
# buff.set('')

# tk.Label(textvariable = buff, font=('FixedSys',14,'bold')).pack()


# show_time()
# root.mainloop()


class App2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        # ラベルのインスタンスを作成
        self.label_str = tk.StringVar()
        tk.Label(self, textvariable=self.label_str, width=20).pack()
        
        # 入力ボックスのインスタンスを作成      
        self.editbox = tk.Entry(self, width = 20)
        self.editbox.pack()
        
        # ボタンのインスタンスを作成
        tk.Button(self,text="OK", command = self.btn_pushed).pack()

    # ボタンのハンドラー
    def btn_pushed(self):
        self.label_str.set(self.editbox.get())
        self.editbox.delete(0, tk.END)

# root = tk.Tk()
# root.title("Entry")
# root.geometry("200x150")
# app = App(master = root)

# app.mainloop()

