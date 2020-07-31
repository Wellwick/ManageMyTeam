from Team import Team
from Ball import Ball

class Match:
    def __init__(self, team1: Team, team2: Team):
        self.score = {team1: 0, team2: 0}
        self.team1 = team1
        self.team2 = team2
        self.time = 0.0
        self.ball = Ball()
        self.possession = team1

    def complete_match(self):
        return self.time >= 90

    def get_score(self) -> str:
        return f"{self.team1.name}: {self.score[self.team1]}\t-\t{self.team2.name}: {self.score[self.team2]}"