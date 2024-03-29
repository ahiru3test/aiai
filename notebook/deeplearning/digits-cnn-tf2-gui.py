# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
#import sys
from PIL import Image, ImageTk, ImageDraw

import tkinter as tk  # for Python 3
import os

# 入力画像の次元
img_rows, img_cols = 8, 8
#img_rows, img_cols = 28, 28

# 学習済ファイルを読み込んでmodelを作成
savefile = "digits_cnn.h5"
savefile = os.path.dirname(__file__) + '/' + savefile
model = tf.keras.models.load_model(savefile)

##### 以下はGUIアプリケーション用の内容

class Application(tk.Frame):
    # 初期化用関数
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.w = 200 # 一つの描画領域の幅
        self.h = 200 # 一つの描画領域の高さ
        self.d = 30  # マウスで描画する際の一点の直径
        #self.r = 20  # 旧バージョン用のフィルタ半径
        self.create_widgets()

    # 様々なGUI部品を構築
    def create_widgets(self):
        w = self.w
        h = self.h
        # マウスで描画するための領域
        self.canvas = tk.Canvas(self, width=w, height=h, bg='white')
        # self.canvasを左端に配置
        self.canvas.grid(row=0, column=0)
        # self.canvasでマウスが動いた際にself.draw_digitが実行されるよう設定
        self.canvas.bind('<Button1-Motion>', self.draw_digit)

        # 認識用に用いる画像(self.canvasと共通化不能)
        self.img = Image.new('L', (w, h), color=255)
        # self.img上に描画するために必要なdraw
        self.draw = ImageDraw.Draw(self.img)

        # 認識用に self.img を加工して表示するキャンバス
        self.recog_canvas = tk.Canvas(self, width=w, height=h, bg='white')
        # self.recog_canvas上に描画するための画像を生成して関連付け
        self.recog_img = tk.PhotoImage(width=w, height=h)
        self.recog_canvas.create_image((w/2,h/2), image=self.recog_img, state='normal')
        self.recog_canvas.image = self.recog_img
        # self.canvasを中央に配置
        self.recog_canvas.grid(row=0, column=1)

        # 結果表示用のキャンバス
        self.digit_canvas = tk.Canvas(self, width=w, height=h, bg='gray')
        # self.digit_canvasを右端に配置
        self.digit_canvas.grid(row=0, column=2)

        # 認識ボタン
        self.recog_btn = tk.Button(self, text='認識', command=self.recog)
        # 認識ボタンを下段左に配置
        self.recog_btn.grid(row=1, column=0)
        # クリアボタン
        self.clear_btn = tk.Button(self, text='クリア', command=self.clear)
        # クリアボタンを下段右に配置
        self.clear_btn.grid(row=1, column=2)

    # 認識ボタンが押されたときに実行される関数
    def recog(self):
        w = self.w
        h = self.h
        # 描画されたイメージを8x8のrecog_imgに縮小
        recog_img = self.img
        recog_img = recog_img.resize(size=(8,8), resample=Image.BICUBIC)
            
        # (8,8)のrecog_imgを描画用に拡大
        recog_img_large = recog_img.resize(size=(w, h))
        self.recog_img = ImageTk.PhotoImage(image=recog_img_large)
        self.recog_canvas.create_image((w/2, h/2), image=self.recog_img, state='normal')
        self.recog_canvas.image = self.recog_img

        # 8x8の画像を機械学習用に加工
        Ximg = np.asarray(recog_img, dtype=int)
        # 最大値を16に
        Ximg = 16*Ximg/255.0
        # 白黒反転
        Ximg = (16-Ximg)/16

        # 機械学習用データの完成
        # Tensorflow 2 最終層にsoftmaxがあるので直接インスタンスで呼び出し
        # 予測結果を右の領域の表示
        y = model(Ximg.reshape(1,img_rows,img_cols,1))
        y = [np.argmax(y.numpy())]
        self.digit_canvas.create_text(w/2, h/2, text = '{0:d}'.format(y[0]), fill='white', font = ('FixedSys', int(w/2)))   
    
    # クリアボタンが押されたときに実行される関数
    def clear(self):
        w = self.w
        h = self.h
        # 左の描画領域をクリア
        self.canvas.delete('all')
        self.draw.rectangle(xy=[0,0,w,h], 
                            outline='white', fill='white')
        # 中央の認識領域をクリア
        self.recog_canvas.delete('all')
        self.recog_img = tk.PhotoImage(width=w, height=h)
        self.recog_canvas.create_image((w/2,h/2), image=self.recog_img, state='normal')
        self.recog_canvas.image = self.recog_img
        # 右の結果表示領域をクリア
        self.digit_canvas.delete('all')

    # 左側の描画領域でマウスが動いたときに呼ばれる関数
    def draw_digit(self,event):
        d = self.d
        x = event.x
        y = event.y
        # 描画領域に黒丸を描画
        id=self.canvas.create_oval(x-d/2, y-d/2, x+d/2, y+d/2)
        self.canvas.itemconfigure(id, fill='black')
        # 認識用の画像に黒丸を描画
        self.draw.ellipse(xy=[x-d/2, y-d/2, x+d/2, y+d/2], fill=0, outline=0) 

root = tk.Tk()
app = Application(master=root)
app.master.title('digits数字認識 tf2')
app.mainloop()
