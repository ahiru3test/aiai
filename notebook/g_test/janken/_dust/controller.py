from model import PlayerList
from view import View

class Controller:
    def __init__(self):
        self.model = PlayerList()
        self.view = View(self.model)

    def run(self):
        self.view.run()
