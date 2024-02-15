from Deck import Deck
from Player import Player

class Players:
    def __len__(self):
        return len(self.players)
    
    def __init__(self,name:list[str],deck:Deck):
        self.players = []
        for n in range(0,4):
            str = ""
            if n<len(name):
                s=name[n]
            else:
                s=Player.player_names[n]
            self.players.append(Player(n,s))
        
        index = 0
        for c in deck.card_deck:
            # print(f"c2: {c}")
            if(c.name in "7"):
                if(c.name=="D7"):
                    self.top_index = index
            else:
                self.players[index].card_deck.append(c)

            index += 1
            if index >=4:
                index = 0
