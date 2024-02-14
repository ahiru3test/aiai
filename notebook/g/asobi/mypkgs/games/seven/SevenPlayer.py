class SevenPlayer:
    default_players = ["Player1","Player2","Player3","Player4"]
    def __init__(self,no,name=""):
        if name == "":
            name = SevenPlayer.default_players[no]
        self.name = name
        self.card_deck = []



if (__name__=="__main__") :
    l= []
    l.append(SevenPlayer(0,"test1"))
    l.append(SevenPlayer(1,"test2"))
    l.append(SevenPlayer(2))
    l.append(SevenPlayer(3))
    for sp in l:
      print(f"{sp.name} {sp.card_deck}")
