from Players.Keeper import Keeper
from Players.Midfielder import Midfielder
from Players.Defender import Defender
from Players.Striker import Striker
from Team import Team
from Match import Match

k = Keeper("Gordon Banks", 22, 99)
print(k.name)

team1 = Team(
    "Charlton Athletics",
    Keeper("", 20, 40),
    [Defender("",20,40), Defender("",20,40), Defender("",20,40), Defender("",20,40)],
    [Midfielder("",20,40), Midfielder("",20,40), Midfielder("",20,40), Midfielder("",20,40), Midfielder("",20,40)],
    [Striker("",20,40)]
)

team2 = Team(
    "Barnsley",
    Keeper("", 20, 40),
    [Defender("",20,40), Defender("",20,40), Defender("",20,40), Defender("",20,40)],
    [Midfielder("",20,40), Midfielder("",20,40), Midfielder("",20,40), Midfielder("",20,40)],
    [Striker("",20,40), Striker("",20,40)]
)

m = Match(team1, team2)
while not m.complete_match():
    m.evaluate_minute()

print("The game is over")
print(f"The final score is {m.get_score()}")
print(f"The game possession was split {m.get_possession()}")
