"""Data structures representing a match and the teams that played in the match."""
from pydantic.dataclasses import dataclass
from pydantic import Field, field_validator

SCORES = {
    "win": 3,
    "draw": 1,
    "loss": 0
}

@dataclass
class Team:
    """Data structure representing a team and it's score."""
    name: str = Field(..., description="Name of the team")
    score: int = Field(..., description="Score the team achieved")

    @field_validator('name')
    @classmethod
    def team_must_not_be_empty(cls, value):
        """The name must not be blank."""
        if not value.strip():
            raise ValueError("team name must not be empty")
        return value.strip()

    @field_validator('score')
    @classmethod
    def score_must_be_non_negative(cls, value):
        """The score must be a positive integer."""
        if value < 0:
            raise ValueError("score must be non-negative")
        return value


@dataclass
class MatchResult:
    """Data structure representing a match - guarantees the structure of the data."""
    team1: Team = Field(..., description="The first team")
    team2: Team = Field(..., description="The second team")

    def get_points(self):
        """
        Return the points of the teams based on their score.

        The result will be a tuple with first teams points then second teams points.
        """
        if self.team1.score > self.team2.score:
            return (SCORES["win"], SCORES["loss"])
        elif self.team2.score > self.team1.score:
            return (SCORES["loss"], SCORES["win"])
        else:
            return (SCORES["draw"], SCORES["draw"])
