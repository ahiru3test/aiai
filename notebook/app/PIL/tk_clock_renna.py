import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import datetime
import os
 
class AClock(tk.Frame):
    def __init__(self, master=None):
        # 親クラス(tk.Frame)のコンストラクター呼び出し
        super().__init__(master)
        # Frameをpack()
        self.pack(expand=True, fill='both')
        self.create_widgets()
    
    def create_widgets(self):
        # イメージの保存用の変数定義
        self.image_data = None
        # キャンバス作成
        self.cv = tk.Canvas(self,width=300, height=300)
        # キャンバスをパック
        self.cv.pack(expand=True, fill='both')
        # 最初のshow_time()関数呼び出し（１回だけ）
        self.show_time()
 
 
    def clock_image(self): 
        tm = datetime.datetime.now()
        tmhour = tm.hour%12
        tmminute = tm.minute
        tmsecond = tm.second
        
        # 時計の文字盤描画
        canvas = Image.new('RGBA', (300, 300), (255,255,255,0))
        draw = ImageDraw.Draw(canvas)
        for i in range(1,13):
            draw.line((280, 150, 300, 150), fill='white', width=2)
            canvas = canvas.rotate(30)
            draw = ImageDraw.Draw(canvas)
 
        # 時針の描画
        imhour = Image.new('RGBA', (300, 300), (255,255,255,0))
        drawhour = ImageDraw.Draw(imhour)
        drawhour.polygon((150,150)+(175,140)+(250,150)+(175,160),fill='green')
        imhour = imhour.rotate(-(tmhour*30+tmminute//2-90))
        canvas.paste(imhour,(0,0),imhour)
        
        # 分針の描画
        imminute = Image.new('RGBA', (300, 300), (255,255,255,0))
        drawminute = ImageDraw.Draw(imminute)
        drawminute.polygon((150,150)+(180,145)+(270,150)+(180,155),fill='blue')
        imminute = imminute.rotate(-(tmminute*6-90))
        canvas.paste(imminute,(0,0),imminute)
        
        # 秒針の描画
        imsecond = Image.new('RGBA', (300, 300), (255,255,255,0))
        drawsecond = ImageDraw.Draw(imsecond)
        drawsecond.line((150,150)+(270,150), fill='red', width=2)
        imsecond = imsecond.rotate(-(tmsecond*6-90))
        canvas.paste(imsecond, (0,0), imsecond)
 
        #return canvas
 
        # 背景を写真にして時計を貼り付け。
        # ファイルの場所は実行環境に合わせて修正
        fname = os.path.dirname(__file__) + "/data/Lenna.jpg"
        bg = Image.open(fname)
        bg = bg.resize(size=(300,300))
        bg.paste(canvas,(0,0),canvas)
        return bg
        
    def show_time(self):
        # キャンバス上のオブジェクトをすべて削除
        self.cv.delete("all")
        # ウインドウサイズの取得
        w = self.cv.winfo_width()
        h = self.cv.winfo_height()
        # 縦横小さい方をsizeにする
        size = w if w < h else h
        # アナログ時計のイメージ作成（毎秒）
        image = self.clock_image()
        # 縦横同じサイズでリサイズする
        image = image.resize((size,size))
        # PILのイメージをTkinterのイメージ形式に変換
        self.image_data = ImageTk.PhotoImage(image)
        # キャンバスにアナログ時計のイメージを貼り付ける
        self.cv.create_image(w//2, h//2,image=self.image_data)
        # 1秒後に再呼び出し
        self.after(1000,self.show_time)
 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("tkClock")
    aclock = AClock(master = root)
    aclock.mainloop()
    