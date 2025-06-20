"""This class records the scores of all team games entered into it."""
from collections import defaultdict

from ranker.match import MatchResult


class LeagueTable:
    """This class records the scores of all team games entered into it."""

    def __init__(self):
        """Initialise the LeagueTable."""
        self.scores = defaultdict(int)

    def process_match(self, match: MatchResult) -> None:
        """Update the scores of the two teams based on who won or if they drew."""
        team1_points, team2_points = match.get_points()
        self.scores[match.team1.name] += team1_points
        self.scores[match.team2.name] += team2_points

    def get_rankings(self) -> list[int|str]:
        """Sort the teams in order of their scores and return the ranked data."""
        sorted_teams = sorted(self.scores.items(), key=lambda x: (-x[1], x[0]))

        rankings = []
        last_score = None
        current_rank = 0
        skip_rank = 0

        for idx, (team, score) in enumerate(sorted_teams, start=1):
            if score == last_score:
                skip_rank += 1
            else:
                skip_rank = 0
                current_rank = idx
                current_rank -= skip_rank
            pts_str = "pt" if score == 1 else "pts"

            rankings.append((current_rank, team, f"{score} {pts_str}"))
            last_score = score

        return rankings

    def print_output(self) -> None:
        """Return the rankings as a series of strings."""
        output = []
        rankings = self.get_rankings()
        for ranking in rankings:
            current_rank, team, score_in_points = ranking
            output.append(f"{current_rank}. {team}, {score_in_points}")

        print("\n⚽ Live League Results ⚽")
        print("\n".join(output))
