import random


ALL_TEAMS = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton and Hove Albion",
    "Burnley",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Leeds United",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Sunderland",
    "Tottenham Hotspur",
    "West Ham United",
    "Wolverhampton Wanderers",
]

GAMES = 1000

def generate_sample_file():
    """Create a file with many games for better testing."""
    with open("sample_input_large.txt", "w", encoding="utf-8") as file:
        for x in range(GAMES):
            teams = random.sample(ALL_TEAMS, 2)
            scores = (random.randint(0, 7), random.randint(0, 7))
            file.write(f"{teams[0]} {scores[0]}, {teams[1]} {scores[1]}\n")


if __name__ == "__main__":
    generate_sample_file()
