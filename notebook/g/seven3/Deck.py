import copy, random
from Card import Card

class Deck:
  def __init__(self):
    self.card_deck:list[Card] = self.set_card_deck()

  def set_card_deck(self) -> list[Card] :
      card_deck =[]
      for s in ["S","C","H","D"]:
          for c in range(1,14,1):
              sss=s+str(c)
              # print(f"sss:{sss}")
              card_deck.append(Card(sss))
      # card_deck.sort()
      random.shuffle(card_deck)
      self.card_deck = copy.deepcopy(card_deck)
      return self.card_deck
