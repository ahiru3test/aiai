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

import os
import time
import csv
import platform
import sqlite3

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=False)
#engine = create_engine('sqlite:///book.db', echo=True)


from sqlalchemy.ext import declarative
Base = declarative.declarative_base()
from sqlalchemy import Column, Integer, Unicode, UnicodeText
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(100), nullable=False)
    price = Column(Integer, nullable=False)
    memo = Column(UnicodeText)
    def __repr__(self):
        return "<Book('%s', '%s', '%s')>" % (self.title, self.price, self.memo)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
query = session.query(Book)
count = query.count()
if count == 0:
    session.add_all([
        Book(title= 'Pythonチュートリアル', price='1800', memo = 'Guido van Rossum'),
        Book(title= 'やさしいPython', price='2580', memo = '高橋麻奈'),
        Book(title= 'Pythonによる機械学習入門', price='2600', memo = '株式会社システム計画研究所'),
    ])
    session.commit()

#ユーティリティ関数を定義します。
#  get_return(): "Press return "を表示して「Enter」キーの入力を待ちます。
#  get_confirm(): "Are you sure? "を表示して y,yes,Y,YESの入力を待ちます。
#  clear_screen(): ターミナル画面を消去します。
def get_return():
    return input("Press return ")

def get_confirm():

    while True:
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

#新しい書籍の登録をします。
#  Title: 書籍のタイトルを入力します。
#  Price: 書籍の価格を入力します
#  Memo: 書籍に関するメモを入力します。
def add_book():

    title = input("Enter title: ")

    price = input("Enter price: ")

    memo = input("Entre memo: ")

    print()
    print("About to add new book")
    print("--------")
    print("ID: ",id)
    print("Title: ",title)
    print("Price: ",price)
    print("Memo: ",memo)
    print("--------")

    if get_confirm():

        book = Book(title = title, price = price, memo = memo)
        session.add(book)
        session.commit()
        print("Entry added")
    get_return()
    return

#書籍の一覧を表示します。
#書籍が無い場合は カラム名だけを表示します。
def list_book():

    print()
    print("{:^4} {:^6} {}".format("ID","Price","Title"))
    print("-"*26)
    query = session.query(Book)
    for book in query:
        print("{:>4} {:>6,d} {}".format(book.id,int(book.price),book.title))

    get_return()
    return

#指定されたIDの書籍を削除します。
#  Enter ID to remove: 削除する書籍のIDを入力します。
#  IDに一致した書籍のデータを表示して get_confirm()関数で確認して削除します。
#  指定したIDの書籍がデータベース内に存在しないときは There is no book と表示しま
def remove_book():
    print("remove_book")
    get_return()
    return

#指定されたIDの書籍を更新します。
#  Enter ID to update: 更新する書籍のIDを入力します。
#  IDに一致した書籍のデータを表示して get_confirm()関数で確認します。
#  get_confirm()の戻り値がTureの場合書籍の更新をします。
#    Title: 書籍のタイトルを入力します。
#    Price: 書籍の価格を入力します
#    Memo: 書籍に関するメモを入力します。
#  指定したIDの書籍がデータベース内に存在しないときは There is no book と表示しま
def update_book():
    print("update_book")
    get_return()
    return

#書籍のデータを表示します。
def show_book():
    print("show_book")
    get_return()
    return
#
#メニュー選択
#  main()から呼び出され選択メニューを表示し入力待ちをします。
#  入力選択されたメニュー(a～s,q)を呼び出し元のmain()関数に戻します。
def set_menu_choice() :
    global cdcatnum

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

# Now the application proper
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
