from abc import ABC,abstractclassmethod

class GameBase:
    loop = True

    @classmethod
    @abstractclassmethod
    def init(self):
        pass

    @classmethod
    @abstractclassmethod
    def input(self):
        pass

    @classmethod
    @abstractclassmethod
    def logic(self):
        pass

    @classmethod
    @abstractclassmethod
    def check(self):
        pass

    @classmethod
    @abstractclassmethod
    def view(self):
        pass

    @classmethod
    @abstractclassmethod
    def loop(self):
      while(GameBase.loop):
          pass
