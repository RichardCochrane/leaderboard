package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

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
			scores[team2] += 0
		} else if score2 > score1 {
			scores[team2] += 3
			scores[team1] += 0
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

	for _, line := range rankTeams(scores) {
		fmt.Println(line)
	}
}
