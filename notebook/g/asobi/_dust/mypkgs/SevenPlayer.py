class SevenPlayer:
    player_names = ["Player1","Player2","Player3","Player4"]
    # players=[]

    # コンストラクタ
    # self.name
    # self.card_deck
    def __init__(self, name=""):
        # print(f"{len(SevenLoop.seven_players)}:name:{name}:type:{type(name)}")
        if name=="":
            self.name = SevenPlayer.player_names[len(SevenPlayer.players)]
        else:
            self.name = name
        
        self.card_deck = []

        pass
