import tkinter as tk
 
class App(tk.Frame):
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
 
root = tk.Tk()
root.title("Entry")
root.geometry("200x150")
app = App(master = root)
 
app.mainloop()
