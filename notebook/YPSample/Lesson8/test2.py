class Person:
  count=0
  def __init__(self,name,age):
    self.count=self.count
    self.name =name
    self.age=age
  
  def getName(self):
    return self.name
  
  def getAge(self):
    return self.age
  
  @classmethod
  def getCount(cls):
    return cls.count

pr1 = Person("鈴木",23)
pr2 = Person("佐藤",38)

print("合計人数は", Person.getCount(), "です。")



# a=10
# b=20
# def func(c):
#   b=b+c
#   print (a,b)

# func(30)


