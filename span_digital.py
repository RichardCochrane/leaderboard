"""League Ranker

Usage:
  span_digital.py <file>
  span_digital.py (-s | --stdin)
  span_digital.py (-l | --live) <file>
  span_digital.py (-h | --help)

Options:
  -s --stdin    Capture input via standard input
  -h --help     Show this screen.
  -l --live     Show a live update of the match processing

Description:
  Reads match results from a file or stdin and outputs a ranked league table.
  Each input line should have the format: "Team A 1, Team B 2"
"""

import sys


from docopt import docopt

from ranker.input_validation import validate_input
from ranker.league_table_draw import render_results_in_live_table
from ranker.league_table import LeagueTable


def run_league_ranker():
    """Run the script that will either read matches from stdin or a file and evaluate the scores."""
    args = docopt(__doc__)
    lines = []

    if args["<file>"]:
        with open(args["<file>"], "r", encoding="utf-8") as f:
            lines = f.readlines()
    elif args.get("--stdin"):
        print("Enter match results (Ctrl+D to finish):")
        lines = sys.stdin.readlines()

    valid_matches, errors = validate_input(lines)

    if errors:
        print("\n🛑 Input validation found the following issues:\n")
        for line_no, error in errors:
            print(f"  Line {line_no}: {error}")

        print(f"\n✅ {len(valid_matches)} valid line(s), ❌ {len(errors)} invalid line(s)\n")
        proceed = input("Proceed with valid lines only? (y/N): ").strip().lower()
        if proceed != "y":
            print("Aborted")
            return

    matches = valid_matches

    if args.get("--live"):
        render_results_in_live_table(matches)
    else:
        table = LeagueTable()
        for match in matches:
            table.process_match(match)

        table.print_output()


if __name__ == "__main__":
    run_league_ranker()
