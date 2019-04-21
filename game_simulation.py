import numpy as np
import random

def hit_quality(batter, batting_average):
    hit_quality = 0
    for i in range(4):
        if batting_average > random.random():
            hit_quality += 1
        else:
            break
    return hit_quality

def run_quality(batter, on_base, stolen_bases, next_occupied_base, hit_quality, current_base):
    bases_run = min(next_occupied_base - current_base - 1, hit_quality * random.random() * stolen_bases)
    return bases_run

def score_lineup(lineups, ): #pass in the stats
    total_runs = 0
    ninnings = 9
    for i in range(ninnings):
        bases = [None] * 4
        for batter in lineup:
            strikes = 0
            while strikes < 3:
                hit_result = get_hit_result(batter)
                if hit_result == 0:
                    strikes += 1
                    break
                bases[0] = batter
                next_occupied_base = 5
                for i, runner in enumerate(reversed(bases)):
                    current_base = 3 - i
                    run = run_quality(runner, on_base, stolen_bases, next_occupied_base, hit_quality, current_base)
                    if current_base + run == 4:
                        total_runs += 1
                        bases[current_base] = None
                    else:
                        bases[current_base + run] = bases[current_base]
                        bases[current_base] = None
                        next_occupied_base = current_base + run
    return total_runs
