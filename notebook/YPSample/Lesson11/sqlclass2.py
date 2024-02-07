import sqlite3
 
conn = sqlite3.connect("pdb.db")
 
c = conn.cursor()
 
c.execute("DROP TABLE IF EXISTS product")
 
c.execute("CREATE TABLE product(name CHAR(20), price INT)")
c.execute("INSERT INTO product VALUES('鉛筆', 80)")
c.execute("INSERT INTO product VALUES('消しゴム', 50)")
c.execute("INSERT INTO product VALUES('定規', 200)")
c.execute("INSERT INTO product VALUES('コンパス', 300)")
c.execute("INSERT INTO product VALUES('ボールペン', 100)")
 
conn.commit()
 
conn.close()
 
class Product:
    def __init__(self):
        self.__conn = sqlite3.connect("pdb.db")
        self.__c = self.__conn.cursor()
        
    def getAll(self):
        return self.__c.execute("SELECT * FROM product")
    
    def setRecord(self, name, price):
        self.__c.execute("INSERT INTO product VALUES(?,?)",(name,price))
        
    def getRecord(self, name):
        self.__c.execute("SELECT * FROM product WHERE name = ?", (name,))
        return list(self.__c.fetchall())
    
    def delRecord(self, name):
        self.__c.execute("DELETE FROM product WHERE name = ?", (name,))
    
    def __del__(self):
        print("deleted")
        self.__conn.commit()
        self.__conn.close()
        
p = Product()
 
p.__c = None
 
itr = p.getAll()
 
for row in itr:
    print(row)
    
# # p.setRecord("ハサミ",300)
p.delRecord('鉛筆')
 
itr = p.getAll()
print("----")
for row in itr:
    print(row)
    
# # print(p.getRecord('ハサミ'))
# インスタンス削除    
del p
