# League Leaderboards (Python)

Welcome! This is a script designed to rank a series of matches played between two teams and output the resulting placements.

## Details

The input for the program can be either entered via standard input or a file but in either case, the format must be:

`<team name> <team score>, <team name> <team score>`

It doesn't matter what order the teams are in (i.e. winning team first or second). Some examples include:
```
Arsenal 3, Fulham 2
Crystal Palace 1, Sunderland 5
```

### Scoring

Each match will award the two teams a certain number of points based on the score:
- If it was a draw, both teams get 1 point
- Otherwise, the winning team gets 3 points and the losing team gets 0 points

When all of the games have been evaluated, the results will be ordered so that the team with the most points is at the top and the team with the least points at the bottom.

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
# Create the virtual environment
uv venv

# Install the necessary dependencies
uv pip install -r requirements.txt
uv pip install -r dev_requirements.txt
```

## Running the script

### Vanilla Mode

The script can be run in it's regular mode using a variety of commands:
- `uv run python span_digital.py -h` - will generate the help page
- `uv run python span_digital.py -s` - will allow you to enter the match scores in via the **interactive** mode, following the format described above, i.e. "<team name> <team score>, <team name> <team score>"
- `uv run python span_digital.py <file_name>` - will allow you to have the script read the matches from a provided file. There are 3 files to play with:
  - `uv run python span_digital.py sample_input.txt` - a very small list of matches
  - `uv run python span_digital.py sample_input_with_errors.txt` - a small list of matches but frought with errors
  - `uv run python span_digital.py sample_input_large.txt` - a larger list of 1000 matches played between English Premiere League teams (with made-up data)

### Live Mode

The scripts fancy mode is when the live mode is invoked. This will render the leaderboard live and update it as the matches are played, reflecting how teams are going up or down the leaderboard based on their matches. This is best seen with the large file, eg. `python span_digital.py sample_input_large.txt -l`


### Automated Tests

Run `pytest .` to run the test suite.


## Other Scripts

### Sample File Generation

By tweaking the script in `generate_sample_file.py`, very long random files can be created to test the script. To run it:
`python generate_sample_file.py`.
