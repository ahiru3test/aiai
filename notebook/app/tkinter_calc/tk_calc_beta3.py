import tkinter as tk
 
root=tk.Tk()
 
def num_pushed(event):
    """
    0-9. button pushed
    event.widget['txt']で押されたボタンの「数値」を取得して
    算術計算のオペランドを作成する。
    """
    num_str=event.widget['text']
    print(num_str)
 
 
def dot_pushed(event):
    """
    dot button pushed
    小数点をオペランドに追加する。
    """
    num_str=event.widget['text']
    print(num_str)
        
 
def op_pushed(event):
    '''
    operator(+ - / *) button pushed
    ボタンで入力されたオペランドをオペレータに適用する。
    '''
    op=event.widget['text']
    print(op)
 
def eq_pushed(event):        
    '''
     equal(=) button pushed
    「=」ボタンが押されたらeval()で計算式を評価する。
    '''
    print("=")
 
def clr_pushed(event):
    '''
     clear(C) button pushed
    「C」ボタンが押されたら計算式と表示をクリアする
 
    '''
    print("C")
 
#class Calc(tk.Frame):
#    def __init__(self, master=None):
#        super().__init__(master)
#        self.pack()
# ベースになるフィレームを定義
frm = tk.Frame(root)
frm.pack()
#frm_formula = tk.LabelFrame(frm, text='Formula')
#frm_formula.pack(anchor='e')
frm_result = tk.LabelFrame(frm, text='Result')
frm_result.pack(anchor='e')
frm_func = tk.Frame(frm)
frm_func.pack(anchor='w')
frm_button = tk.Frame(frm)
frm_button.pack(anchor='w')
#        create_widgets()
 
#    def create_widgets(self):
result=tk.StringVar()
result.set('0')
#formula=tk.StringVar()
#formula.set('')
 
operand =""
expr = ""
#clear_expr = False
 
 
#formula ラベル(式表示)
#lb = tk.Label(frm_formula, textvariable=formula)
#lb.pack()
#result ラベル(結果表示)
lb = tk.Label(frm_result, textvariable=result)
lb.pack()
 
# create and bind clear button
btn = tk.Button(frm_func, text='C',width=3)
btn.bind("<Button-1>", clr_pushed)
btn.grid(column=0, row=0)
 
# create 1-9. buttons
for n, cap in enumerate([7,8,9,4,5,6,1,2,3,0]):
    btn = tk.Button(frm_button,text=str(cap),width=3)
    btn.bind("<Button-1>", num_pushed)
    btn.grid(column=n%3, row=n//3)
 
# create dot button    
btn = tk.Button(frm_button,text='.',width=3)
btn.bind("<Button-1>", dot_pushed)
btn.grid(column=1, row=3)
 
# create operater buttons
for n, cap in enumerate(['/','*','-','+']):
    btn = tk.Button(frm_button, text=cap, width=3)
    btn.bind("<Button-1>", op_pushed)
    btn.grid(column=3, row=n)
 
# create and bind equal button
btn = tk.Button(frm_button,text='=',width=3)
btn.bind("<Button-1>", eq_pushed)
btn.grid(column=2, row=3)
 
#if __name__ == '__main__':
    #root=tk.Tk()
    #root.geometry('210x280+100+100')
    #root.title("Cal")
    #app = Calc(master=root)
    #app.mainloop()
root.geometry('210x280+100+100')    
root.title("Cal")
root.mainloop()
