#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:24:27 2019

@author: alyssa
"""

#Parsing code:
import numpy as np
import csv

def read_stats():
    csv_file = open("batting_line_up_data.csv")
    total_row = sum(1 for row in csv_file) - 1
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file, delimiter = ",")
    batting_average = np.zeros((total_row,))
    on_base = np.zeros((total_row,))
    slugging = np.zeros((total_row,))
    strike_out = np.zeros((total_row,))
    stolen_bases = np.zeros((total_row,))
    batter_names = [None] * total_row # np.empty((total_row,))
    i = 0 
    for row in csv_reader:
        if i != 0:
            batter_names [i-1] = row[0]
            batting_average [i-1] = (float(row[1]) - .177)/.169
            on_base [i-1] = (float(row[2]) - .232)/.206
            slugging [i-1] = (float(row[3]) - .279)/.361
            strike_out [i-1] = 1 - (float(row[4]) - .144)/.145
            stolen_bases [i-1] = (float(row[5]) - 1)/29
        i += 1
    csv_file.close()
    return batting_average, on_base, slugging, strike_out, stolen_bases, batter_names


print(read_stats())

