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

The UV environment manager has been used here but regular PIP could be used as well. To install UV:

```
# For Linux or WSL
curl -LsSf https://astral.sh/uv/install.sh | sh   (if curl is available)
wget -qO- https://astral.sh/uv/install.sh | sh

# For Mac OSX
brew install UV
```

Once uv is intalled (although regular pip could be used as well), install the project dependencies:
```
uv pip install requirements.txt
uv pip install dev_requirements.txt
```

## Running the script

### Vanilla Mode

The script can be run in it's regular mode using a variety of commands:
- `python ranker/span_digital.py -h` - will generate the help page
- `python ranker/span_digital.py -s` - will allow you to enter the match scores in, following the format described above, i.e. "<team name> <team score>, <team name> <team score>"
- `python ranker/span_digital.py <file_name>` - will allow you to have the script read the matches from a provided file. There are 3 files to play with:
  - `python ranker/span_digital.py sample_input.txt` - a very small list of matches
  - `python ranker/span_digital.py sample_input_with_errors.txt` - a small list of matches but frought with errors
  - `python ranker/span_digital.py sample_input_large.txt` - a larger list of 1000 matches played between English Premiere League teams (with made-up data)

### Live Mode

The scripts fancy mode is when the live mode is invoked. This will render the leaderboard live and update it as the matches are played, reflecting how teams are going up or down the leaderboard based on their matches. This is best seen with the large file, eg. `python ranker/span_digital.py sample_input_large.txt -l`


### Automated Tests

Run `pytest .` to run the test suite.


## Other Scripts

### Sample File Generation

By tweaking the script in `ranker/generate_sample_file.py`, very long random files can be created to test the script. To run it:
`python ranker/generate_sample_file.py`.
