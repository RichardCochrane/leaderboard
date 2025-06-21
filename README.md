# League Leaderboards

Welcome! This is a script designed to rank a series of matches played between two teams and output the resulting placements.

## Details

The input for the program can be either entered via stdin or a file but in either case, the format must be:
<team name> <team score>, <team name> <team score>

It doesn't matter what order the teams are in. Some examples include:
```
Arsenal 3, Fulham 2
Crystal Palace 1, Sunderland 5
```

### Scoring

Each match will award the two teams a certain number of points based on the score:
- If it was a draw, both teams get 1 point
- Otherwise, the winning team gets 3 points and the losing team gets 0 points

When all games have been evaluated, the results will be ordered from the team with the most points to the team with the least.

## Installation

Install Coursier which contains everything needed to install and use Scala:

```
# For Linux or WSL
curl -fL https://github.com/coursier/coursier/releases/latest/download/cs-x86_64-pc-linux.gz | gzip -d > cs && chmod +x cs && ./cs setup

# For Mac OSX
brew install coursier/formulas/coursier && cs setup

```
It's not an unattended setup, so there will be some prompts to answer as part of installation.


## Running the scripts

```
# Running the ranker with the various files:

sbt "run sample_input.txt"
sbt "run sample_input_with_errors.txt"
sbt "run sample_input_large.txt"

# Running the ranker with manual input
sbt run

# For running the tests
sbt test
```
