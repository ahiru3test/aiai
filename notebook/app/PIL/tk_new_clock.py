import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import datetime
 
 
class AClock(tk.Frame):
    def __init__(self, master=None, size=(300,300)):
        #self.master = master
        super().__init__(master)
        self.pack()
        self.create_widgets(size)
        
    def create_widgets(self, size):
 
        w = size[0]
        h = size[1]
        self.cv = tk.Canvas(width = w, height = h)
        self.id_ = None
        self.cv.pack(expand=True,fill='both')
 
        # 文字盤の図形作成
        canvas = Image.new('RGBA', (300, 300), (255,255,255,0))
        draw = ImageDraw.Draw(canvas)
        for i in range(1,13):
            draw.line((280, 150, 300, 150), fill='black', width=2)
            canvas = canvas.rotate(30)
            draw = ImageDraw.Draw(canvas)
        self.canvas = canvas
 
        # 時針の図形作成
        self.imhour = Image.new('RGBA', (300, 300), (255,255,255,0))
        drawhour = ImageDraw.Draw(self.imhour)
        drawhour.polygon((150,150)+(175,140)+(250,150)+(175,160),fill='black')
 
        # 分針の図形作成
        self.imminute = Image.new('RGBA', (300, 300), (255,255,255,0))
        drawminute = ImageDraw.Draw(self.imminute)
        drawminute.polygon((150,150)+(180,145)+(270,150)+(180,155),fill='black')
 
        # 秒針の図形作成
        self.imsecond = Image.new('RGBA', (300, 300), (255,255,255,0))
        drawsecond = ImageDraw.Draw(self.imsecond)
        drawsecond.line((150,150)+(270,150), fill='red', width=2)
 
        self.show_time()
 
    def clock_image(self):
        tm = datetime.datetime.now()
        tmhour = tm.hour
        tmminute = tm.minute
        tmsecond = tm.second+tm.microsecond/1000000
        
        # 時計の文字盤複製
        canvas = self.canvas.copy()
        
        # 時針の描画
        imhour = self.imhour.rotate(-(tmhour*30+tmminute//2-90))
        canvas.paste(imhour,(0,0),imhour)
        
        # 分針の描画
        imminute = self.imminute.rotate(-(tmminute*6-90))
        canvas.paste(imminute,(0,0),imminute)
        
        # 秒針の描画
        imsecond = self.imsecond.rotate(-(tmsecond*6-90))
        canvas.paste(imsecond, (0,0), imsecond)
        
        return canvas
 
 
    def show_time(self):
        #global id_, image_data, cv
        self.cv.delete(self.id_)
        w = self.cv.winfo_width()
        h = self.cv.winfo_height()
        # 縦横小さい方をsizeにする
        size = w if w < h else h
        image = self.clock_image()
        # 縦横の小さい方でリサイズ
        image = image.resize((size, size))
        self.image = ImageTk.PhotoImage(image)
        self.id_ = self.cv.create_image(w//2, h//2, image=self.image)
 
        self.after(20, self.show_time)
 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("tkClock")
    aclock = AClock(master=root)
    aclock.mainloop()
