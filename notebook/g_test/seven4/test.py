def bbb():
    print("bbb")

def ccc():
    print("ccc")

a = {"bbb":bbb,"ccc":ccc}

a["bbb"]()

#---

class ddd:
    def __init__(self):
        self.name="ddd"
        pass
class eee:
    def __init__(self):
        self.name="eee"
        pass

d = {"ddd":ddd,"eee":eee}
cls=d["ddd"]()
print(cls.name)
