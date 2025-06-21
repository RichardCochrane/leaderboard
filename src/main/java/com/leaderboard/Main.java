package com.leaderboard;

import java.io.IOException;
import java.nio.file.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        List<String> lines;

        if (args.length > 0) {
            Path path = Paths.get(args[0]);
            lines = Files.readAllLines(path);
        } else {
            System.out.println("Enter match results (Ctrl+D to end):");
            Scanner scanner = new Scanner(System.in);
            lines = new ArrayList<>();
            while (scanner.hasNextLine()) {
                lines.add(scanner.nextLine());
            }
        }

        List<String> errors = new ArrayList<>();
        Map<String, Integer> scores = LeagueRanker.computeScores(lines, errors);

        if (!errors.isEmpty()) {
            System.out.println("\n🛑 Validation Errors:");
            errors.forEach(System.out::println);
            System.out.printf("\n✅ %d valid lines, ❌ %d invalid lines\n", lines.size() - errors.size(), errors.size());

            Scanner confirm = new Scanner(System.in);
            System.out.print("Proceed with valid lines only? (y/N): ");
            String input = confirm.nextLine().trim().toLowerCase();
            if (!input.equals("y")) {
                System.out.println("Aborted.");
                return;
            }
        }

        System.out.println("\n🏆 League Ranking:");
        LeagueRanker.rankTeams(scores).forEach(System.out::println);
    }
}
