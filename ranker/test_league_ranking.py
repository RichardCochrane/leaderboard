import pytest
from ranker.span_digital import LeagueTable
from ranker.match import Team, MatchResult


def test_single_match_win():
    """get_rankings: returns rankings following a win/loss match."""
    table = LeagueTable()
    table.process_match(MatchResult(Team(name="Lions", score=2), Team(name="Snakes", score=1)))
    rankings = table.get_rankings()
    assert rankings == [
        (1, "Lions", "3 pts"),
        (2, "Snakes", "0 pts")
    ]


def test_single_match_draw():
    """get_rankings: returns rankings following a draw match."""
    table = LeagueTable()
    table.process_match(MatchResult(Team(name="Lions", score=1), Team(name="Snakes", score=1)))
    rankings = table.get_rankings()
    assert rankings == [
        (1, "Lions", "1 pt"),
        (1, "Snakes", "1 pt")
    ]


def test_multiple_matches_and_ranking():
    """get_rankings: returns rankings following a series of matches."""
    table = LeagueTable()
    matches = [
        MatchResult(Team(name="Lions", score=3), Team(name="Snakes", score=3)),
        MatchResult(Team(name="Tarantulas", score=1), Team(name="FC Awesome", score=0)),
        MatchResult(Team(name="Lions", score=1), Team(name="FC Awesome", score=1)),
        MatchResult(Team(name="Tarantulas", score=3), Team(name="Snakes", score=1)),
        MatchResult(Team(name="Lions", score=4), Team(name="Grouches", score=0)),
    ]
    for match in matches:
        (table.process_match(match))

    expected = [
        (1, "Tarantulas", "6 pts"),
        (2, "Lions", "5 pts"),
        (3, "FC Awesome", "1 pt"),
        (3, "Snakes", "1 pt"),
        (5, "Grouches", "0 pts")
    ]
    assert table.get_rankings() == expected


def test_team_with_spaces():
    """get_rankings: still ranks correctly given teams with spaces in their names."""
    table = LeagueTable()
    table.process_match(
        MatchResult(Team(name="Real Madrid", score=2), Team(name="Manchester United", score=2)))
    rankings = table.get_rankings()
    assert rankings == [
        (1, "Manchester United", "1 pt"),
        (1, "Real Madrid", "1 pt")
    ]


def test_rank_tie_sorting_alphabetically():
    """get_rankings: returns rankings alphabetically in the event of ties."""
    table = LeagueTable()
    table.process_match(MatchResult(Team(name="B Team", score=1), Team(name="C Team", score=1)))
    table.process_match(MatchResult(Team(name="A Team", score=0), Team(name="D Team", score=0)))
    rankings = table.get_rankings()
    assert rankings == [
        (1, "A Team", "1 pt"),
        (1, "B Team", "1 pt"),
        (1, "C Team", "1 pt"),
        (1, "D Team", "1 pt"),
    ]
