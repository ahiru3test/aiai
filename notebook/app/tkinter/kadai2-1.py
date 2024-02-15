import tkinter as tk

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

        self.color_label = tk.Label(self.master, text = 'COLOR', bg = '#000')
        self.color_label.pack(fill = 'both')
        self.s1 = tk.Scale(self.master, label = 'red', orient = 'h', length = 300,
                from_ = 0, to = 255, variable = self.red,
                command = self.change_color)
        
        self.s2 = tk.Scale(self.master, label = 'blue', orient = 'h', length = 300,
                from_ = 0, to = 255, variable = self.blue,
                command = self.change_color)
        
        self.s3 = tk.Scale(self.master, label = 'green', orient = 'h', length = 300,
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
    # root = tk.Tk()
    # root.title("Tkinter:Scale")
    # root.geometry("300x200")
    # app = App(master = root)
    app = App(master = tk.Tk())

    app.mainloop()


# -------------------------------------------

# Main Window 
# root = tk.Tk()
# root.title("Tkinter:Scale")
# root.geometry("300x200")
 
# Define the scales
# スケール値を読み書きするIntVarオブジェクトの定義
# red = tk.IntVar()
# red.set(0)
# blue = tk.IntVar()
# blue.set(0)
# green = tk.IntVar()
# green.set(0)
 
# Change background color 
# n: ツマミを動かした位置の文字列(不使用)
# スケール位置を示すIntVarオブジェクトred,green,blueで値を読み取り
# ラベルの背景色を設定する。
# def change_color( n ):
# #   color = '#%02x%02x%02x' % (red.get(), green.get(), blue.get())
#     color = '#{:02x}{:02x}{:02x}'.format(red.get(), green.get(), blue.get())
#     color_label.configure(bg = color)
 
# color_Label 
# color_label = tk.Label(root, text = 'COLOR', bg = '#000')
# color_label.pack(fill = 'both');
 
# label: ラベル色を設定
# orient: 'h' 水平に設定
# length: スケールの幅を300ピクセルに設定
# from_, to: スケールの範囲を0から255 に設定
# variable: スケール値を読み書きするIntVarオブジェクトを設定
# command: ツマミを動かしたときに呼び出される関数 change_color を設定
# s1 = tk.Scale(root, label = 'red', orient = 'h', length = 300,
#            from_ = 0, to = 255, variable = red,
#            command = change_color)
 
# s2 = tk.Scale(root, label = 'blue', orient = 'h', length = 300,
#            from_ = 0, to = 255, variable = blue,
#            command = change_color)
 
# s3 = tk.Scale(root, label = 'green', orient = 'h', length = 300,
#            from_ = 0, to = 255, variable = green,
#            command = change_color)
 
# Layout and styling widged
# s1.pack(fill = 'both')
# s2.pack(fill = 'both')
# s3.pack(fill = 'both')
 
# Main
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
