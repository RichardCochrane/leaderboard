# League Leaderboards (Java)

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

This particular implementation requires the use of Java v15 or later.

```
# For Linux or WSL
sudo apt install openjdk-17-jdk


# For Mac OSX
brew install maven
```

The app must then be compiled with: `mvn compile`

If there are errors, they are likely because of a mismatched version of Java. To confirm this, run: `mvn -v` and confirm that the version of java is greater than 15. It's possible that even with a later version JDK, an older version is being used by Maven. To fix this, get the path to your JDK as follows:
`readlink -f $(which java) | sed 's:/bin/java::'`

The above value must be entered to the JAVA_HOME variable and the PATH variable updated in your .bashrc, .zshrc or equivalent file:
```
export JAVA_HOME=/path/from/above/command
export PATH=$JAVA_HOME/bin:$PATH
```

## Running the script

The script can be run with the following files:
```
mvn exec:java -Dexec.mainClass="com.leaderboard.Main" -Dexec.args="sample_input.txt"
mvn exec:java -Dexec.mainClass="com.leaderboard.Main" -Dexec.args="sample_input_with_errors.txt"
mvn exec:java -Dexec.mainClass="com.leaderboard.Main" -Dexec.args="sample_input_large.txt"
```

The interactive version of the script can be run as follows:

`mvn exec:java -Dexec.mainClass="com.leaderboard.Main"`


### Automated Tests

Run `mvn test` to run the test suite.
