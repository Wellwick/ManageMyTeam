from Players.Player import Player

class Defender(Player):
    def __init__(self, name, age, skill):
        super(Defender, self).__init__(name, age)
        self.skill = skill

