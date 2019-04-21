"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import assigning_batters
import game_simulation



# DEMONSTRATION CODE
lineup_indices, batter_names = assigning_batters.get_lineup()
print('Batting Lineup:')
for i, batter_index in enumerate(lineup_indices):
    print(str(i+1) + ". " + batter_names[batter_index])



