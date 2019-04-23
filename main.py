"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions
# IMPORT STATEMENTS
from assigning_batters import *
from game_simulation2 import *
import numpy as np
import matplotlib.pyplot as plt

# DEMONSTRATION CODE

batting_average, on_base, slugging, strike_out, stolen_bases, batter_names = read_stats()

lineup_indices, batter_names = get_lineup()
print('Batting Lineup:')
for i, batter_index in enumerate(lineup_indices):
    print(str(i+1) + ". " + batter_names[batter_index])

score = np.zeros(50000)
for i in range(50000):
    score[i] = final_score(4, on_base, batting_average, lineup_indices)
average_score = score.mean()
print("\n Average Total Run: " + str(average_score))

plt.hist(score, bins = np.linspace(0, 30, 31) + 0.5)
plt.title("Final Score Distribution")