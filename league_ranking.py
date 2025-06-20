import sys
from collections import defaultdict
from typing import List, Tuple


class LeagueTable:
    def __init__(self):
        self.scores = defaultdict(int)

    def process_match(self, line: str):
        # Example: "Lions 3, Snakes 3"
        try:
            team1_info, team2_info = line.strip().split(", ")
            team1_name, team1_score = self._parse_team(team1_info)
            team2_name, team2_score = self._parse_team(team2_info)
        except Exception:
            raise ValueError(f"Invalid line format: '{line}'")

        team1_score = int(team1_score)
        team2_score = int(team2_score)

        if team1_score > team2_score:
            self.scores[team1_name] += 3
        elif team2_score > team1_score:
            self.scores[team2_name] += 3
        else:
            self.scores[team1_name] += 1
            self.scores[team2_name] += 1

    def _parse_team(self, s: str) -> Tuple[str, int]:
        *name_parts, score = s.strip().split()
        return " ".join(name_parts), int(score)

    def get_rankings(self) -> List[str]:
        sorted_teams = sorted(
            self.scores.items(),
            key=lambda x: (-x[1], x[0])
        )

        output = []
        last_score = None
        current_rank = 0
        skip_rank = 0

        for idx, (team, score) in enumerate(sorted_teams, start=1):
            if score == last_score:
                skip_rank += 1
            else:
                current_rank = idx
                current_rank -= skip_rank
                skip_rank = 0
            pts_str = "pt" if score == 1 else "pts"
            output.append(f"{current_rank}. {team}, {score} {pts_str}")
            last_score = score

        return output


def main():
    import argparse

    parser = argparse.ArgumentParser(description="League Table Calculator")
    parser.add_argument('file', nargs='?', help="Input file (defaults to stdin)")

    args = parser.parse_args()
    lines = []

    if args.file:
        with open(args.file) as f:
            lines = f.readlines()
    else:
        print("Enter match results (Ctrl+D to end):")
        lines = sys.stdin.readlines()

    table = LeagueTable()
    for line in lines:
        if line.strip():
            table.process_match(line)

    for row in table.get_rankings():
        print(row)


if __name__ == "__main__":
    main()
