import pytest
from ranker.span_digital import LeagueTable


def test_single_match_win():
    table = LeagueTable()
    table.process_match("Lions 2, Snakes 1")
    rankings = table.get_rankings()
    assert rankings == [
        "1. Lions, 3 pts",
        "2. Snakes, 0 pts"
    ]


def test_single_match_draw():
    table = LeagueTable()
    table.process_match("Lions 1, Snakes 1")
    rankings = table.get_rankings()
    assert rankings == [
        "1. Lions, 1 pt",
        "1. Snakes, 1 pt"
    ]


def test_multiple_matches_and_ranking():
    table = LeagueTable()
    matches = [
        "Lions 3, Snakes 3",
        "Tarantulas 1, FC Awesome 0",
        "Lions 1, FC Awesome 1",
        "Tarantulas 3, Snakes 1",
        "Lions 4, Grouches 0"
    ]
    for match in matches:
        table.process_match(match)

    expected = [
        "1. Tarantulas, 6 pts",
        "2. Lions, 5 pts",
        "3. FC Awesome, 1 pt",
        "3. Snakes, 1 pt",
        "5. Grouches, 0 pts"
    ]
    assert table.get_rankings() == expected


def test_team_with_spaces():
    table = LeagueTable()
    table.process_match("Real Madrid 2, Manchester United 2")
    rankings = table.get_rankings()
    assert rankings == [
        "1. Manchester United, 1 pt",
        "1. Real Madrid, 1 pt"
    ]


def test_rank_tie_sorting_alphabetically():
    table = LeagueTable()
    table.process_match("B Team 1, C Team 1")
    table.process_match("A Team 0, D Team 0")
    rankings = table.get_rankings()
    assert rankings == [
        "1. B Team, 1 pt",
        "1. C Team, 1 pt",
        "1. D Team, 1 pt",
        "1. A Team, 1 pt"
    ]


def test_invalid_input():
    table = LeagueTable()
    with pytest.raises(ValueError):
        table.process_match("Invalid Input Line")
