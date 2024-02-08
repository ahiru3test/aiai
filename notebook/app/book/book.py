# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.

# This program is distributed in the hopes that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.
# 675 Mass Ave, Cambridge, MA 02139, USA.

import os, sys
import time
import csv
import platform
import sqlite3

# db = "book.db"
db = os.path.dirname(__file__) + "/book.db"
conn = sqlite3.connect(db)
c = conn.cursor()
c.execute("select count(*) from sqlite_master where type='table' and name='books'")
n=c.fetchall()[0][0]
# Check that the table exists
if n == 0:
    # If the table books doesn't exist then create table
    c.execute("create table books(id INTEGER PRIMARY KEY, title VARCHAR(255), price INTEGER, memo TEXT)")
    c.execute("INSERT INTO books(title, price, memo) VALUES('Pythonチュートリアル',1800,'Guido van Rossum')")
    c.execute("INSERT INTO books(title, price, memo) VALUES('やさしいPython',2580,'高橋麻奈')")
    c.execute("INSERT INTO books(title, price, memo) VALUES('Pythonによる機械学習入門',2600,'株式会社システム計画研究所')")

conn.commit()
conn.close()
#file_err = open('book.log', 'w')
#ユーティリティ関数を定義します。
#  get_return(): "Press return "を表示して「Enter」キーの入力を待ちます。
#  get_confirm(): "Are you sure? "を表示して y,yes,Y,YESの入力を待ちます。
#  clear_screen(): ターミナル画面を消去します。
# =============================================================================
# def input_str(msg):
#     while True:
#         try:
#             print(msg, end="")
#             str_ = input()
#         except UnicodeDecodeError:
#             print("UnicodeDecodeError: Try again")
#             time.sleep(1)
#         else:
#             return str_
# =============================================================================
        
def get_return():
    return input("Press return ")

def get_confirm():

    while True:
        #print("Are you sure? ", end="")
        x = input("Are you sure? ")
        if x in ['y','yes','Y','Yes','YES']:
            return True

        if x in ['n','no', 'N', 'No', 'NO']:
            print("Cancelled")
            return False

        print("Please enter yes or no ", end="")
        time.sleep(1)

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')    # Windows
    else:
        os.system('clear') # Linux or Mac

#SQLiteデコレータ
# SQLiteにアクセスする関数をデコレートします。
#  データベース接続
#  カーソル取得
#  カーソルを引数にして被デコレート関数の呼び出し
#  データベースコミット
#  データベースクローズ
def sqlctl(func):
    def wrapper():
        conn = sqlite3.connect(db)
        c = conn.cursor()
        func(c)
        conn.commit()
        conn.close()
    return wrapper    

#新しい書籍の登録をします。
#  Title: 書籍のタイトルを入力します。
#  Price: 書籍の価格を入力します。
#  Memo: 書籍に関するメモを入力します。
@sqlctl
def add_book(c):
    print("add_book")
 
    title = input("Enter title: ")
 
    price = input("Enter price: ")
 
    memo = input("Entre memo: ")
 
    print()
    print("About to add new book")
    print("--------")
    #print("ID: ",id)
    print("Title: ",title)
    print("Price: ",price)
    print("Memo: ",memo)
    print("--------")
 
    if get_confirm():

        sql = "INSERT INTO books(title, price, memo)VALUES(?,?,?)"
        #print(sql, file=sys.stderr)
        c.execute(sql,(title,price,memo))
        print("Entry added")
 
    get_return()

#書籍の一覧を表示します。
#書籍が無い場合は カラム名だけを表示します。
@sqlctl
def list_book(c):
    print()
    print("{:^4} {:^6} {}".format("ID","Price","Title"))
    print("-"*26)

    itr = c.execute("SELECT * FROM books")
    for book in itr:
        print("{:>4} {:>6,d} {}".format(book[0],int(book[2]),book[1]))

    print()
    get_return()

#指定されたIDの書籍を削除します。
#  Enter ID to remove: 削除する書籍のIDを入力します。
#  IDに一致した書籍のデータを表示して get_confirm()関数で確認して削除します。
#  指定したIDの書籍がデータベース内に存在しないときは There is no book と表示しま
@sqlctl
def remove_book(c):
    print("remove_book")
 
    get_return()

#指定されたIDの書籍を更新します。
#  Enter ID to update: 更新する書籍のIDを入力します。
#  IDに一致した書籍のデータを表示して get_confirm()関数で確認します。
#  get_confirm()の戻り値がTureの場合書籍の更新をします。
#    Title: 書籍のタイトルを入力します。
#    Price: 書籍の価格を入力します
#    Memo: 書籍に関するメモを入力します。
#  指定したIDの書籍がデータベース内に存在しないときは There is no book と表示しま
@sqlctl
def update_book(c):
    print("update_book")
 
    get_return()

#書籍のデータを表示します。
#def show_book():
#    print("show_book")
#    get_return()
#    return
@sqlctl
def show_book(c):
    print("show_book")
 
    get_return()
#
#メニュー選択
#  main()から呼び出され選択メニューを表示し入力待ちをします。
#  入力選択されたメニュー(a～s,q)を呼び出し元のmain()関数に戻します。
def set_menu_choice() :
    #global cdcatnum

    clear_screen()

    print("Options :-")
    print
    print( "   a) Add new book")
    print( "   l) List book")
    print( "   r) Remove book")
    print( "   u) Update book")
    print( "   s) Show book")

    print( "   q) Quit")
    print()
    ret = input("Please enter choice then press return: ")
    return ret

#main() メイン関数
#  cleara_screen() 関数でターミナル画面の文字を消去します。
#  set_menu_choice() 関数でメニュー選択入力を待ちます。
#  メニュー選択された(a～s)に対応した処理関数を呼び出します。
#  q が選択されると処理を終了します。
def main():
    clear_screen()
    print()
    print()
    print("Mini Book manager")
    time.sleep(1)

    quit='n'
    while quit != "y":

        ret = set_menu_choice()
        if ret == "a":
            add_book()
        elif ret == "r":
            remove_book()
        elif ret == "u":
            update_book()
        elif ret == "l":
            list_book()
        elif ret == "s":
            show_book()

        elif ret == "q" or ret == "Q":
            #save_changes()
            print("Mini Book manager Finished")
            quit="y"
        else:
            print("Sorry, choice not recognized")
            time.sleep(1)

# Tidy up and leave
if __name__ == "__main__":
    main()
