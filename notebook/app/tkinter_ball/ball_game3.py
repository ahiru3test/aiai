import tkinter as tk

WINDOWWIDTH = 400
WINDOWHEIHGT = 420

class Ball:
   def __init__(self,x=30,y=10,vx=7,vy=5):
        self.x=30
        self.y=10
        self.vx=7
        self.vy=5
    
class Bar:
    def __init__(self,pos=0):
        self.pos=pos


class Game(tk.LabelFrame):
    def __init__(self,  master=None, size=(WINDOWWIDTH, WINDOWHEIHGT)):
        super().__init__(master, width=size[0], height=size[1])
        self.pack()
        self.balls=[]
        # self.bars=[]
        self.create_widgets(size)

    def create_widgets(self,size):
        # bar = Bar(0)
        self.pos = 0 #barの位置
        self.w = size[0] #幅
        self.h = size[1] #高さ

        #点数ラベル
        self.score=tk.StringVar()
        self.score.set('0')

        # キャンバスの生成と配置
        self.canvas  = tk.Canvas(self, width = self.w, height = self.h, bg="#fff")
        self.canvas.place(x=0, y=0, anchor=tk.NW)

        # ラベルウィジェットを作成し、textvariableオプションでself.scoreを指定
        score_label = tk.Label(self, textvariable=self.score)
        # placeメソッドでラベルウィジェットを配置し、xとyオプションでフレームの中心にする
        score_label.place(x=self.w//2, y=self.h//2, anchor=tk.CENTER)
        score_label.config(font=("Arial", 32), fg="black")

        # ボールのプロパティ定義
        self.balls.append(Ball(30,10,7,5))
        # self.x = 30
        # self.y = 10
        # self.vx = 7
        # self.vy = 5

        self.s1 = tk.Scale(self, label = '', orient = 'h',
            from_=0, to = self.w-60, 
            command = self.change_pos,
            showvalue = 0,
            length = self.w)
        self.s1.place(x=0, y=self.h, anchor=tk.SW)
        
        self.dia = 20
        
        # タイマースタート
        self.onTimer()
  
    def change_pos(self, pos):
        self.pos = int(pos)


    def onTimer(self):
        # Clear Canvas
        self.canvas.delete('all')
        h = self.h
        w = self.w

        # draw bar
        self.canvas.create_rectangle(self.pos, h - 80, self.pos+60, h - 60, fill = 'blue')

        # Update Circle Pos
        for b in self.balls:
            b.x += b.vx
            b.y += b.vy
            
            if b.x > w or b.x < 0:
                b.vx = - b.vx
            if b.y > h or b.y < 0:
                b.vy = - b.vy
            # elif b.y==self.bar_upper_pos and (self.pos <= self.x <= self.pos+self.bar_width) and self.vy > 0:
            if b.y==(h-80) and (self.pos <= b.x <= self.pos+60) and b.vy > 0:
                b.vy = - b.vy
                score_n = int(self.score.get())+1
                self.score.set(score_n)
                score_c = 3
                if(score_n%score_c==0):
                    self.balls.append(Ball(30,10,7+score_n/score_c,5+score_n/score_c))
          
            # Draw Circle on Canvas
            self.canvas.create_oval(b.x - self.dia/2, b.y - self.dia/2,
                                    b.x + self.dia/2, b.y + self.dia/2,
                                    fill="red")

        self.after(20, self.onTimer)

if __name__=="__main__":
    root=tk.Tk()
    root.title("Tkinter Game")
    app = Game(master=root)
    app.mainloop()
