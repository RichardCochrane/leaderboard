"""Run through the entries in the input and validate each entry as a MatchResult."""
from pydantic import ValidationError
from ranker.match import MatchResult, Team
from ranker.input_validation import validate_input

def validate_input(lines: list[str]) -> tuple[list[MatchResult], list[tuple[int, str]]]:
    """Run through the entries in the input and validate each entry as a MatchResult."""
    valid_matches = []
    errors = []
    for index, line in enumerate(lines, start=1):
        if not bool(line.strip()):
            errors.append((index, "empty line"))
            continue

        components = line.strip().split(",")
        if len(components) <= 1:
            errors.append((index, "invalid score pattern - only one 'team + score' pattern found"))
            continue
        elif len(components) > 2:
            errors.append((index, "invalid score pattern - too many 'team + score' patterns found"))
            continue

        team1_info, team2_info = components
        *team1_name, team1_score = team1_info.strip().split()
        *team2_name, team2_score = team2_info.strip().split()

        try:
            team1 = Team(name=" ".join(team1_name), score=team1_score)
            team2 = Team(name=" ".join(team2_name), score=team2_score)
            match_result = MatchResult(team1=team1, team2=team2)

            valid_matches.append(match_result)
        except ValidationError as validation_error:
            error = validation_error.errors()[0]
            errors.append((index, f"Invalid value for {error["loc"][0]} ({error["input"]}) - {error["msg"]}"))
    return valid_matches, errors


def test_validate_input_with_expected_data():
    """validate_input: returns success when the input data is all good."""
    valid_matches, errors = validate_input(["Orlando Pirates 3, Mamelodi Sundowns 5"])

    assert valid_matches == [
        MatchResult(Team(name="Orlando Pirates", score=3), Team(name="Mamelodi Sundowns", score=5))]

    assert errors == []


def test_validate_input_with_missing_comma():
    """validate_input: returns error when there are too few columns of data."""
    valid_matches, errors = validate_input(["Orlando Pirates 3"])

    assert not bool(valid_matches)

    assert errors == [(1, "invalid score pattern - only one 'team + score' pattern found")]


def test_validate_input_with_additional_commas():
    """validate_input: returns error when there are too many columns of data."""
    valid_matches, errors = validate_input(["Orlando Pirates 3, Mamelodi Sundowns 5, Pele Pele 2"])

    assert not bool(valid_matches)

    assert errors == [(1, "invalid score pattern - too many 'team + score' patterns found")]


def test_validate_input_with_invalid_negative_score():
    """validate_input: returns error when the team score is negative."""
    valid_matches, errors = validate_input(["Orlando Pirates 3, Mamelodi Sundowns -5"])

    assert not bool(valid_matches)

    assert errors == [
        (1, "Invalid value for score (-5) - Value error, score must be non-negative")
    ]


def test_validate_input_with_invalid_non_integer_score():
    """validate_input: returns error when the team score is not an integer."""
    valid_matches, errors = validate_input(
        [
            "Orlando Pirates A, Mamelodi Sundowns 5",
            "Pele Pele 2, Umvoti 5C",
        ])

    assert not bool(valid_matches)

    assert errors == [
        (1, (
            "Invalid value for score (A) - Input should be a valid integer, unable to parse "
            "string as an integer")),
        (2, (
            "Invalid value for score (5C) - Input should be a valid integer, unable to parse "
            "string as an integer"))
    ]


def test_validate_input_with_empty_line():
    """validate_input: returns error when the line is empty."""
    valid_matches, errors = validate_input(
        [
            "Orlando Pirates 3, Mamelodi Sundowns 5",
            "",
            "Pele Pele 2, Umvoti 5",
        ])

    assert valid_matches == [
        MatchResult(Team(name="Orlando Pirates", score=3), Team(name="Mamelodi Sundowns", score=5)),
        MatchResult(Team(name="Pele Pele", score=2), Team(name="Umvoti", score=5)),
        ]

    assert errors == [(2, "empty line")]
