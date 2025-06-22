# League Leaderboards (Golang)

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

Install golang:
```
# Linux
wget https://go.dev/dl/go1.24.4.linux-amd64.tar.gz
tar -xvf go1.24.4.linux-amd64.tar.gz
mv go go-1.24.4
sudo mv go-1.24.4 /usr/local

# Mac OSX
brew install go
```

These environment variables also need to be added to your `~/.bashrc` or equivalent file:
```
# Linux (having installed Go using the package installation above)
export GOROOT=/usr/local/go-1.24.4
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH

# Mac OSX
Nothing required
```

## Running the script

The script is run with the following files as follows:
```
go run main.go league.go sample_input.txt
go run main.go league.go sample_input_with_errors.txt
go run main.go league.go sample_input_large.txt
```

The interactive version of the script can be run as follows:

`go run main.go league.go`

### Automated Tests

Run `go test` to run the test suite.
