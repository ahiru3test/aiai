import time
import tkinter as tk

class Calc(tk.Frame):
    def __init__(self, master=None):
        ###Frameの初期化
        super().__init__(master)
        self.bind("<Key>", self.key)
        self.focus_set()
        self.pack()

        #LabelFrame部分
        #LabelFrame Fomila
        self.frm_formula = tk.LabelFrame(self, text='Formula')
        # self.frm_formula.pack()
        self.frm_formula.pack(anchor='e')

        #LabelFrame Result
        self.frm_result=tk.LabelFrame(self,text="Result")
        # self.frm_result.pack()
        self.frm_result.pack(anchor="e")

        #grid部分
        #Frame func
        self.frm_func=tk.Frame(self)
        self.frm_func.pack(anchor="w")

        #LabelFrame result2
        self.frm_result2=tk.LabelFrame(self,text="Result")
        self.frm_result2.pack(anchor="e")

        #ButtonFrame部分
        #button
        self.frm_button = tk.Frame(self)
        self.frm_button.pack(anchor="w")

        #create widget
        self.create_widgets()
        

    def create_widgets(self):
        #formulaの値
        self.formula=tk.StringVar()
        self.formula.set('')
        #restltの値
        self.result=tk.StringVar()
        self.result.set("0")

        self.operand =""
        self.expr = ""
        self.clear_expr=False

        #formula部のラベル(式表示)
        lb = tk.Label(self.frm_formula, textvariable=self.formula)
        lb.pack(anchor=tk.E)
        #result部のラベル
        lb = tk.Label(self.frm_result, textvariable=self.result)
        lb.pack(anchor=tk.E)

        #funcのpack
        btn = tk.Button(self.frm_func, text="C",width=3)
        btn.bind("<Button-1>", self.clr_pushed)
        btn.grid(column=0,row=0)

        #result2のpack
        lb2 = tk.Label(self.frm_func, textvariable=self.result)
        lb2.grid(column=1,row=0,columnspan=3)

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



    def clr_pushed(self,event):
        '''
         clear(C) button pushed
        「C」ボタンが押されたら計算式と表示をクリアする
 
        '''
        # print("C")
        self.expr=""
        self.operand=""
        self.result.set("0")
        self.formula.set("")

    def num_pushed(self,event,kbd=None):
        """
        0-9. button pushed
        event.widget['txt']で押されたボタンの「数値」を取得して
        算術計算のオペランドを作成する。
        """
        if kbd is None:
            num_str=event.widget['text']
        else:
            num_str=kbd

        # print(num_str)
            
        self.clear_expr = False

        if self.operand == "0":
            self.operand = num_str
        else:
            self.operand += num_str
        self.result.set(self.operand)
        self.formula.set(self.expr+self.operand)

    def dot_pushed(self, event):
        """
        dot button pushed
        小数点をオペランドに追加する。
        """
        num_str=event.widget['text']
        # print(num_str)

        if self.operand == "":
            self.operand += "0" + num_str
        elif num_str not in self.operand:
            self.operand += num_str
        else:
            return
        self.result.set(self.operand)           
        self.formula.set(self.expr + self.operand)

    def op_pushed(self,event,kbd=None):
        '''
        operator(+ - / *) button pushed
        ボタンで入力されたオペランドをオペレータに適用する。
        '''
        if kbd is not None:
            self.op = kbd
        else:
            self.op=event.widget['text']

        # print(self.op)

        # Mar,23,'22 修正
        # 1+2=*3の入力で計算結果が9になるようにするため。
        if self.clear_expr:
            #self.expr = ""
            self.clear_expr = False
            self.operand = self.result.get()

        # rslt = self.result.get()
        # if rslt != "0" and self.operand == "" and self.expr == "":
        #     self.operand = rslt

        ex = self.expr + self.operand

        # 式が空
        if not ex:
            self.expr = "0" + self.op
        # 式の終端が数値ではない
        elif not ex[-1].isnumeric():
            self.expr = ex[:-1] + self.op
        else:
            self.expr = self.expr + self.operand + self.op
        # result表示の"."を消去
        rst = self.result.get().rstrip(".")
        self.result.set(rst)
        # オペランドクリア
        self.operand = ""
        # 式の表示
        self.formula.set(self.expr)



    def eq_pushed(self,event):        
        '''
         equal(=) button pushed
        「=」ボタンが押されたらeval()で計算式を評価する。
        '''
        # print("=")

        try:
            ex = self.expr + self.operand
            eval(ex)
        except SyntaxError as e:
            print(e)
            print("Error! ", ex)
        except ZeroDivisionError:
            self.result.set("ZeroDivisionError")
            self.update()
            time.sleep(2)
            self.result.set("0")
            self.formula.set("") 
            self.operand = ""
            self.expr = ""   
        else:
            rslt = eval(ex)
            if isinstance(rslt,int):
                self.result.set("{:d}".format(rslt))
            # floatの場合 .is_integer()で小数点以下が"0"かの判定
            elif rslt.is_integer():
                self.result.set("{:d}".format(int(rslt)))
            else:
                self.result.set("{:f}".format(rslt).rstrip("0"))
            self.formula.set(ex + "=")
            # print(rslt)
            self.operand = ""
            self.expr = ""
            self.clear_expr = True

    def key(self,event):
        print( "pressed", repr(event.char))
        print("PRESSED", repr(event.keysym))
        if event.char in ["0","1","2","3","4",
                          "5","6","7","8","9"]:
            self.num_pushed(event, kbd=event.char)
            
        elif event.char == ".":
            self.dot_pushed(event)
 
        elif event.char in ["+", "-","*","/"]:
            self.op_pushed(event, kbd=event.char)
            
        elif event.char == "=" or event.char =="\r":
            self.eq_pushed(event)
            
        elif event.char.upper() == "C" :
            self.clr_pushed(event)


if __name__ == '__main__':
    root=tk.Tk()
    root.geometry('210x280+100+100')
    root.title("Cal")
    app = Calc(master=root)
    app.mainloop()
