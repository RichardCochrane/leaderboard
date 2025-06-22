## Introduction

Hi there, I'm Richard 👋

As part of demonstrating some backend developer skills, I've completed the challenge to create a leaderboard ranking script
that takes input and returns the teams in their ranking order.

## TL;DR

- I have produced the solution to the challenge in all four languages, each on it's own branch (Python on `main`, Scala on `scala`, GoLang on `golang` and java on `java`).
- I have a fancy live leaderboard visualizer on the Python version - the see README for instructions to run it
- There are automated tests for each of the scripts - the commands to run them are in the various README files.

## The Challenge

The challenge is to take input, either via a file or via the command line, that will include match results in the format:

`<team name> <team score>, <team name> <team score>`

After completion, the script will return the list of teams in order of points, the points being given to each team: 3 points for a win, 1 point for a draw and 0 points for a loss.

## The Solution
### AI and How We Can Use It

The use of AI in interview challenges can be controversial - after all, if all I'm going to do is use
AI, then why hire me instead of getting another AI license? I'd argue that there are two great reasons for using AI in this project:
- It's a tool that developers can, and should, be using already - using it effectively in this test demonstrates competence with AI
- It can allow us to go further than would ordinarily be possible - see below for what this means.

To mitigate any fears that I have taken shortcuts:
- I have included the original ChatGTP code in a branch called `chat-gtp`
- My Python solution goes way beyond this initial code into better code structure and improved readability
- My Python solution includes a special feature that, while unnecessary, is pretty darn cool
- I also used ChatGTP to help me get the program working in Scala, Java and GoLang - languages that I have no experience in at all

### What the Script Will Do

The script is offered in two forms, **interactive** and using an **input file** (the means to using both are described in the various README files). I included 3 different files:
- `sample_input.txt` which has the sample input from the assignment
- `sample_input_with_errors.txt` which includes lines that are broken (wrong data type, too many columns, too few columns, etc)
- `sample_input_large.txt` which has the sample input from a generation script that includes 1000 matches

If the script (both interactive and via input file for the Python version) detects any errors in the input, it will list
the issues and then prompt you to continue or not. Should you choose to continue, only the valid lines will be processed.

There are automated tests and the command to run them being in the README files as well.

The Python version has a special live preview that renders each match one by one, with the leaderboard updating in realtime, also
reflecting the change in the position for teams on the leaderboard.

The Python solution exists on the `main` branch, while the Scala, Java and Golang solutions exist on the respective branches with those names.

To make it super simple, the links to the 4 README's are:
- [Python](https://github.com/RichardCochrane/leaderboard/tree/main?tab=readme-ov-file)
- [Java](https://github.com/RichardCochrane/leaderboard/tree/java?tab=readme-ov-file)
- [Scala](https://github.com/RichardCochrane/leaderboard/tree/scala?tab=readme-ov-file)
- [GoLang](https://github.com/RichardCochrane/leaderboard/tree/golang?tab=readme-ov-file)


### Limitations

My experience with Python allowed me to structure the code more sensibly, aiding readability and maintainability of code. However, my lack of experience with Scala, Java and GoLang mean that my solutions for those are less refined. While ChatGTP provided a lot of the work there, it had issues in both the script and the tests that required fixing in all 3 languages. The process of getting these languages to work required some time, patience, sweat and tears and I've documented the necessary packages and steps in the README to install and run the various commands but I acknowledge that seasoned developers may do things quite differently to the way I have (for these 3 languages).

My tests for Scala, Java and GoLang are just the tests that ChatGTP provided, but corrected so that they pass - somehow the AI couldn't produce passing tests in any of the languages. The tests for Python are more extensive, which come from my experience with the language.
