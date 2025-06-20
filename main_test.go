package main

import (
	"reflect"
	"testing"
)

func TestSplitTeamScore(t *testing.T) {
	tests := []struct {
		input    string
		wantTeam string
		wantScore int
		wantErr  bool
	}{
		{"Lions 3", "Lions", 3, false},
		{"FC Awesome 0", "FC Awesome", 0, false},
		{"NoScore", "", 0, true},
		{"Bad 3x", "", 0, true},
		{"", "", 0, true},
	}

	for _, test := range tests {
		team, score, err := splitTeamScore(test.input)
		if (err != nil) != test.wantErr {
			t.Errorf("splitTeamScore(%q) error = %v, wantErr = %v", test.input, err, test.wantErr)
		}
		if team != test.wantTeam || score != test.wantScore {
			t.Errorf("splitTeamScore(%q) = (%q, %d), want (%q, %d)", test.input, team, score, test.wantTeam, test.wantScore)
		}
	}
}

func TestValidateLine(t *testing.T) {
	tests := []struct {
		input     string
		wantErr   bool
		wantTeams [2]string
		wantScores [2]int
	}{
		{"Lions 3, Snakes 3", false, [2]string{"Lions", "Snakes"}, [2]int{3, 3}},
		{"Team 1, Another Team 0", false, [2]string{"Team", "Another Team"}, [2]int{1, 0}},
		{"OnlyOneTeam 3", true, [2]string{}, [2]int{}},
		{"BadScore, Team 2", true, [2]string{}, [2]int{}},
		{"Team A x, Team B 2", true, [2]string{}, [2]int{}},
	}

	for _, test := range tests {
		t1, t2, s1, s2, err := validateLine(test.input)
		if (err != nil) != test.wantErr {
			t.Errorf("validateLine(%q) error = %v, wantErr = %v", test.input, err, test.wantErr)
			continue
		}
		if !test.wantErr {
			if t1 != test.wantTeams[0] || t2 != test.wantTeams[1] || s1 != test.wantScores[0] || s2 != test.wantScores[1] {
				t.Errorf("validateLine(%q) = (%q, %q, %d, %d), want (%q, %q, %d, %d)",
					test.input, t1, t2, s1, s2, test.wantTeams[0], test.wantTeams[1], test.wantScores[0], test.wantScores[1])
			}
		}
	}
}

func TestRankTeams(t *testing.T) {
	input := map[string]int{
		"Tarantulas": 6,
		"Lions":      5,
		"FC Awesome": 1,
		"Snakes":     1,
		"Grouches":   0,
	}
	expected := []string{
		"1. Tarantulas, 6 pts",
		"2. Lions, 5 pts",
		"3. FC Awesome, 1 pt",
		"3. Snakes, 1 pt",
		"5. Grouches, 0 pts",
	}

	actual := rankTeams(input)
	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("rankTeams() = %v, want %v", actual, expected)
	}
}
