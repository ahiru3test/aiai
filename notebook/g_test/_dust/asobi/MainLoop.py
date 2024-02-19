from .mypkgs.games.seven import GameSeven

class MainLoop:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def run(self):
        gs = GameSeven()
        gs.run()
        pass

if (__name__=="__main__"):
    ml = MainLoop()
    ml.run()
