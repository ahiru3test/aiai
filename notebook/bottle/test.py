import os
from pathlib import Path

# filename = os.path.dirname(__file__) + "/books.csv" #実行ファイルのパス
# filename = os.path.abspath(".") + "\\book\\books.csv" # For VScode
# filename = os.path.join(os.path.abspath("."), "aaa", "bbb", "ccc.txt") # 環境に応じてパスを生成する
# filename = os.path.join(os.path.abspath(__file__), "static").replace("\\","/")
# filename = (os.path.abspath(__path__) + "\\static").replace("\\","/")
filename = (os.path.dirname(__file__) + "\\static").replace("\\","/")
# filename = os.path.join(os.path.abspath("."), "aaa", "bbb", "ccc.txt").replace("\\","/") # 環境に応じてパスを生成する
print(filename)
