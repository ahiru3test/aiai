#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
 
root = tk.Tk()
root.title("Raidobutton機能")
root.geometry("200x180")
 
 
 
# 選択ボタンの確定
def commit():
    btn = v1.get()
 
    if btn == 1:
        radio12.configure(state = "disabled")
 
    elif btn == 2:
        radio11.configure(state = "disabled")
 
    btn = v2.get()
    if btn == 1:
        radio22.configure(state = "disabled")
 
    elif btn == 2:
        radio21.configure(state = "disabled")
 
 
v1 = tk.IntVar()
v1.set(0)
v2 = tk.IntVar()
v2.set(0)
# Frameの生成と配置
frame1 = tk.LabelFrame(root, text = "Group1")
frame1.pack()
# ラジオボタン・オブジェクトの生成と配置
radio11 = tk.Radiobutton(frame1, text ="選択項目#1", variable=v1, value=1)
radio11.pack()
 
radio12 = tk.Radiobutton(frame1, text ="選択項目#2", variable=v1, value=2)
radio12.pack()
 
# Frameの生成と配置
frame2 = tk.LabelFrame(root ,text= "Group2")
frame2.pack()
# ラジオボタン・オブジェクトの生成と配置
radio21 = tk.Radiobutton(frame2, text ="選択項目#1", variable=v2, value=1)
radio21.pack()
 
radio22 = tk.Radiobutton(frame2, text ="選択項目#2", variable=v2, value=2)
radio22.pack()
 
# RESETボタンの生成と配置
restbtn = tk.Button(text="COMMIT", command = commit)
restbtn.pack()
 
root.mainloop()
