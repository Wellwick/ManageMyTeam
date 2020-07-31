from Players.Player import Player

class Midfielder(Player):
    def __init__(self, name, age, skill):
        super(Midfielder, self).__init__(name, age)
        self.skill = skill

