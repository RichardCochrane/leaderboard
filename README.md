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

Install golang:
```
wget https://go.dev/dl/go1.24.4.linux-amd64.tar.gz
tar -xvf go1.24.4.linux-amd64.tar.gz
mv go go-1.24.4
sudo mv go-1.24.4 /usr/local
```

These environment variables also need to be added to your `~/.bashrc` or equivalent file:
```
export GOROOT=/usr/local/go-1.24.4
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
```

## Running the script

The script is run with the following:
`go run main.go league.go sample_input.txt`

The tests can be run with the following:
`go test`
