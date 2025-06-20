"""Render the league results in real-time."""
import time

from rich.live import Live
from rich.table import Table

from ranker.league_table import LeagueTable
from ranker.match import MatchResult

# Sample team scores
teams = {
    "Lions": 0,
    "Tigers": 0,
    "Bears": 0,
    "Wolves": 0
}

def make_table(rankings: list[int|str], ranking_changes: dict[str, str]):
    """
    Create the table structure necessary for the "rich" library to render it.

    rankings:        a list of the tuples with ranking data
    ranking_changes: a dictionary of all teams and their change from the previous round
    """
    table = Table(title="⚽ Live League Results ⚽")

    table.add_column("Position", justify="center", style="yellow")
    table.add_column("Team", style="cyan", no_wrap=True)
    table.add_column("Score", justify="right", style="magenta")
    table.add_column("Change")

    for ranking in rankings:
        current_rank, team, score_in_points = ranking
        table.add_row(str(current_rank), team, score_in_points, ranking_changes[team])

    return table


def render_results_in_live_table(matches: list[MatchResult]) -> None:
    """Render the league results in a live redraw as each match is processed."""
    table = LeagueTable()
    previous_rankings = {}
    ranking_changes = {}

    with Live(make_table(table.get_rankings(), ranking_changes), refresh_per_second=4) as live:
        for match in matches:
            table.process_match(match)

            # Update the table
            current_rankings = table.get_rankings()
            ranking_changes = _compare_rankings(current_rankings, previous_rankings)
            live.update(make_table(current_rankings, ranking_changes))
            previous_rankings = current_rankings
            time.sleep(0.5)


def _compare_rankings(current_rankings: list[int|str], previous_rankings: list[int|str]) -> dict[str, str]:
    """
    Compare the current rankings with the previous rankings and return the changes.

    The changes will take the form of:
    ⇑   The team improved in rank
    ⇓   The team worsened in rank
    ⇐   The team entered the league
        No change (blank)
    """
    changes = {}

    # Turn both rankings into a dictionary for speedy lookups
    current_ranks = {rank[1]: rank[0] for rank in current_rankings}
    previous_ranks = {rank[1]: rank[0] for rank in previous_rankings}

    # Because the current rankings will always include the entries from the previous rankings,
    # we can simply iterate through the current rankings and assess the changes, noting that
    # there may be new entries but no missing ones (from previous rankings)
    for team, rank in current_ranks.items():
        if team in previous_ranks:
            difference = previous_ranks[team] - rank
            if difference:
                change = f"[red]⇓ ({difference})" if difference < 0 else f"[green]⇑ (+{difference})"
            else:
                change = ""
        else:
            change = "[blue]⇐"

        changes[team] = change

    return changes
