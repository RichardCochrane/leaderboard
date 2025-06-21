package leaderboard

import scala.io.StdIn.readLine
import scala.io.Source
import scala.util.{Try, Success, Failure}
import scala.collection.mutable
import scala.util.control.Breaks._

case class TeamResult(name: String, score: Int)
case class MatchLine(line: String, lineNumber: Int)

object LeagueRanker {

  def parseTeamResult(input: String): Try[TeamResult] = Try {
    val parts = input.trim.split(" ")
    val score = parts.last.toInt
    val team = parts.dropRight(1).mkString(" ")
    TeamResult(team, score)
  }

  def validateLine(line: String): Try[(TeamResult, TeamResult)] = Try {
    val teams = line.split(", ")
    if (teams.length != 2) throw new Exception("Expected 2 teams separated by ', '")
    val team1 = parseTeamResult(teams(0)).get
    val team2 = parseTeamResult(teams(1)).get
    (team1, team2)
  }

  def rankTeams(scoreMap: Map[String, Int]): List[String] = {
    val sorted = scoreMap.toList
      .sortBy { case (name, pts) => (-pts, name) }

    var output = List[String]()
    var rank = 0
    var skip = 0
    var lastScore: Option[Int] = None

    for (((name, score), index) <- sorted.zipWithIndex) {
      if (lastScore.contains(score)) {
        skip += 1
      } else {
        skip = 0
        rank = index + 1 - skip
      }
      val suffix = if (score == 1) "pt" else "pts"
      output :+= s"$rank. $name, $score $suffix"
      lastScore = Some(score)
    }

    output
  }

  def processMatches(lines: List[MatchLine]): (Map[String, Int], List[(Int, String)]) = {
    val scoreMap = mutable.Map[String, Int]().withDefaultValue(0)
    val errors = mutable.ListBuffer[(Int, String)]()

    for (MatchLine(line, lineNum) <- lines) {
      validateLine(line) match {
        case Success((t1, t2)) =>
          if (t1.score > t2.score) {
            scoreMap(t1.name) += 3
            scoreMap(t2.name) += 0
          } else if (t1.score < t2.score) {
            scoreMap(t1.name) += 0
            scoreMap(t2.name) += 3
          } else {
            scoreMap(t1.name) += 1
            scoreMap(t2.name) += 1
          }
        case Failure(e) =>
          errors += ((lineNum, e.getMessage))
      }
    }

    (scoreMap.toMap, errors.toList)
  }

  def readInput(fileOpt: Option[String]): List[MatchLine] = {
    val lines = fileOpt match {
      case Some(filename) => Source.fromFile(filename).getLines().toList
      case None =>
        println("Enter match results (enter quit when done):")
        Iterator.continually(readLine()).takeWhile{
            case null => false
            case l => l.trim.toLowerCase != "quit"
        }.toList
    }
    lines.zipWithIndex.map { case (line, idx) => MatchLine(line.trim, idx + 1) }.filter(_.line.nonEmpty)
  }

  def main(args: Array[String]): Unit = {
    val fileOpt = if (args.nonEmpty) Some(args(0)) else None
    val inputLines = readInput(fileOpt)

    val (scores, errors) = processMatches(inputLines)

    if (errors.nonEmpty) {
      println("\n🛑 Validation Errors:")
      errors.foreach { case (lineNum, msg) =>
        println(s"  Line $lineNum: $msg")
      }
      println(s"\n✅ ${inputLines.length - errors.length} valid lines, ❌ ${errors.length} invalid lines\n")

      print("Proceed with valid lines only? (y/N): ")
      val proceed = readLine().trim.toLowerCase
      if (proceed != "y") {
        println("Aborted.")
        return
      }
    }

    println("\n🏆 League Ranking:")
    rankTeams(scores).foreach(println)
  }
}
