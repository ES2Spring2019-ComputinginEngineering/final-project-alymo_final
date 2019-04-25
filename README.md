You should include in your final project readme a description of the project, a list of all the files that you have created and instructions for use.

This readme is written in a language called markdown. This is not a programming language but a formatting langauge. There are symbols (syntax) used to indicate how to format the text. For example the pound symbol (i.e. the hashtag) is used to format a title; two of the same symbol format a heading, and three format a sub-heading.

Below is some example text in markdown however this alone is not suffiecent for the final project. **Make sure you follow the directions on Canvas.**
---------------------------------------------

# Baseball Statistics

Our program takes in batting statistics (batting average, on base percentage, slugging percentage, stolen bases, and strike out percentage) from a team and uses optimization functions (unique to each batter) to return the best lineup, which will maximize the amount of runs scored. It then tests this hypothesized lineup by simulating a game by running through the batting lineup over nine innings by looking at who is on base and the chance of the batter to get on base to determine the final score of the game. The computer generated lineup using our program was run as well as a random lineup to compare the results and determine if the program which generated a lineup using stats was effective.

After the maximized lineup is generated, a theoretical score of the team could be generated using the game simulation. Bear in mind that the score considers only the ability of the players and not the opponents, and therefore the total runs scored is likely higher than that of an actual game. Runs scored in a single inning is calcualted based whether the hitter was able to hit a single, double, triple, or a homerun, and the function iterates through every single batter on the lineup until the number of outs in an inning reaches three. In the end, the score from each inning is added to the final score. The simulation is repeated as much as the user desires and its results are visually represented in a histogram. 

## Instructions

Describe how the users(instructors) should run your code to see an ***easy to run example of the functionality***. This should all be in a *main.py* "driver" script.

## File List

batting_llineup_data.csv: the file containing categorical statistics of each of the nine batters.
assigning_batters.py: parses the statistics from the csv file and organize them into separate arrays. A maximized, indexed lineup is generated using the given weights.
game_simulation.py: uses the arrays and lineup generated to simulate a baseball game and keeps track of the scores. 
main.py: user inputs the lineup data and other paramters to generate a distribution of total runs scored by that particular lineup. 

## How to format your readme

In your readme, you can:
```
Give code examples
```

You can also include useful links, like this one with information about [formatting markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

You can 
- Also
- Make
- Lists
