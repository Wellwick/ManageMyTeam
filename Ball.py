class Ball:
    def __init__(self):
        # Position can vary between 0-4
        # 0 is shooting range for team 2, defense team 1
        # 1 is midfield team 1
        # 2 is centre field for both teams
        # 3 and 4 is inverse of 1 and 0 for team 2
        self.position = 2