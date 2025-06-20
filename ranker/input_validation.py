"""Run through the entries in the input and validate each entry as a MatchResult."""
from pydantic import ValidationError
from ranker.match import MatchResult, Team


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
