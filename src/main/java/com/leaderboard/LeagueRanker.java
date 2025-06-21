package com.leaderboard;

import java.util.*;
import java.util.regex.*;

public class LeagueRanker {

    public record TeamScore(String name, int score) {}

    public static Optional<TeamScore> parseTeam(String input) {
        var pattern = Pattern.compile("^(.*)\\s+(\\d+)$");
        var matcher = pattern.matcher(input.trim());
        if (matcher.find()) {
            String team = matcher.group(1).trim();
            int score = Integer.parseInt(matcher.group(2));
            return Optional.of(new TeamScore(team, score));
        }
        return Optional.empty();
    }

    public static Optional<String> validateLine(String line) {
        String[] parts = line.split(", ");
        if (parts.length != 2) return Optional.of("Line must contain two teams separated by ', '");

        var t1 = parseTeam(parts[0]);
        var t2 = parseTeam(parts[1]);
        if (t1.isEmpty() || t2.isEmpty()) return Optional.of("Invalid team format");
        return Optional.empty();
    }

    public static Map<String, Integer> computeScores(List<String> lines, List<String> errors) {
        Map<String, Integer> scores = new HashMap<>();

        int lineNum = 1;
        for (String line : lines) {
            Optional<String> error = validateLine(line);
            if (error.isPresent()) {
                errors.add("Line " + lineNum + ": " + error.get());
                lineNum++;
                continue;
            }

            String[] parts = line.split(", ");
            TeamScore t1 = parseTeam(parts[0]).get();
            TeamScore t2 = parseTeam(parts[1]).get();

            scores.putIfAbsent(t1.name, 0);
            scores.putIfAbsent(t2.name, 0);

            if (t1.score > t2.score) {
                scores.put(t1.name, scores.get(t1.name) + 3);
                scores.put(t2.name, scores.get(t2.name));
            }
            else if (t2.score > t1.score) {
                scores.put(t2.name, scores.get(t2.name) + 3);
                scores.put(t1.name, scores.get(t1.name));
            }
            else {
                scores.put(t1.name, scores.get(t1.name) + 1);
                scores.put(t2.name, scores.get(t2.name) + 1);
            }

            lineNum++;
        }

        return scores;
    }

    public static List<String> rankTeams(Map<String, Integer> scores) {
        List<Map.Entry<String, Integer>> sorted = new ArrayList<>(scores.entrySet());

        sorted.sort((a, b) -> {
            int scoreComp = b.getValue().compareTo(a.getValue());
            return (scoreComp != 0) ? scoreComp : a.getKey().compareTo(b.getKey());
        });

        List<String> output = new ArrayList<>();
        int lastScore = -1, rank = 0, skip = 0;

        for (int i = 0; i < sorted.size(); i++) {
            var entry = sorted.get(i);
            if (entry.getValue() != lastScore) {
                skip = 0;
                rank = i + 1 - skip;
            } else {
                skip++;
            }

            String label = entry.getValue() == 1 ? "pt" : "pts";
            output.add(rank + ". " + entry.getKey() + ", " + entry.getValue() + " " + label);
            lastScore = entry.getValue();
        }

        return output;
    }
}
