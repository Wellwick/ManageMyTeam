from Players.Defender import Defender
from Players.Keeper import Keeper
from Players.Midfielder import Midfielder
from Players.Striker import Striker
from Team import Team

charlton = Team(
    "Charlton Athletics",
    Keeper("Dillon Phillips",25, 70),
    [
        Defender("Adam Matthews",28, 65),
        Defender("Naby Sarr",27, 66),
        Defender("Jason Pearce", 31, 67),
        Defender("Ben Purrington", 24, 65)
    ],
    [
        Midfielder("Albie Morgan", 20, 62),
        Midfielder("Jonny Williams", 26, 70),
        Midfielder("Darren Pratley", 35, 72),
        Midfielder("Jake Forster-Caskey", 26, 68),
        Midfielder("Alfie Doughty", 20, 67)
    ],
    [
        Striker("Macauley Bonne", 24, 66)
    ]
)