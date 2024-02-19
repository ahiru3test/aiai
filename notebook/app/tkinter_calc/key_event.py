import tkinter as tk
 
root = tk.Tk()
 
def key(event):
    print( "pressed", repr(event.char))
    print("PRESSED", repr(event.keysym))
 
frame = tk.Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.focus_set()
frame.pack()
 
root.mainloop()
