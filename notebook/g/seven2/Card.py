class Card:
    # sort_keys = {"S":"0S","C":"1C","H":"2H","D":"3D"}

    def __init__(self, name:str, image=None):
        self.name = name
        self.image = image
        self.key = name.replace("S", "0S").replace("C", "1C").replace("H", "2H").replace("D", "3D")
    
    def __str__(self):
        return self.name
