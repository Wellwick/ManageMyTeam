from Team import Team
from Ball import Ball
import random

class Match:
    def __init__(self, team1: Team, team2: Team):
        self.score = {team1: 0, team2: 0}
        self.possession = {"now": team1, team1: 0, team2: 0}
        self.team1 = team1
        self.team2 = team2
        self.time = 0.0
        self.ball = Ball()

    def complete_match(self):
        return self.time >= 90

    def get_score(self) -> str:
        return f"{self.team1.name}: {self.score[self.team1]}\t-\t{self.team2.name}: {self.score[self.team2]}"

    def get_possession(self) -> str:
        return f"{self.team1.name}: {self.possession[self.team1]}\t-\t{self.team2.name}: {self.possession[self.team2]}"

    def evaluate_minute(self):
        if self.possession["now"] is self.team1:
            if self.ball.position == 4:
                self.shot_on_goal(self.team1, self.team2)
            elif self.ball.position == 0:
                if self.clearance(self.team1, self.team2):
                    self.ball.position = 1
                    #print(f"{self.time}: {self.team1.name} cleared the ball")
                else:
                    self.possession["now"] = self.team2
                    #print(f"{self.time}: {self.team2.name} claimed the ball")
            elif self.ball.position == 1:
                if self.contest(self.team1.midfield(), self.team2.striking()):
                    self.ball.position = 2
                    #print(f"{self.time}: {self.team1.name} moved the ball to centre pitch")
                else:
                    self.possession["now"] = self.team2
                    #print(f"{self.time}: {self.team2.name} claimed the ball")
            elif self.ball.position == 2:
                if self.contest(self.team1.midfield(), self.team2.striking()):
                    self.ball.position = 3
                    #print(f"{self.time}: {self.team1.name} moved the ball into {self.team2.name}'s half ")
                else:
                    self.possession["now"] = self.team2
                    #print(f"{self.time}: {self.team2.name} claimed the ball")
            elif self.ball.position == 3:
                if self.contest(self.team1.striking(), self.team2.defense()):
                    self.ball.position = 4
                    #print(f"{self.time}: {self.team1.name} gets in shooting range")
                else:
                    self.possession["now"] = self.team2
                    #print(f"{self.time}: {self.team2.name} claimed the ball")
        else:
            if self.ball.position == 0:
                self.shot_on_goal(self.team2, self.team1)
            elif self.ball.position == 4:
                if self.clearance(self.team2, self.team1):
                    self.ball.position = 3
                    #print(f"{self.time}: {self.team2.name} cleared the ball")
                else:
                    self.possession["now"] = self.team1
                    #print(f"{self.time}: {self.team1.name} claimed the ball")
            elif self.ball.position == 3:
                if self.contest(self.team2.midfield(), self.team1.striking()):
                    self.ball.position = 2
                    #print(f"{self.time}: {self.team2.name} moved the ball to centre pitch")
                else:
                    self.possession["now"] = self.team1
                    #print(f"{self.time}: {self.team1.name} claimed the ball")
            elif self.ball.position == 2:
                if self.contest(self.team2.midfield(), self.team1.striking()):
                    self.ball.position = 1
                    #print(f"{self.time}: {self.team2.name} moved the ball into {self.team1.name}'s half ")
                else:
                    self.possession["now"] = self.team1
                    #print(f"{self.time}: {self.team1.name} claimed the ball")
            elif self.ball.position == 1:
                if self.contest(self.team2.striking(), self.team1.defense()):
                    self.ball.position = 0
                    #print(f"{self.time}: {self.team2.name} gets in shooting range")
                else:
                    self.possession["now"] = self.team1
                    #print(f"{self.time}: {self.team1.name} claimed the ball")
        self.time += 1
        self.possession[self.possession["now"]] += 1
        if (self.time == 45):
            self.possession["now"] = self.team2
            self.ball.position = 2
            #print("Half Time!")

    def shot_on_goal(self, attacker, defender):
        striking = attacker.striking()
        goalkeeping = defender.goalkeeping()
        if goalkeeping > striking:
            percent = striking/goalkeeping
            percent *= percent
            scored = random.uniform(0.0,1.0) < percent
        else:
            percent = goalkeeping/striking
            percent *= percent
            scored = random.uniform(0.0,1.0) >= percent
        if scored:
            #print(f"{self.time}: {attacker.name} scored!")
            self.ball.position = 2
            self.score[attacker] += 1
            #print(f"Score is now {self.get_score()}")
        else:
            pass
            #print(f"{self.time}: {defender.name} defends a shot on goal")

        self.possession["now"] = defender

    def clearance(self, defenders, attackers):
        defense = defenders.defense()
        striking = attackers.striking()
        if defense > striking:
            return True
        else:
            return random.random(0, striking) < defense

    def contest(self, attack, defend):
        if attack > defend:
            percent = defend/attack
            percent *= percent*0.5
            return random.uniform(0.0,1.0) > percent
        else:
            return random.randrange(0, int(defend)*2) < attack