import tkinter as tk
 
class Calc(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        #self.frm_formula = tk.LabelFrame(self, text='Formula')
        #self.frm_formula.pack(anchor='e')
        self.frm_result = tk.LabelFrame(self, text='Result')
        self.frm_result.pack(anchor='e')
        self.frm_func = tk.Frame(self)
        self.frm_func.pack(anchor='w')
        self.frm_button = tk.Frame(self)
        self.frm_button.pack(anchor='w')
        self.create_widgets()
        
    def create_widgets(self):
        self.result=tk.StringVar()
        self.result.set('0')
        #self.formula=tk.StringVar()
        #self.formula.set('')
        
        self.operand =""
        self.expr = ""
        #self.clear_expr = False
        
        #formula ラベル(式表示)
        #lb = tk.Label(self.frm_formula, textvariable=self.formula)
        #lb.pack()
        #result ラベル(結果表示)
        lb = tk.Label(self.frm_result, textvariable=self.result)
        lb.pack()
 
        # create and bind clear button
        btn = tk.Button(self.frm_func,text='C',width=3)
        btn.bind("<Button-1>", self.clr_pushed)
        btn.grid(column=0, row=0)
 
        # create 1-9. buttons
        for n, cap in enumerate([7,8,9,4,5,6,1,2,3,0]):
            btn = tk.Button(self.frm_button,text=str(cap),width=3)
            btn.bind("<Button-1>", self.num_pushed)
            btn.grid(column=n%3, row=n//3)
        
        # create dot button    
        btn = tk.Button(self.frm_button,text='.',width=3)
        btn.bind("<Button-1>", self.dot_pushed)
        btn.grid(column=1, row=3)
 
        # create operater buttons
        for n, cap in enumerate(['/','*','-','+']):
            btn = tk.Button(self.frm_button, text=cap, width=3)
            btn.bind("<Button-1>", self.op_pushed)
            btn.grid(column=3, row=n)
 
        # create and bind equal button
        btn = tk.Button(self.frm_button,text='=',width=3)
        btn.bind("<Button-1>", self.eq_pushed)
        btn.grid(column=2, row=3)
 
    def num_pushed(self,event):
        """
        0-9. button pushed
        event.widget['txt']で押されたボタンの「数値」を取得して
        算術計算のオペランドを作成する。
        """
        num_str=event.widget['text']
        print(num_str)
 
 
    def dot_pushed(self, event):
        """
        dot button pushed
        小数点をオペランドに追加する。
        """
        num_str=event.widget['text']
        print(num_str)
            
 
    def op_pushed(self,event):
        '''
        operator(+ - / *) button pushed
        ボタンで入力されたオペランドをオペレータに適用する。
        '''
        self.op=event.widget['text']
        print(self.op)
 
    def eq_pushed(self,event):        
        '''
         equal(=) button pushed
        「=」ボタンが押されたらeval()で計算式を評価する。
        '''
        print("=")
 
    def clr_pushed(self,event):
        '''
         clear(C) button pushed
        「C」ボタンが押されたら計算式と表示をクリアする
 
        '''
        print("C")
 
if __name__ == '__main__':
    root=tk.Tk()
    root.geometry('210x280+100+100')
    root.title("Cal")
    app = Calc(master=root)
    app.mainloop()
