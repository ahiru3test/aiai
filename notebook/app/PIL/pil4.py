# %matplotlib inline
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
 
# 時計の文字盤描画
canvas = Image.new('RGBA', (300, 300), (255,255,255,0))
draw = ImageDraw.Draw(canvas)
for i in range(12):
    draw.line((280, 150, 300, 150), fill='black', width=2)
    canvas = canvas.rotate(30)
    draw = ImageDraw.Draw(canvas)
 
plt.imshow(canvas)
plt.axis('off')
plt.show()
