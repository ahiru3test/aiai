#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
 
WINDOWWIDTH = 400
WINDOWHEIHGT = 420
 
class Ball(tk.Frame): 
    def __init__(self,  master=None, size=(WINDOWWIDTH, WINDOWHEIHGT)):
        super().__init__(master, width=size[0], height=size[1])
        self.pack()
        self.create_widgets(size)
        
    def create_widgets(self, size):
        self.w = size[0]
        self.h = size[1]                
        # キャンバスの生成と配置
        self.canvas  = tk.Canvas(self, width = self.w, height = self.h, bg="#fff")
        self.canvas.place(x=0, y=0, anchor=tk.NW)
 
        # ボールのプロパティ定義
        self.x = 30
        self.y = 10
        self.vx = 7
        self.vy = 5
        
        self.dia = 20
        
        # タイマースタート
        self.onTimer()
 
    
    def onTimer(self):
        # Clear Canvas
        self.canvas.delete('all')
        h = self.h
        w = self.w
 
        # Update Circle Pos
        self.x += self.vx
        self.y += self.vy
        
        if self.x > w or self.x < 0:
            self.vx = - self.vx
        if self.y > h or self.y < 0:
            self.vy = - self.vy
    
        # Draw Circle on Canvas
        self.canvas.create_oval(self.x - self.dia/2, self.y - self.dia/2,
                                self.x + self.dia/2, self.y + self.dia/2,
                                fill="red")
 
        self.after(20, self.onTimer)
 
 
if __name__=="__main__":
    root=tk.Tk()
    root.title("Tkinter Game")
    app = Ball(master=root)
    app.mainloop()
 