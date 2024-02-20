class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.choice_entry = None  # Add this line

    def choose(self, choice):
        self.choice = choice

class PlayerList:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    # def get_winner(self):
    #     # プレイヤーの選択を取得する
    #     choices = [player.choice for player in self.players]

    #     # 勝者を決める
    #     if choices.count("グー") == 3:
    #         return None  # 引き分け
    #     elif choices.count("グー") == 2:
    #         return [player for player in self.players if player.choice == "チョキ"]
    #     elif choices.count("グー") == 1:
    #         return [player for player in self.players if player.choice == "パー"]
    #     elif choices.count("チョキ") == 3:
    #         return None  # 引き分け
    #     elif choices.count("チョキ") == 2:
    #         return [player for player in self.players if player.choice == "パー"]
    #     elif choices.count("チョキ") == 1:
    #         return [player for player in self.players if player.choice == "グー"]
    #     elif choices.count("パー") == 3:
    #         return None  # 引き分け
    #     elif choices.count("パー") == 2:
    #         return [player for player in self.players if player.choice == "グー"]
    #     elif choices.count("パー") == 1:
    #         return [player for player in self.players if player.choice == "チョキ"]

def get_winner(self):
    # Get the choices of all players
    choices = [player.choice for player in self.players]

    # Check if all players chose the same option
    if len(set(choices)) == 1:
        return None  # Draw

    # Otherwise, determine the winner(s)
    else:
        # Create a dictionary to count the number of occurrences of each choice
        choice_counts = {}
        for choice in choices:
            if choice not in choice_counts:
                choice_counts[choice] = 0
            choice_counts[choice] += 1

        # Get the choice(s) with the highest count
        max_count = max(choice_counts.values())
        winning_choices = [choice for choice, count in choice_counts.items() if count == max_count]

        # Get the player(s) who chose the winning choice(s)
        winners = [player for player in self.players if player.choice in winning_choices]

        return winners
