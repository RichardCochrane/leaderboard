package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

// TeamScore stores team name and points
type TeamScore struct {
	Name  string
	Score int
}

// readLines reads lines from a file or stdin
func readLines(filename string) ([]string, error) {
	var scanner *bufio.Scanner
	var file *os.File
	var err error

	if filename != "" {
		file, err = os.Open(filename)
		if err != nil {
			return nil, err
		}
		defer file.Close()
		scanner = bufio.NewScanner(file)
	} else {
		fmt.Println("Enter match results (Ctrl+D to finish):")
		scanner = bufio.NewScanner(os.Stdin)
	}

	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

// validateLine attempts to validate and parse a line
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

func promptUser() bool {
	fmt.Print("Proceed with valid lines only? (y/N): ")
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	text = strings.TrimSpace(strings.ToLower(text))
	return text == "y"
}

func main() {
	var filename string
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

	lines, err := readLines(filename)
	if err != nil {
		fmt.Println("Error reading input:", err)
		os.Exit(1)
	}

	scores := make(map[string]int)
	validLines := []string{}
	errors := []string{}

	for i, line := range lines {
		if strings.TrimSpace(line) == "" {
			continue
		}
		team1, team2, score1, score2, err := validateLine(line)
		if err != nil {
			errors = append(errors, fmt.Sprintf("Line %d: %s", i+1, err.Error()))
			continue
		}
		validLines = append(validLines, line)

		if score1 > score2 {
			scores[team1] += 3
		} else if score2 > score1 {
			scores[team2] += 3
		} else {
			scores[team1]++
			scores[team2]++
		}
	}

	if len(errors) > 0 {
		fmt.Println("\n🛑 Validation errors:")
		for _, e := range errors {
			fmt.Println("  ", e)
		}
		fmt.Printf("\n✅ %d valid line(s), ❌ %d invalid line(s)\n", len(validLines), len(errors))
		if !promptUser() {
			fmt.Println("Aborted.")
			return
		}
	}

	rankings := rankTeams(scores)
	for _, r := range rankings {
		fmt.Println(r)
	}
}

// rankTeams sorts and ranks the teams
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
