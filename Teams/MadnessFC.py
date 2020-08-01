from Players.Defender import Defender
from Players.Keeper import Keeper
from Players.Midfielder import Midfielder
from Players.Striker import Striker
from Team import Team

madness = Team(
    "Madness FC",
    Keeper("Ray Clements", 71, 82),
    [
        Defender("Trent Alexander-Arnold", 21, 83),
        Defender("Alan Hanson", 65, 81),
        Defender("Virgil Van Dijk", 28, 88),
        Defender("Alan Kennedy", 65, 80)
    ],
    [
        Midfielder("Graham Souness", 66, 79),
        Midfielder("Steven Gerard", 40, 83),
        Midfielder("Xabi Alonso", 40, 90)
    ],
    [
        Striker("Michael Owen", 40, 83),
        Striker("Sadio Mane", 29, 82),
        Striker("Kenny Dalglish", 69, 84)
    ]
)