from Players.Player import Player
from Players.Keeper import Keeper
from Players.Defender import Defender
from Players.Midfielder import Midfielder
from Players.Striker import Striker

class Team:
    def __init__(self, name: str, keeper: Keeper, defenders: [Defender],
                 midfielders: [Midfielder], strikers: [Striker]):
        self.name = name
        assert keeper is not None
        for player in defenders:
            assert player is not None
        for player in midfielders:
            assert player is not None
        for player in strikers:
            assert player is not None

        self.keeper = keeper
        self.defenders = defenders
        self.midfielders = midfielders
        self.strikers = strikers
        players = self.all_players()
        assert len(players) == 11

    def all_players(self) -> [Player]:
        players = [self.keeper]
        players += self.defenders
        players += self.midfielders
        players += self.strikers
        return players

    def goalkeeping(self):
        goalkeeping_skill = self.keeper.skill
        for i in self.defenders:
            goalkeeping_skill += (i.skill/4)
        return goalkeeping_skill

    def defense(self):
        defense_skill = 0.0
        for i in self.defenders:
            defense_skill += i.skill
        for i in self.midfielders:
            defense_skill += (i.skill/4)
        defense_skill += (self.keeper.skill/2)
        return defense_skill

    def midfield(self):
        midfielder_skill = 0.0
        for i in self.midfielders:
            midfielder_skill += (3*i.skill/4)
        for i in self.defenders:
            midfielder_skill += (i.skill/5)
        for i in self.strikers:
            midfielder_skill += (i.skill/3)
        return midfielder_skill

    def upfront(self):
        striker_skill = 0.0
        for i in self.strikers:
            striker_skill += i.skill
        for i in self.midfielders:
            striker_skill += (i.skill/4)
        return striker_skill
