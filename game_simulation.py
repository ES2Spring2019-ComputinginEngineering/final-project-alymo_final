import random

def hit_quality(batter_average): #batter_average considers batting averagge, slugging, on_base, and strike out
    bases_hit = 0
    for i in range(4):
        if batter_average > random.random():
            bases_hit += 1
        else:
            break
    return bases_hit

#def stealing(stealing_average): #runner_average considers 
#    bases_stolen = 0 
#        for i in range(4):
#            if stealing_average > random.random():
#                bases_stolen += 1
#        return bases_stolen

def single_lineup_score(on_base, batting_average, lineup_indices): 
    runs = 0
    current_bases = [0] * 4
    for batter in lineup_indices:
        batter_average = (on_base[batter] + batting_average[batter]) / 2
        bases_hit = hit_quality(batter_average)
        if bases_hit == 1:
            current_bases = [1] + current_bases[0:3]
            runs += int(current_bases[3])
        if bases_hit == 2:
            current_bases = [1] + current_bases[0:3]
            runs += int(current_bases[3])
            current_bases = [0] + current_bases[0:3]
            runs += int(current_bases[3])
        if bases_hit == 3:
            current_bases = [1] + current_bases[0:3]
            runs += int(current_bases[3])
            current_bases = [0] + current_bases[0:3]
            runs += int(current_bases[3])
            current_bases = [0] + current_bases[0:3]
            runs += int(current_bases[3])
        if bases_hit == 4:
            current_bases[3] = 0
            runs += sum(current_bases) + 1
            current_bases = [0] * 4
    return runs
    
    
def final_score(nlineup, on_base, batting_average, lineup_indices):
    total_runs = 0
    for i in range(nlineup):
        total_runs += single_lineup_score(on_base, batting_average, lineup_indices)
    return total_runs


#    for i in range(ninnings):
#        bases = [None] * 4
#        nhits = hits(lineup)
#        bases[0] = batter
#        next_occupied_base = 5
#        for i, runner in enumerate(reversed(bases)):
#            current_base = 3 - i
#            run = run_quality(runner, on_base, stolen_bases, next_occupied_base, hit_quality, current_base)
#            if current_base + run == 4:
#                total_runs += 1
#                bases[current_base] = None
#            else:
#                bases[current_base + run] = bases[current_base]
#                bases[current_base] = None
#                next_occupied_base = current_base + run
#    return total_runs


#def hits(lineup):
#     for batter in lineup:
#            strikes = 0
#            while strikes < 3:
#                hit_result = hit_quality(batter, batter_names, batting_average)
#                if hit_result == 0:
#                    strikes += 1
#                    continue 
#                else: 
#                    hits = hit_result
#                    return hits