class GameSeven():
    
class GameSevenInit(GameSevenBase):
    def __init__(self,g):
        self.g=g
    
    def init(self):
        pass


class GameSeven:
    def __init__(self):
        (gsi:=GameSevenInit(self)).init()
        # self.ginit(self,"")
        # self.ginput(self,)
        # self.logic()
        # self.gresolve()
        # self.gview()
    
    def test(self):
        print("test")

    def run(self):
        pass

if(__name__ == "__main__"):(gs:=GameSeven()).run()
