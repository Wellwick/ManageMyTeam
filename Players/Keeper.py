from Player import Player

class Keeper(Player):
    def __init__(self, name, age, skill):
        super(Keeper, self).__init__(name, age)
        self.skill = skill
