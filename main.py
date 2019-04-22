"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
from assigning_batters import read_stats, get_lineup, find_batter_index
from game_simulation import score_lineup, hit_quality

# DEMONSTRATION CODE
lineup_indices, batter_names = get_lineup()
print('Batting Lineup:')
for i, batter_index in enumerate(lineup_indices):
    print(str(i+1) + ". " + batter_names[batter_index])

batting_average, on_base, slugging, strike_out, stolen_bases, batter_names = read_stats()
batter_index = find_batter_index("Sandy Leon", batter_names)
hit_quality = hit_quality(batter_index, batter_names, batting_average[batter_index])
print("score: " + str(score_lineup(lineup_indices, batting_average, on_base, stolen_bases, hit_quality)))