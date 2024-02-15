# tkinterをインポートする
import tkinter as tk

# Appクラスを定義する
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # ルートウィンドウを作成する
        self.master = master # この行を追加する
        self.master.title("Tkinter:Scale") # この行を追加する
        self.master.geometry("300x200") # この行を追加する
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.red = tk.IntVar()
        self.red.set(0)
        self.blue = tk.IntVar()
        self.blue.set(0)
        self.green = tk.IntVar()
        self.green.set(0)

        self.color_label = tk.Label(self.master, text = 'COLOR', bg = '#000') # rootをself.masterに変更する
        self.color_label.pack(fill = 'both')
        self.s1 = tk.Scale(self.master, label = 'red', orient = 'h', length = 300, # rootをself.masterに変更する
                from_ = 0, to = 255, variable = self.red,
                command = self.change_color)
        
        self.s2 = tk.Scale(self.master, label = 'blue', orient = 'h', length = 300, # rootをself.masterに変更する
                from_ = 0, to = 255, variable = self.blue,
                command = self.change_color)
        
        self.s3 = tk.Scale(self.master, label = 'green', orient = 'h', length = 300, # rootをself.masterに変更する
                from_ = 0, to = 255, variable = self.green,
                command = self.change_color)
        
        self.s1.pack(fill = 'both')
        self.s2.pack(fill = 'both')
        self.s3.pack(fill = 'both')

        # # ラベルのインスタンスを作成
        # self.label_str = tk.StringVar()
        # tk.Label(self, textvariable=self.label_str, width=20).pack()
        
        # # 入力ボックスのインスタンスを作成      
        # self.editbox = tk.Entry(self, width = 20)
        # self.editbox.pack()
        
        # # ボタンのインスタンスを作成
        # tk.Button(self,text="OK", command = self.btn_pushed).pack()
    def change_color(self, event):
        color = '#{:02x}{:02x}{:02x}'.format(self.red.get(), self.green.get(), self.blue.get())
        self.color_label.configure(bg = color)

    # ボタンのハンドラー
    def btn_pushed(self):
        # self.label_str.set(self.editbox.get())
        # self.editbox.delete(0, tk.END)
        pass


if (__name__=="__main__"):
    # root = tk.Tk() # この行を削除する
    app = App(master = tk.Tk()) # この行を変更する

    app.mainloop()
