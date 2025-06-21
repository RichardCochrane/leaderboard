package leaderboard

import org.scalatest.funsuite.AnyFunSuite
import leaderboard.TeamResult

class LeagueRankerTest extends AnyFunSuite {

  test("splitTeamResult should parse valid input") {
    val result = LeagueRanker.parseTeamResult("Lions 3")
    assert(result.isSuccess)
    assert(result.get == TeamResult("Lions", 3))
  }

  test("splitTeamResult should fail on invalid input") {
    val result = LeagueRanker.parseTeamResult("Broken")
    assert(result.isFailure)
  }

  test("validateLine should parse valid line") {
    val line = "Lions 2, Snakes 1"
    val result = LeagueRanker.validateLine(line)
    assert(result.isSuccess)
    val (team1, team2) = result.get
    assert(team1 == TeamResult("Lions", 2))
    assert(team2 == TeamResult("Snakes", 1))
  }

  test("validateLine should fail on invalid line") {
    val line = "InvalidLine"
    val result = LeagueRanker.validateLine(line)
    assert(result.isFailure)
  }

  test("rankTeams returns correctly ranked output") {
    val scores = Map(
      "Tarantulas" -> 6,
      "Lions" -> 5,
      "FC Awesome" -> 1,
      "Snakes" -> 1,
      "Grouches" -> 0
    )
    val expected = List(
      "1. Tarantulas, 6 pts",
      "2. Lions, 5 pts",
      "3. FC Awesome, 1 pt",
      "3. Snakes, 1 pt",
      "5. Grouches, 0 pts"
    )
    val actual = LeagueRanker.rankTeams(scores)
    assert(actual == expected)
  }
}
