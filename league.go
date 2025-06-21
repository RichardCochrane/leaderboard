package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

type TeamScore struct {
	Name  string
	Score int
}

// Parses a string like "Lions 3" into ("Lions", 3)
func splitTeamScore(s string) (string, int, error) {
	parts := strings.Fields(s)
	if len(parts) < 2 {
		return "", 0, fmt.Errorf("not enough parts")
	}
	score, err := strconv.Atoi(parts[len(parts)-1])
	if err != nil {
		return "", 0, fmt.Errorf("invalid score: %s", parts[len(parts)-1])
	}
	team := strings.Join(parts[:len(parts)-1], " ")
	return team, score, nil
}

// Parses a full line like "Lions 3, Snakes 3"
func validateLine(line string) (string, string, int, int, error) {
	parts := strings.Split(line, ", ")
	if len(parts) != 2 {
		return "", "", 0, 0, fmt.Errorf("expected 2 teams separated by ', '")
	}
	team1, score1, err := splitTeamScore(parts[0])
	if err != nil {
		return "", "", 0, 0, fmt.Errorf("team1 error: %v", err)
	}
	team2, score2, err := splitTeamScore(parts[1])
	if err != nil {
		return "", "", 0, 0, fmt.Errorf("team2 error: %v", err)
	}
	return team1, team2, score1, score2, nil
}

// Takes a map of team scores and returns formatted leaderboard lines
func rankTeams(scores map[string]int) []string {
	teams := make([]TeamScore, 0, len(scores))
	for name, score := range scores {
		teams = append(teams, TeamScore{name, score})
	}

	sort.Slice(teams, func(i, j int) bool {
		if teams[i].Score == teams[j].Score {
			return teams[i].Name < teams[j].Name
		}
		return teams[i].Score > teams[j].Score
	})

	var output []string
	rank := 0
	skip := 0
	lastScore := -1

	for i, team := range teams {
		if team.Score != lastScore {
			rank = i + 1 - skip
		} else {
			skip++
		}
		pts := "pts"
		if team.Score == 1 {
			pts = "pt"
		}
		output = append(output, fmt.Sprintf("%d. %s, %d %s", rank, team.Name, team.Score, pts))
		lastScore = team.Score
	}
	return output
}
