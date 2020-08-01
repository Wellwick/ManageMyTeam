from Match import Match
from Teams.CharltonAthletics import charlton
from Teams.MadnessFC import madness

winner = 0
games = 0
ca = 0
ma = 0
last_games=""
while winner < 3:
    m = Match(charlton, madness)
    while not m.complete_match():
        m.evaluate_minute()

    #print("The game is over")
    #print(f"The final score is {m.get_score()}")
    #print(f"The game possession was split {m.get_possession()}")
    if 10 < m.score[madness]:
        winner += 1
        last_games += f"{m.get_score()}\n"
    else:
        winner = 0
        last_games = ""
    games += 1
    ca += m.score[charlton]
    ma += m.score[madness]
    if (games % 10000 == 0):
        print(f"Just completed game {games}")

print(last_games)
print(f"There were {games} games")
print(f"That's {games*90} minutes of play, {ca} CA goals and {ma} Madness goals")

# It took about 2.7 million games for CA to beat ma 3 times in a row
# admittedly not very helpful considering it's a single data point