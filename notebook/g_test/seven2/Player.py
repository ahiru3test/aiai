class Player:
    default_players = ["Player1","Player2","Player3","Player4"]
    def __init__(self,no,name=""):
        self.ctrl=no
        self.cpu=False
        if name == "":
            name = Player.default_players[no]
            self.cpu = True
        self.name = name
        self.card_deck = []
