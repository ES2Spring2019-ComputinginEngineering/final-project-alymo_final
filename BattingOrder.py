#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:24:27 2019

@author: alyssa
"""

#Parsing code:
import numpy as np
import csv

def read_data_file():
    csv_file = open('ckd.csv')
    total_row = sum(1 for row in csv_file) - 1
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file, delimiter = ',')
    batting_average = np.zeros((total_row,))
    on_base = np.zeros((total_row,))
    slugging = np.zeros((total_row,))
    strike_out = np.zeros((total_row,))
    stolen_bases = np.zeros((total_row,))
    i = 0 
    for row in csv_reader:
        if i == 0:
            None
        else:
            Glucose[i-1] = (int(row[0]) - 70)/420
            Hemoglobin[i-1] = (float(row[1]) - 3.1)/14.7
            Class[i-1] = int(row[2])
        i += 1
    csv_file.close()
    return batting_average, on_base, slugging, strike_out