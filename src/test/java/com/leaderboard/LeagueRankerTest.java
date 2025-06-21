package com.leaderboard;

import org.junit.jupiter.api.Test;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LeagueRankerTest {

    @Test
    void testParseTeamValid() {
        var result = LeagueRanker.parseTeam("Lions 3");
        assertTrue(result.isPresent());
        assertEquals("Lions", result.get().name());
        assertEquals(3, result.get().score());
    }

    @Test
    void testParseTeamInvalid() {
        assertTrue(LeagueRanker.parseTeam("InvalidLine").isEmpty());
    }

    @Test
    void testComputeScoresAndRanking() {
        List<String> input = List.of(
                "Lions 3, Snakes 3",
                "Tarantulas 1, FC Awesome 0",
                "Lions 1, FC Awesome 1",
                "Tarantulas 3, Snakes 1",
                "Lions 4, Grouches 0"
        );
        List<String> errors = new ArrayList<>();
        Map<String, Integer> scores = LeagueRanker.computeScores(input, errors);

        List<String> expected = List.of(
                "1. Tarantulas, 6 pts",
                "2. Lions, 5 pts",
                "3. FC Awesome, 1 pt",
                "3. Snakes, 1 pt",
                "5. Grouches, 0 pts"
        );

        List<String> actual = LeagueRanker.rankTeams(scores);
        assertEquals(expected, actual);
    }
}
