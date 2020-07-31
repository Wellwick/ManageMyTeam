from Players.Player import Player

class Striker(Player):
    def __init__(self, name, age, skill):
        super(Striker, self).__init__(name, age)
        self.skill = skill

